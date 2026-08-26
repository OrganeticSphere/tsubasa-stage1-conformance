# Tobi Runs for v0.2 — macOS arm64

**Status:** macOS real-run evidence completed; no release/tag authorization<br>
**Evidence verdict:** MACOS_EVIDENCE_COMPLETE_ALL_MATCH<br>
**Scope:** existing 12-case public baseline only

This report records a bounded native macOS arm64 execution of the existing
public Tsubasa Conformance Corpus. Tobi Validator is the applicable Reasoning
Artifact Validator. This is observed process evidence, not certification,
proof of truth, or a universal correctness claim.

## Evidence context

- Evidence source head: c0bf99d2b2bc04212e32c50ea51acc02dd58139e
- Evidence time (UTC): 2026-08-26T02:26:11Z
- Workflow run: 32922703063, temporary-macos-evidence-capture, completed / success
- Runtime: fresh GitHub-hosted macOS VM
- Runner label: macos-14
- Runner image: macos14 20260629.0180.1
- macOS version: 14.8.7
- macOS build: 23J520
- Darwin kernel release: 23.6.0
- Darwin kernel version: Darwin Kernel Version 23.6.0: Tue Apr 21 20:17:41 PDT 2026; root:xnu-10063.141.1.712.16~1/RELEASE_ARM64_VMAPPLE
- Architecture: arm64
- Hardware model: VirtualMac2,1
- Python used by the evidence runner: Python 3.14.6
- Manifest: corpus/manifest.v0.1.json
- Manifest SHA-256: ab7fb64f088cb3bf05f356922bc3edc5990c2ae7ca8bb5eb000cee342c268c3d

## Binary provenance

The executable came from the authorized released distribution identified as
stage1-tobi-validator-v0.7.0. The asset was selected only after the native
runtime reported arm64.

| Item | Observed identity |
|---|---|
| Outer asset | macos-arm64-release-archive.zip |
| Expected outer SHA-256 | 425ea8f11b3aefcd75cb17101fedd2ed0541d6bfc73162b77ca47694ef25cb16 |
| Actual outer SHA-256 | 425ea8f11b3aefcd75cb17101fedd2ed0541d6bfc73162b77ca47694ef25cb16 |
| Outer checksum sidecar SHA-256 | b5f60bbd5382ddc20fdc1d8bc1667f89f34b78183ee6eb874b43d15a45450d2e |
| Nested payload | stage1-tobi-validator-v0.7.0-macos-arm64.tar.gz |
| Nested payload SHA-256 | bf1323a35f41eb63bef84171f5ae72e607b71bf61bba6c4989fae78bc23f8ac3 |
| Executable SHA-256 | b381a3bc5e026513a855919083fb7face3517d3b0b7e1a60aaca81839387317a |
| Exact executable path | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi |

The outer checksum sidecar and the nested payload sidecar both verified before
execution. The extracted executable SHA-256 was recomputed on the macOS host.
The controlled asset was delivered through temporary encrypted workflow
secrets; those secrets were deleted after capture. No credential or private
download URL is retained in the repository, report, matrix, or public workflow
logs.

## Capture-artifact integrity

The public-safe capture artifact contained only JSON evidence and its checksum
manifest:

| File | SHA-256 |
|---|---|
| raw-evidence-v0.2-macos.json | b2a464ccc8b8723f44ce57f54a5b0b03a78aca9634b2bdee607f6c0005dc82ed |
| macos-runtime-provenance.json | 07c26ccdc3c9539fedf5a10dd0e819ae1c71365007fd46934c1c07d9d60454d6 |
| SHA256SUMS.txt | ffcaa075f9e38131ee62ada0de0bd5da36a71b613b7d12cd44d1c47cb48fc08f |

The artifact checksum manifest was independently verified after download.
[EVIDENCE_MATRIX_v0.2.json](EVIDENCE_MATRIX_v0.2.json) retains the public-safe
observations, including raw byte lengths, SHA-256 values, Base64, and escaped
UTF-8.

## Raw-output notation

Every process result was captured before parsing. In this report, \n denotes
one literal LF byte. No CR/LF or whitespace normalization was performed before
raw hashes were calculated.

| Label | Exact escaped bytes |
|---|---|
| S_BIND_X | stdout, UTF-8, 106 bytes, SHA-256 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e: CANON:\nbind(ID(x), DEC(1), ID(x))\n\nHASH:\n8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06\n; stderr empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| S_BIND_Y | stdout, UTF-8, 106 bytes, SHA-256 1764c15e07d8409e0bd08ad2cd834e83b9dfc9e7a05f24015731fc6c427587af: CANON:\nbind(ID(y), DEC(2), ID(y))\n\nHASH:\n37205233a0fffc2592fa3cc385356b10d13e73af3332dd75be01a294e71b9c79\n; stderr empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| S_SEQUENCE | stdout, UTF-8, 141 bytes, SHA-256 6d6f48e615e82da2122fdc2356eeb224a5861a42e6b89853695a857fd360df06: CANON:\nseq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])\n\nHASH:\n756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96\n; stderr empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| R_E023 | stdout empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; stderr, UTF-8, 57 bytes, SHA-256 413d4105258014530535f488497ec3dbcdf8ff3651a4233fd01872899107d560: Error: E023: expected identifier after 'let' (span 3..4)\n |
| R_E013 | stdout empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; stderr, UTF-8, 49 bytes, SHA-256 6679ecbe768c51151945ceaad30323b614d5ccee93208c7ae47816d80502f1af: Error: E013: invalid number literal (span 8..11)\n |
| S_REINPUT | stdout, UTF-8, 167 bytes, SHA-256 a5eaf0fbb63b6bdeed8dcd65cb3a4f31595ec1ab7dda7509a497acb8ff1c481a: CANON:\nCALL(ID(bind), [CALL(ID(ID), [ID(x)]), CALL(ID(DEC), [DEC(1)]), CALL(ID(ID), [ID(x)])])\n\nHASH:\n95e695c394519984dc8347ae6176d1f67585126aa08ae116b4c9194800d17710\n; stderr empty, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

## macOS case observations

All commands used the exact executable path recorded above.

| Case | Exact command | Exit | Raw output | Parsed observation | Windows v0.1 | Linux v0.2 |
|---|---|---:|---|---|---|---|
| accept.basic_bind_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/accept/basic_bind_001.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH | MATCH, raw SHA-256 |
| accept.basic_bind_002 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/accept/basic_bind_002.tsubasa | 0 | S_BIND_Y | bind(ID(y), DEC(2), ID(y)); compatibility identity 37205233a0fffc2592fa3cc385356b10d13e73af3332dd75be01a294e71b9c79 | MATCH | MATCH, raw SHA-256 |
| accept.atomic_sequence_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/accept/atomic_sequence_001.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); compatibility identity 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH | MATCH, raw SHA-256 |
| reject.invented_syntax_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/reject/invented_syntax_001.tsubasa | 1 | R_E023 | E023; expected identifier after 'let'; span 3..4 | MATCH | MATCH, raw SHA-256 |
| reject.malformed_decimal_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/reject/malformed_decimal_001.tsubasa | 1 | R_E013 | E013; invalid number literal; span 8..11 | MATCH | MATCH, raw SHA-256 |
| equivalence.decimal_convergence.decimal_1 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/equivalence/decimal_convergence/decimal_1.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH | MATCH, raw SHA-256 |
| equivalence.decimal_convergence.decimal_1_0 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/equivalence/decimal_convergence/decimal_1_0.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH | MATCH, raw SHA-256 |
| equivalence.decimal_convergence.decimal_01_000 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/equivalence/decimal_convergence/decimal_01_000.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH | MATCH, raw SHA-256 |
| equivalence.sequence_skin_convergence.semicolon | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/equivalence/sequence_skin_convergence/semicolon.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); compatibility identity 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH | MATCH, raw SHA-256 |
| equivalence.sequence_skin_convergence.triangle | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/equivalence/sequence_skin_convergence/triangle.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); compatibility identity 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH | MATCH, raw SHA-256 |
| idempotence.basic_bind_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/idempotence/basic_bind_001/source.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | RAW_BYTE_COMPARISON_NOT_AVAILABLE; historical pending case | MATCH, raw SHA-256 |
| determinism.basic_bind_001 | /Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon corpus/determinism/basic_bind_001/source.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); compatibility identity 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH | MATCH, raw SHA-256 |

The compatibility identity is recorded only for compatibility comparison. It
is not proof, certification, truth, signature, or consensus.

## Cross-platform comparison

For the 11 historical VERIFIED_WITH_TOBI cases:

~~~text
WINDOWS_FIELD_MATCH: 11
WINDOWS_DIVERGENCE_OBSERVED: 0
WINDOWS_RAW_BYTES: RAW_BYTE_COMPARISON_NOT_AVAILABLE

LINUX_FIELD_MATCH: 11
LINUX_DIVERGENCE_OBSERVED: 0
RAW_LINUX_MACOS_STDOUT_STDERR_SHA256_MATCH: 11
~~~

The pending idempotence primary run also matched the Linux process fields and
raw stdout/stderr SHA-256, but it was not promoted into the historical Windows
baseline. Across all 12 primary case runs, the Linux and macOS stdout/stderr
byte lengths, SHA-256 values, and UTF-8 text matched.

This is a bounded comparison of the recorded Windows, Linux, and macOS
observations. Windows v0.1 did not retain raw process-byte captures, so no
three-platform raw-byte equality claim is made.

## Determinism

determinism.basic_bind_001 was run three additional times with the same
released executable, source bytes, command, arm64 machine architecture, and
fresh macOS VM context.

| Run | Exit | stdout | stderr | Linux v0.2 raw comparison |
|---:|---:|---|---|---|
| 1 | 0 | S_BIND_X, 106 bytes, 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e | empty, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | MATCH |
| 2 | 0 | S_BIND_X, 106 bytes, 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e | empty, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | MATCH |
| 3 | 0 | S_BIND_X, 106 bytes, 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e | empty, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | MATCH |

Result: SAME_CONTEXT_BYTE_IDENTICAL.

This is same-context repeatability evidence only. It is not a universal
determinism claim.

## Idempotence observation

The authored source produced S_BIND_X. Its actual canonical ASCII was written
as UTF-8 with no added newline to:

~~~text
/var/folders/g3/pffjr_y96bq06blnkf72x_hw0000gn/T/tobi-v02-idempotence-hwfsi2y0/canonical-reinput.tsubasa
~~~

The exact second command was:

~~~text
/Users/runner/work/_temp/tobi-v02-macos-evidence/release/stage1-tobi-validator-v0.7.0-macos-arm64/tobi canon /var/folders/g3/pffjr_y96bq06blnkf72x_hw0000gn/T/tobi-v02-idempotence-hwfsi2y0/canonical-reinput.tsubasa
~~~

The second run exited 0, emitted S_REINPUT, and had empty stderr.

Result: NON_IDEMPOTENT_REINPUT_OBSERVED.

Both idempotence process results matched the corresponding Linux v0.2 raw
stdout/stderr SHA-256 values. The transient file and containing directory were
deleted by the runner. The historical v0.1 manifest remains
PENDING_REAL_TOBI_RUN for this case.

## Boundary confirmation and limitations

- Only the existing 12 public .tsubasa sources were used.
- The historical v0.1 files and all corpus sources were not modified.
- The Linux platform observation in the v0.2 matrix was not rewritten; the
  macOS platform observation was added.
- No validator binary, archive, credential, authorization header, private URL,
  private fixture, golden corpus, environment dump, or transient input is
  committed.
- Temporary encrypted delivery secrets were deleted after the successful run.
- The one-use capture workflow is removed from the final repository tree.
- No Tsubasa or Tobi semantics changed and no language coverage was added.
- This run covers one GitHub-hosted macOS 14.8.7 arm64 VM. It does not provide
  an Intel macOS observation or establish universal cross-platform behavior.

## Final evidence verdict

MACOS_EVIDENCE_COMPLETE_ALL_MATCH

The existing 12-case baseline was executed on a native arm64 macOS VM with the
identified released binary. All 11 historical verified case fields matched
both Windows and Linux; their Linux/macOS stdout and stderr hashes also
matched. No divergence was observed, while the historical idempotence case
remains pending and its direct canonical re-input observation remains
non-idempotent.
