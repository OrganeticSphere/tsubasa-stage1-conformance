# Tobi Runs for v0.2 — Linux x86_64

**Status:** Linux real-run evidence completed; no release/tag authorization
**Evidence verdict:** LINUX_EVIDENCE_COMPLETE_ALL_MATCH
**Scope:** existing 12-case public baseline only

This report records a bounded Linux x86_64 execution of the existing public
Tsubasa Conformance Corpus. It is evidence of observed validator behavior, not
certification, a proof of truth, or a universal correctness claim.

## Evidence context

- Repository HEAD at execution: c9a6b9c3754fef4207af84f4c8fe7bf36670875a
- Manifest: corpus/manifest.v0.1.json
- Manifest SHA-256: ab7fb64f088cb3bf05f356922bc3edc5990c2ae7ca8bb5eb000cee342c268c3d
- Evidence time (UTC): 2026-08-26T01:27:25Z
- Validator product: Tobi Validator (Reasoning Artifact Validator)
- Validator release identity: stage1-tobi-validator-v0.7.0
- Platform: Linux x86_64
- OS/kernel: Linux 5.15.133.1-microsoft-standard-WSL2, #1 SMP Thu Oct 5 21:02:42 UTC 2023
- Runtime: local Docker Linux runtime, python:3.12-slim
- Runtime image digest: sha256:7a8b475003c4fe15a2cd4e55e5cfc2f3560bdc9333d624f24cdd6d4340fd7a17
- Executable path used: /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi
- Executable SHA-256: 50139a073320616b2e77cfc9e5fe53f94882244b12e88dcf27c01379e31fa9c9

## Binary provenance

The executable came from an authorized released distribution. A preserved local
copy of linux-x86_64-release-archive.zip was matched to the controlled release
asset digest:

~~~text
outer archive SHA-256:
1ba2efaba37c697995d5e333de5f128f3623dba5903179b10833c336522e8c6d

nested payload:
stage1-tobi-validator-v0.7.0-linux-x86_64.tar.gz

nested payload SHA-256:
b6c11630447496163d88967f626e2b2ba5dd2a02826a550febf46c265e8cb802
~~~

Both the outer and nested checksum sidecars matched before execution. The
executable SHA-256 above was recomputed from the extracted Linux binary and
matched its packaged SHA256SUMS.txt entry. No credential, archive, binary, or
private download URL is recorded here.

## Raw-output notation

Every process result was captured before parsing. The matrix at
[EVIDENCE_MATRIX_v0.2.json](EVIDENCE_MATRIX_v0.2.json) stores each case's
actual command, byte length, SHA-256, and escaped UTF-8 output. In this report,
\n denotes a literal LF byte; outputs were not CR/LF-normalized.

The following raw payload labels are referenced by the case table:

| Label | Exact escaped bytes |
|---|---|
| S_BIND_X | stdout, UTF-8, 106 bytes, 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e: CANON:\nbind(ID(x), DEC(1), ID(x))\n\nHASH:\n8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06\n; stderr: empty, 0 bytes, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| S_BIND_Y | stdout, UTF-8, 106 bytes, 1764c15e07d8409e0bd08ad2cd834e83b9dfc9e7a05f24015731fc6c427587af: CANON:\nbind(ID(y), DEC(2), ID(y))\n\nHASH:\n37205233a0fffc2592fa3cc385356b10d13e73af3332dd75be01a294e71b9c79\n; stderr: empty, 0 bytes, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| S_SEQUENCE | stdout, UTF-8, 141 bytes, 6d6f48e615e82da2122fdc2356eeb224a5861a42e6b89853695a857fd360df06: CANON:\nseq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])\n\nHASH:\n756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96\n; stderr: empty, 0 bytes, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| R_E023 | stdout: empty, 0 bytes, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; stderr, UTF-8, 57 bytes, 413d4105258014530535f488497ec3dbcdf8ff3651a4233fd01872899107d560: Error: E023: expected identifier after 'let' (span 3..4)\n |
| R_E013 | stdout: empty, 0 bytes, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; stderr, UTF-8, 49 bytes, 6679ecbe768c51151945ceaad30323b614d5ccee93208c7ae47816d80502f1af: Error: E013: invalid number literal (span 8..11)\n |

## Linux case observations

All primary commands used the exact executable path above followed by
canon and a relative .tsubasa path.

| Case | Exact command | Exit | Raw output | Parsed observation | Windows v0.1 comparison |
|---|---|---:|---|---|---|
| accept.basic_bind_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/accept/basic_bind_001.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH |
| accept.basic_bind_002 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/accept/basic_bind_002.tsubasa | 0 | S_BIND_Y | bind(ID(y), DEC(2), ID(y)); _h 37205233a0fffc2592fa3cc385356b10d13e73af3332dd75be01a294e71b9c79 | MATCH |
| accept.atomic_sequence_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/accept/atomic_sequence_001.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); _h 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH |
| reject.invented_syntax_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/reject/invented_syntax_001.tsubasa | 1 | R_E023 | E023; expected identifier after 'let'; span 3..4 | MATCH |
| reject.malformed_decimal_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/reject/malformed_decimal_001.tsubasa | 1 | R_E013 | E013; invalid number literal; span 8..11 | MATCH |
| equivalence.decimal_convergence.decimal_1 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/equivalence/decimal_convergence/decimal_1.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH |
| equivalence.decimal_convergence.decimal_1_0 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/equivalence/decimal_convergence/decimal_1_0.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH |
| equivalence.decimal_convergence.decimal_01_000 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/equivalence/decimal_convergence/decimal_01_000.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH |
| equivalence.sequence_skin_convergence.semicolon | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/equivalence/sequence_skin_convergence/semicolon.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); _h 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH |
| equivalence.sequence_skin_convergence.triangle | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/equivalence/sequence_skin_convergence/triangle.tsubasa | 0 | S_SEQUENCE | seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))]); _h 756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96 | MATCH |
| idempotence.basic_bind_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/idempotence/basic_bind_001/source.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | Pending v0.1 baseline; not promoted |
| determinism.basic_bind_001 | /release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/determinism/basic_bind_001/source.tsubasa | 0 | S_BIND_X | bind(ID(x), DEC(1), ID(x)); _h 8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06 | MATCH |

_h is recorded as a compatibility identity only. It is not a proof,
signature, certification, truth identity, or consensus claim.

## Cross-platform comparison

For each of the 11 VERIFIED_WITH_TOBI v0.1 cases, the recorded Linux exit
code, canonical ASCII, compatibility identity, and applicable diagnostic
code/message/span matched the Windows v0.1 record:

~~~text
MATCH: 11
DIVERGENCE_OBSERVED: 0
~~~

The v0.1 historical artifacts record successful CLI framing and diagnostic text,
but do not preserve process-byte captures. Therefore this report does not claim
Windows/Linux raw-byte equality; it retains Linux raw bytes and records
NOT_AVAILABLE_FROM_V0_1_RECORD for that byte-level comparison boundary.

## Determinism

determinism.basic_bind_001 was run three additional times with the same
released binary, source bytes, command, platform, and environment policy.

| Run | Exit | stdout | stderr |
|---:|---:|---|---|
| 1 | 0 | S_BIND_X (106 bytes; 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e) | empty (0 bytes; e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855) |
| 2 | 0 | S_BIND_X (106 bytes; 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e) | empty (0 bytes; e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855) |
| 3 | 0 | S_BIND_X (106 bytes; 508f65205d3f929432adfc2520bf30d29dcb8749c3cc6f9a2681139cccb3cf1e) | empty (0 bytes; e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855) |

Result: SAME_CONTEXT_BYTE_IDENTICAL.

This is limited to the same released binary, Linux platform, command, source,
and recorded repetitions. It is not a universal determinism claim.

## Idempotence observation

The authored source was run first:

~~~text
/release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon corpus/idempotence/basic_bind_001/source.tsubasa
~~~

It produced S_BIND_X: canonical ASCII bind(ID(x), DEC(1), ID(x)) and
compatibility identity
8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06.

That actual canonical ASCII was written as UTF-8 without an added newline to the
transient file /tmp/tobi-v02-idempotence-_xfz6p6x/canonical-reinput.tsubasa
outside the repository, then run with the same executable. The transient
directory was deleted immediately after capture.

~~~text
/release/stage1-tobi-validator-v0.7.0-linux-x86_64/tobi canon /tmp/tobi-v02-idempotence-_xfz6p6x/canonical-reinput.tsubasa
~~~

The second run exited 0 with empty stderr and this exact escaped stdout
(UTF-8, 167 bytes, SHA-256
a5eaf0fbb63b6bdeed8dcd65cb3a4f31595ec1ab7dda7509a497acb8ff1c481a):

~~~text
CANON:\nCALL(ID(bind), [CALL(ID(ID), [ID(x)]), CALL(ID(DEC), [DEC(1)]), CALL(ID(ID), [ID(x)])])\n\nHASH:\n95e695c394519984dc8347ae6176d1f67585126aa08ae116b4c9194800d17710\n
~~~

Result: NON_IDEMPOTENT_REINPUT_OBSERVED.

The historical v0.1 manifest remains PENDING_REAL_TOBI_RUN for this case.
No pending status or expected output was promoted.

## Boundary confirmation and limitations

- Only the existing public .tsubasa sources were used as primary inputs.
- The repository was mounted read-only during Linux execution.
- No validator binary, archive, credential, authorization header, private URL,
  private fixture, golden corpus, environment dump, or transient file was
  committed.
- No Tsubasa or Tobi semantics changed.
- No language coverage was added.
- The historical v0.1 Windows evidence does not permit a raw process-byte
  equality claim, even though all of its recorded comparison fields matched.
- This run does not establish Linux/macOS parity or universal cross-platform
  determinism.

## Final evidence verdict

LINUX_EVIDENCE_COMPLETE_ALL_MATCH

The existing 12-case baseline was executed on Linux x86_64 using the identified
released binary. All 11 v0.1 verified case fields matched the Windows record;
the pending idempotence case remained pending and the direct re-input observation
remained non-idempotent.
