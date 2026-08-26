#!/usr/bin/env python3
"""Capture bounded v0.2 evidence from an explicitly supplied Tobi binary.

This tool deliberately does not implement Tsubasa parsing, canonicalization, or
diagnostics.  It invokes the supplied executable against the existing manifest
sources and records the exact process outputs before making any bounded
comparison to the historical v0.1 manifest expectations.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import platform as host_platform
import re
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_RELEASE = "stage1-tobi-validator-v0.7.0"
DEFAULT_PLATFORM = "linux-x86_64"
ROOT = Path(__file__).resolve().parents[1]
MANIFEST_RELATIVE_PATH = Path("corpus/manifest.v0.1.json")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def raw_output(value: bytes) -> dict[str, Any]:
    try:
        text = value.decode("utf-8")
        utf8_valid = True
    except UnicodeDecodeError:
        text = value.decode("utf-8", errors="replace")
        utf8_valid = False

    return {
        "byte_length": len(value),
        "sha256": sha256_bytes(value),
        "base64": base64.b64encode(value).decode("ascii"),
        "utf8_valid": utf8_valid,
        "text": text,
    }


def text_for_parsing(capture: dict[str, Any]) -> str | None:
    if not capture["utf8_valid"]:
        return None
    return str(capture["text"])


def parse_success_framing(stdout: dict[str, Any]) -> dict[str, Any]:
    """Parse only actual CANON:/HASH: framing emitted by the executable."""

    text = text_for_parsing(stdout)
    parsed: dict[str, Any] = {
        "framing": "NOT_PARSED",
        "canonical_ascii": None,
        "compatibility_identity": None,
    }
    if text is None:
        parsed["framing"] = "NON_UTF8_STDOUT"
        return parsed

    lines = text.splitlines()
    try:
        canon_index = lines.index("CANON:")
        hash_index = lines.index("HASH:", canon_index + 1)
    except ValueError:
        parsed["framing"] = "CANON_HASH_FRAMING_NOT_OBSERVED"
        return parsed

    canonical_lines = lines[canon_index + 1 : hash_index]
    # The observed CLI framing separates CANON payload from HASH with one empty
    # line. Preserve raw stdout above; remove only that framing separator from
    # the parsed canonical field.
    if canonical_lines and canonical_lines[-1] == "":
        canonical_lines = canonical_lines[:-1]
    hash_lines = lines[hash_index + 1 :]
    if not canonical_lines or not hash_lines:
        parsed["framing"] = "INCOMPLETE_CANON_HASH_FRAMING"
        return parsed

    parsed["framing"] = "CANON_HASH_FRAMING_OBSERVED"
    parsed["canonical_ascii"] = "\n".join(canonical_lines)
    parsed["compatibility_identity"] = hash_lines[0]
    if len(hash_lines) > 1:
        parsed["unparsed_hash_trailing_lines"] = hash_lines[1:]
    return parsed


DIAGNOSTIC_PATTERN = re.compile(
    r"^Error:\s*(?P<code>E\d+):\s*(?P<message>.*?)(?:\s+\(span\s+(?P<start>\d+)\.\.(?P<end>\d+)\))?$"
)


def parse_diagnostic(stderr: dict[str, Any]) -> dict[str, Any] | None:
    text = text_for_parsing(stderr)
    if text is None:
        return None
    for line in text.splitlines():
        match = DIAGNOSTIC_PATTERN.fullmatch(line)
        if match is None:
            continue
        span = None
        if match.group("start") is not None:
            span = {
                "start": int(match.group("start")),
                "end": int(match.group("end")),
            }
        return {
            "code": match.group("code"),
            "message": match.group("message"),
            "span": span,
        }
    return None


def command_display(command: list[str]) -> str:
    return shlex.join(command)


def invoke_tobi(
    *,
    tobi: Path,
    argument: str,
    cwd: Path,
    source_label: str,
) -> dict[str, Any]:
    command = [str(tobi), "canon", argument]
    started_at = utc_now()
    process = subprocess.run(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    stdout = raw_output(process.stdout)
    stderr = raw_output(process.stderr)
    return {
        "source_path": source_label,
        "command": command,
        "command_display": command_display(command),
        "working_directory": str(cwd),
        "started_at_utc": started_at,
        "completed_at_utc": utc_now(),
        "exit_code": process.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "parsed": {
            **parse_success_framing(stdout),
            "diagnostic": parse_diagnostic(stderr),
        },
    }


def compare_to_windows_manifest(case: dict[str, Any], observation: dict[str, Any]) -> dict[str, Any]:
    if case["expected_status"] != "VERIFIED_WITH_TOBI":
        return {
            "classification": "NOT_APPLICABLE_PENDING_WINDOWS_BASELINE",
            "differences": [],
        }

    expected = case["expected"]
    parsed = observation["parsed"]
    differences: list[dict[str, Any]] = []

    def compare(field: str, windows_value: Any, linux_value: Any) -> None:
        if windows_value != linux_value:
            differences.append(
                {
                    "field": field,
                    "windows_recorded": windows_value,
                    "linux_observed": linux_value,
                }
            )

    compare("exit_code", expected["exit_code"], observation["exit_code"])
    compare("canonical_ascii", expected["canonical_ascii"], parsed["canonical_ascii"])
    compare("compatibility_identity", expected["h"]["value"], parsed["compatibility_identity"])

    expected_diagnostic = expected["diagnostic"]
    observed_diagnostic = parsed["diagnostic"]
    if expected_diagnostic is None:
        compare("diagnostic", None, observed_diagnostic)
    else:
        if observed_diagnostic is None:
            compare("diagnostic", expected_diagnostic, None)
        else:
            compare("diagnostic.code", expected_diagnostic["code"], observed_diagnostic["code"])
            compare("diagnostic.message", expected_diagnostic["message"], observed_diagnostic["message"])
            compare("diagnostic.span", expected_diagnostic["span"], observed_diagnostic["span"])
    return {
        "classification": "MATCH" if not differences else "DIVERGENCE_OBSERVED",
        "differences": differences,
        "historical_raw_output_boundary": {
            "stdout": "V0_1_RECORDS_TEXTUAL_FRAMING_ONLY; RAW_PROCESS_BYTES_NOT_AVAILABLE",
            "stderr": (
                "V0_1_RECORDS_DIAGNOSTIC_TEXT_ONLY; RAW_PROCESS_BYTES_NOT_AVAILABLE"
                if expected_diagnostic is not None
                else "V0_1_RECORDS_EMPTY_STDERR_TEXT_ONLY; RAW_PROCESS_BYTES_NOT_AVAILABLE"
            ),
        },
    }


def source_argument(source_path: str, root: Path) -> tuple[str, Path]:
    source = (root / source_path).resolve()
    root_resolved = root.resolve()
    if root_resolved not in source.parents:
        raise ValueError(f"manifest source path escapes repository root: {source_path}")
    if not source.is_file():
        raise ValueError(f"manifest source path is missing: {source_path}")
    return source_path, source


def process_case(case: dict[str, Any], tobi: Path, root: Path) -> dict[str, Any]:
    argument, source = source_argument(case["source_path"], root)
    observation = invoke_tobi(
        tobi=tobi,
        argument=argument,
        cwd=root,
        source_label=case["source_path"],
    )
    observation["case_id"] = case["case_id"]
    observation["class"] = case["class"]
    observation["source_sha256"] = sha256_file(source)
    observation["comparison_to_windows_manifest"] = compare_to_windows_manifest(case, observation)
    return observation


def determinism_observation(
    *,
    case: dict[str, Any],
    tobi: Path,
    root: Path,
    repetitions: int,
) -> dict[str, Any]:
    argument, source = source_argument(case["source_path"], root)
    runs = [
        invoke_tobi(tobi=tobi, argument=argument, cwd=root, source_label=case["source_path"])
        for _ in range(repetitions)
    ]
    byte_signatures = {
        (
            run["exit_code"],
            run["stdout"]["base64"],
            run["stderr"]["base64"],
        )
        for run in runs
    }
    return {
        "case_id": case["case_id"],
        "source_path": case["source_path"],
        "source_sha256": sha256_file(source),
        "repetitions": repetitions,
        "result": (
            "SAME_CONTEXT_BYTE_IDENTICAL"
            if len(byte_signatures) == 1
            else "SAME_CONTEXT_DIVERGENCE_OBSERVED"
        ),
        "runs": runs,
    }


def idempotence_observation(*, case: dict[str, Any], tobi: Path, root: Path) -> dict[str, Any]:
    argument, source = source_argument(case["source_path"], root)
    first = invoke_tobi(tobi=tobi, argument=argument, cwd=root, source_label=case["source_path"])
    first["source_sha256"] = sha256_file(source)
    canonical = first["parsed"]["canonical_ascii"]
    if first["exit_code"] != 0 or canonical is None:
        return {
            "case_id": case["case_id"],
            "result": "NOT_RUN first authored-source run did not emit parseable canonical ASCII",
            "first_run": first,
            "second_run": None,
        }

    with tempfile.TemporaryDirectory(prefix="tobi-v02-idempotence-") as temporary_directory:
        reinput = Path(temporary_directory) / "canonical-reinput.tsubasa"
        reinput.write_bytes(canonical.encode("utf-8"))
        second = invoke_tobi(
            tobi=tobi,
            argument=str(reinput),
            cwd=root,
            source_label=str(reinput),
        )

    same = (
        first["exit_code"] == second["exit_code"]
        and first["parsed"]["canonical_ascii"] == second["parsed"]["canonical_ascii"]
        and first["parsed"]["compatibility_identity"] == second["parsed"]["compatibility_identity"]
    )
    return {
        "case_id": case["case_id"],
        "result": "IDEMPOTENT_REINPUT_OBSERVED" if same else "NON_IDEMPOTENT_REINPUT_OBSERVED",
        "first_run": first,
        "second_run": second,
        "reinput_source_utf8_base64": base64.b64encode(canonical.encode("utf-8")).decode("ascii"),
    }


def find_case(cases: list[dict[str, Any]], case_id: str) -> dict[str, Any]:
    for case in cases:
        if case["case_id"] == case_id:
            return case
    raise ValueError(f"required manifest case is missing: {case_id}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tobi", required=True, type=Path, help="absolute path to an authorized released Tobi binary")
    parser.add_argument("--platform", default=DEFAULT_PLATFORM, help="platform label recorded in evidence")
    parser.add_argument("--validator-release", default=DEFAULT_RELEASE, help="logical released package identity")
    parser.add_argument("--output", required=True, type=Path, help="JSON path outside the repository for raw run capture")
    parser.add_argument("--source-root", default=ROOT, type=Path, help="repository root containing corpus/manifest.v0.1.json")
    parser.add_argument("--determinism-repetitions", default=3, type=int, help="same-context repetitions for determinism.basic_bind_001")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.determinism_repetitions < 3:
        print("error: --determinism-repetitions must be at least 3", file=sys.stderr)
        return 2

    root = args.source_root.resolve()
    tobi = args.tobi.resolve()
    manifest_path = (root / MANIFEST_RELATIVE_PATH).resolve()
    if not manifest_path.is_file():
        print(f"error: manifest is missing: {manifest_path}", file=sys.stderr)
        return 2
    if not tobi.is_file():
        print(f"error: supplied Tobi binary is missing: {tobi}", file=sys.stderr)
        return 2
    if not os.access(tobi, os.X_OK):
        print(f"error: supplied Tobi binary is not executable: {tobi}", file=sys.stderr)
        return 2

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        cases = manifest["cases"]
        if not isinstance(cases, list) or len(cases) != 12:
            raise ValueError("expected exactly 12 manifest cases")
        observations = [process_case(case, tobi, root) for case in cases]
        determinism = determinism_observation(
            case=find_case(cases, "determinism.basic_bind_001"),
            tobi=tobi,
            root=root,
            repetitions=args.determinism_repetitions,
        )
        idempotence = idempotence_observation(
            case=find_case(cases, "idempotence.basic_bind_001"),
            tobi=tobi,
            root=root,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: evidence run failed: {exc}", file=sys.stderr)
        return 1

    verified_observations = [
        item for item in observations if item["comparison_to_windows_manifest"]["classification"] != "NOT_APPLICABLE_PENDING_WINDOWS_BASELINE"
    ]
    comparison_counts = {
        "match": sum(item["comparison_to_windows_manifest"]["classification"] == "MATCH" for item in verified_observations),
        "divergence_observed": sum(
            item["comparison_to_windows_manifest"]["classification"] == "DIVERGENCE_OBSERVED"
            for item in verified_observations
        ),
    }
    payload = {
        "evidence_version": "0.2-raw-capture",
        "execution_timestamp_utc": utc_now(),
        "case_manifest": str(MANIFEST_RELATIVE_PATH).replace("\\", "/"),
        "case_manifest_sha256": sha256_file(manifest_path),
        "validator_release": args.validator_release,
        "platform": args.platform,
        "os": {
            "system": host_platform.system(),
            "release": host_platform.release(),
            "version": host_platform.version(),
            "machine": host_platform.machine(),
        },
        "executable": {
            "path": str(tobi),
            "sha256": sha256_file(tobi),
        },
        "environment_policy": "Inherited local runtime environment; no environment values are recorded.",
        "case_observations": observations,
        "windows_manifest_comparison_counts": comparison_counts,
        "determinism": determinism,
        "idempotence": idempotence,
    }

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote raw evidence capture: {output}")
    print(
        "Cases executed: {total}; Windows-manifest matches: {matches}; divergences: {divergences}".format(
            total=len(observations),
            matches=comparison_counts["match"],
            divergences=comparison_counts["divergence_observed"],
        )
    )
    print(f"Determinism: {determinism['result']}")
    print(f"Idempotence: {idempotence['result']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
