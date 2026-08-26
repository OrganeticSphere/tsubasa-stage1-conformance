# Tsubasa Conformance Corpus — macOS Evidence Protocol v0.2

**Status:** DRAFT EVIDENCE PROTOCOL — no release/tag authorization<br>
**Scope:** macOS evidence for the existing 12-case public baseline<br>
**Public display name:** Tsubasa Conformance Corpus<br>
**Validator product:** Tobi Validator<br>
**Pinned validator release identity:** `stage1-tobi-validator-v0.7.0`

## 1. Purpose

This protocol defines the macOS follow-up to the merged Linux v0.2 evidence pass.

The goal is narrow: execute the same existing 12 public `.tsubasa` cases using an exact released macOS Tobi Validator artifact, record real process evidence, compare the observations with the recorded Windows v0.1 and Linux v0.2 evidence, repeat the same-context determinism case, and reproduce the two-step idempotence observation.

This protocol does not widen Tsubasa language coverage, change Tobi behavior, create a new manifest schema, publish a release, or authorize a public product claim beyond the recorded evidence.

## 2. Fixed baseline

Use the existing case baseline:

`corpus/manifest.v0.1.json`

Current fixed case set:

- 12 cases total;
- 11 historical `VERIFIED_WITH_TOBI` cases;
- 1 historical pending case: `idempotence.basic_bind_001`.

The v0.1 manifest, v0.1 verification records, merged Linux v0.2 evidence, and all existing corpus source files are evidence/history surfaces. Do not rewrite them to attach macOS observations.

## 3. Native macOS execution requirement

Primary macOS evidence must come from an actual macOS execution environment.

Do not use Linux containers, QEMU/Linux emulation, Wine, Rosetta-only substitution for a different released architecture, copied Playground output, copied Action output, a local Tobi build, a mock, or a semantic reimplementation as primary evidence.

The execution report must record:

- macOS version;
- Darwin kernel version;
- machine architecture;
- whether the host is physical or a GitHub-hosted/other macOS VM;
- exact released artifact selected;
- executable SHA-256;
- execution timestamp UTC.

If no real macOS execution environment is available, stop with:

`MACOS_RUNTIME_UNAVAILABLE`

Do not manufacture evidence.

## 4. Released artifact selection

The current controlled release `stage1-tobi-validator-v0.7.0` publishes both macOS families.

For native Apple Silicon use:

- asset: `macos-arm64-release-archive.zip`
- release asset SHA-256: `425ea8f11b3aefcd75cb17101fedd2ed0541d6bfc73162b77ca47694ef25cb16`

For native Intel macOS use:

- asset: `macos-x86_64-release-archive.zip`
- release asset SHA-256: `b75ca03e12a7fa6772020a09ee4b886b15997b0b9b6125508f144bd4b09933e6`

Select the artifact matching the actual execution architecture. Do not choose an architecture merely because its artifact is easier to obtain.

Verify the outer asset digest against the release metadata and checksum sidecar before execution. Recompute and record the extracted executable SHA-256. If the package contains an inner archive/checksum manifest, verify and record it as well.

No binary, archive, credential, authorization header, private URL, or private distribution log may be committed.

## 5. Existing evidence to compare

Windows baseline:

- `corpus/manifest.v0.1.json`
- `docs/verification/TOBI_RUNS_v0.1.md`

Linux v0.2 evidence:

- `docs/verification/TOBI_RUNS_v0.2.md`
- `docs/verification/EVIDENCE_MATRIX_v0.2.json`

Comparison is field-level unless both sides preserve raw process bytes.

For the 11 Windows-verified cases compare at least:

- exit code;
- canonical ASCII;
- compatibility identity;
- diagnostic code/message/span where applicable.

For Linux v0.2, compare raw stdout/stderr byte hashes in addition to parsed fields where the macOS run captures raw bytes.

Classify each comparison as:

- `MATCH`
- `DIVERGENCE_OBSERVED`
- `RAW_BYTE_COMPARISON_NOT_AVAILABLE`

A divergence is evidence, not automatically a bug.

## 6. Primary case execution

Run every existing case with the exact released executable using:

`<tobi> canon <relative .tsubasa path>`

For each case record:

- exact command;
- source path and source SHA-256;
- exit code;
- raw stdout bytes/length/SHA-256 and escaped UTF-8 when valid;
- raw stderr bytes/length/SHA-256 and escaped UTF-8 when valid;
- parsed canonical ASCII and compatibility identity for successful runs;
- parsed diagnostic code/message/span for rejected runs;
- comparison to Windows v0.1;
- comparison to Linux v0.2.

`_h` remains compatibility identity only. It is not proof, signature, certification, truth, or consensus.

## 7. Determinism observation

For `determinism.basic_bind_001`, run the same command at least three times with the same released binary, source bytes, machine architecture, macOS environment, and command.

Compare exit code, stdout bytes, and stderr bytes.

Classify:

- `SAME_CONTEXT_BYTE_IDENTICAL`
- `SAME_CONTEXT_DIVERGENCE_OBSERVED`

This is same-context repeatability evidence only, not universal determinism.

## 8. Idempotence observation

For `idempotence.basic_bind_001`:

1. run the authored source;
2. capture actual canonical ASCII from the first result;
3. write that canonical ASCII to a temporary UTF-8 `.tsubasa` file outside the repository;
4. run the same macOS binary against the temporary file;
5. capture the second result;
6. delete the temporary file/directory;
7. classify:
   - `IDEMPOTENT_REINPUT_OBSERVED`
   - `NON_IDEMPOTENT_REINPUT_OBSERVED`
   - `NOT_RUN <reason>`.

Do not change the historical v0.1 pending status in this PR.

## 9. Evidence artifacts

Update the merged v0.2 evidence line rather than inventing a new language manifest.

Expected changes after real macOS execution:

- add a macOS platform section to `docs/verification/EVIDENCE_MATRIX_v0.2.json`;
- create `docs/verification/TOBI_RUNS_v0.2_MACOS.md` for the human-readable macOS report;
- update `docs/verification/TOBI_RUNS_v0.2.md` only if a concise platform-summary cross-reference is useful and does not rewrite the Linux evidence;
- adapt `tools/run_tobi_evidence_v0_2.py` only if required for platform-neutral execution. Any tool change must remain a process-evidence runner and must not implement Tsubasa semantics.

Do not create `corpus/manifest.v0.2.json` in this phase.

## 10. Public/private and release boundaries

Do not commit validator binaries, release archives, credentials, private URLs, temporary files, private fixtures, golden corpus, or environment dumps.

Do not create or move any tag or release.

Do not change Project Sources.

Do not widen language coverage.

Do not claim three-platform parity unless the macOS run is complete and the recorded comparison supports that bounded claim.

Even with Windows/Linux/macOS field matches, do not claim universal cross-platform determinism.

## 11. Completion condition

The macOS evidence phase is ready for review only when:

- a real macOS environment is identified;
- exact released macOS binary provenance is established;
- all 12 cases are executed or explicitly blocked;
- the 11 historical verified cases are compared to Windows and Linux;
- determinism is repeated at least three times;
- the two-step idempotence observation is recorded;
- evidence artifacts contain actual observations only;
- historical v0.1 and Linux evidence remain intact except deliberate additive cross-reference/matrix extension;
- public boundary/JSON/structure/diff checks pass;
- exact-head CI state is recorded.

Allowed overall verdicts:

- `MACOS_EVIDENCE_COMPLETE_ALL_MATCH`
- `MACOS_EVIDENCE_COMPLETE_WITH_DIVERGENCE`
- `MACOS_EVIDENCE_PARTIAL`
- `MACOS_EVIDENCE_BLOCKED`
