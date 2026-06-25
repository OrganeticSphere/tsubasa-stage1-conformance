# Tsubasa Stage 1 Conformance Corpus

**Status:** v0.1 verified draft / release-candidate scaffold
**Owner:** AI Verification PM / AI Verification 2.0
**Technical verifier:** Tobi Compiler / Architect
**Scope:** public-safe Stage 1 conformance examples for `.tsubasa` artifacts

This repository is a public conformance and authoring corridor for the released Stage 1 Tobi Validator product line.

It is intended to make Stage 1 behavior more inspectable without publishing the private validator implementation.

## What this repository contains

- public-safe `.tsubasa` examples;
- source-only accept/reject/equivalence/idempotence/determinism cases;
- a manifest format for expected results;
- structure checks for the public corpus;
- documentation explaining public/private boundaries;
- real-run expected-output evidence for 11 cases, with 1 idempotence case still pending.

See [`docs/COVERAGE_LIMITATIONS.md`](docs/COVERAGE_LIMITATIONS.md) for the
verified v0.1 coverage boundary.

## What this repository does not contain

- Tobi compiler or validator source code;
- validator binaries;
- private fixtures;
- private golden corpus;
- private release or distribution logic;
- future product internals;
- a reimplementation of Tobi behavior;
- a public proof/truth/consensus layer.

## Required expected-output discipline

No canonical output, diagnostic expectation, exit code, or hash value may be treated as final unless it comes from a real Tobi Validator run.

Unverified cases must remain marked as:

```json
"expected_status": "PENDING_REAL_TOBI_RUN"
```

A case may be changed to `VERIFIED_WITH_TOBI` only when the verification record includes the exact Tobi release, platform, command, exit code, and observed output. The current v0.1 draft includes 11 `VERIFIED_WITH_TOBI` cases from Tobi Validator `v0.7.0` on Windows x86_64 and keeps `idempotence.basic_bind_001` as `PENDING_REAL_TOBI_RUN`.

## Idempotence limitation

The idempotence category is intentionally reserved in v0.1. The current
idempotence case remains `PENDING_REAL_TOBI_RUN` because direct re-input of
canonical ASCII produced a different canonical form and hash under the verified
v0.7.0 context. This is preserved as a limitation, not hidden as a pass. v0.1
does not claim verified idempotence coverage.

## Hash boundary

`_h`, when present, is a compatibility identity only. It is not a proof of truth, not consensus, and not a certification of the real-world correctness of a reasoning claim.

For v0.1, `_h` is optional and version-bound.

## How to use

1. Review the public examples under `corpus/`.
2. Run structure checks:

```bash
python tools/run_structure_checks.py
```

3. Use an authorized Tobi Validator distribution to run real verification.
4. Update `corpus/manifest.v0.1.json` only from real command output. See `docs/verification/TOBI_RUNS_v0.1.md` for the current v0.1 verification record.

See `docs/HOW_TO_USE_WITH_TOBI_VALIDATOR.md`.

## License

Repository contents are licensed under the Apache License, Version 2.0. See
[`LICENSE`](LICENSE). This license does not license private Tobi binaries,
private distribution artifacts, or private compiler/validator source.

Use of the Organetic, Tobi, and Tsubasa names is also subject to the naming
guard in [`TRADEMARKS.md`](TRADEMARKS.md).

## Ownership

This repository is owned by AI Verification PM because it is a public trust/openness surface for the released Stage 1 product line.

Tobi Compiler / Architect may verify the technical correctness of examples and expected outputs, but ownership does not transfer to the compiler implementation line.
