# Tobi Runs for v0.1

**Status:** technical verification completed with limitations
**Final verdict:** `PASSED_WITH_LIMITATIONS`

This report records real Tobi Validator runs for the public Stage 1 `.tsubasa`
corpus. It is technical verification evidence only. Repository ownership remains
with AI Verification PM / AI Verification 2.0.

## Verification context

- Tobi release identity: `stage1-tobi-validator-v0.7.0`
- Binary source: authorized packaged Stage 1 Tobi Validator distribution
- Executable: `tobi.exe`
- Executable SHA-256: `946f433f98874a9cff5abbacc6c16d8ed49dbd8f41b69877746460fb6a266672`
- Checksum source: packaged `SHA256SUMS.txt` (exact match)
- Platform: Windows x86_64, Microsoft Windows 10.0.26200
- Working directory: repository root
- Command form: `tobi.exe canon <relative .tsubasa path>`
- Verification date: 2026-06-20

The executable does not implement `--version`; that command exits 2. The release
identity is therefore package/tag and checksum based rather than CLI self-reported.

## Public structure checks

Command:

```text
python tools/run_structure_checks.py
```

Initial verification run result: exit 0.

```text
OK: manifest structure valid (12 cases)
OK: public boundary file scan passed
OK: all public structure checks passed
```

During final hygiene verification, local IDE metadata appeared under the gitignored
`.idea/` directory. `check_public_boundary.py` was aligned with `.gitignore` so that
known editor and Python-cache directories are excluded from the repository artifact
scan. The final standard structure check passes, and the ignored `.idea/` files were
not used as verification input or included in the repository commit.

## Successful canon output framing

Every successful command below exited 0, emitted empty stderr, and emitted stdout
in this exact form:

```text
CANON:
<canonical ASCII shown in the table>

HASH:
<hash shown in the table>
```

The emitted hash is recorded as optional, version-bound compatibility identity.
It is not proof, truth, consensus, or certification.

## Accepted cases

| Case | Exact command | Canonical ASCII | Emitted hash | Limitation |
|---|---|---|---|---|
| `accept.basic_bind_001` | `tobi.exe canon corpus/accept/basic_bind_001.tsubasa` | `bind(ID(x), DEC(1), ID(x))` | `8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06` | v0.7.0 / Windows x64 only |
| `accept.basic_bind_002` | `tobi.exe canon corpus/accept/basic_bind_002.tsubasa` | `bind(ID(y), DEC(2), ID(y))` | `37205233a0fffc2592fa3cc385356b10d13e73af3332dd75be01a294e71b9c79` | v0.7.0 / Windows x64 only |
| `accept.atomic_sequence_001` | `tobi.exe canon corpus/accept/atomic_sequence_001.tsubasa` | `seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])` | `756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96` | v0.7.0 / Windows x64 only |

## Rejected cases

### `reject.invented_syntax_001`

- Command: `tobi.exe canon corpus/reject/invented_syntax_001.tsubasa`
- Exit code: 1
- stdout: empty
- stderr (exact):

```text
Error: E023: expected identifier after 'let' (span 3..4)
```

- Limitation: diagnostic text and span are release/platform-bound.

### `reject.malformed_decimal_001`

- Command: `tobi.exe canon corpus/reject/malformed_decimal_001.tsubasa`
- Exit code: 1
- stdout: empty
- stderr (exact):

```text
Error: E013: invalid number literal (span 8..11)
```

- Limitation: diagnostic text and span are release/platform-bound.

## Equivalence cases

All commands exited 0 with empty stderr and the successful stdout framing above.

| Case | Exact command | Canonical ASCII | Emitted hash | Limitation |
|---|---|---|---|---|
| `equivalence.decimal_convergence.decimal_1` | `tobi.exe canon corpus/equivalence/decimal_convergence/decimal_1.tsubasa` | `bind(ID(x), DEC(1), ID(x))` | `8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06` | Family equality observed only in this context |
| `equivalence.decimal_convergence.decimal_1_0` | `tobi.exe canon corpus/equivalence/decimal_convergence/decimal_1_0.tsubasa` | `bind(ID(x), DEC(1), ID(x))` | `8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06` | Family equality observed only in this context |
| `equivalence.decimal_convergence.decimal_01_000` | `tobi.exe canon corpus/equivalence/decimal_convergence/decimal_01_000.tsubasa` | `bind(ID(x), DEC(1), ID(x))` | `8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06` | Family equality observed only in this context |
| `equivalence.sequence_skin_convergence.semicolon` | `tobi.exe canon corpus/equivalence/sequence_skin_convergence/semicolon.tsubasa` | `seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])` | `756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96` | Family equality observed only in this context |
| `equivalence.sequence_skin_convergence.triangle` | `tobi.exe canon corpus/equivalence/sequence_skin_convergence/triangle.tsubasa` | `seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])` | `756a7889a958b394c1f73e99c7886b5c3ccf39ffe4c3892cd580d68d01cefa96` | Family equality observed only in this context |

The three decimal variants were byte-identical in stdout. The two sequencing-skin
variants were also byte-identical in stdout.

## Determinism case

Case: `determinism.basic_bind_001`

- Command repeated three times: `tobi.exe canon corpus/determinism/basic_bind_001/source.tsubasa`
- Exit code for all runs: 0
- stderr for all runs: empty
- Canonical ASCII for all runs: `bind(ID(x), DEC(1), ID(x))`
- Hash for all runs: `8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06`
- Result: exit code, stdout, and stderr were byte-identical across all three runs.
- Limitation: same binary, platform, command, and source only.

## Idempotence case: pending

Case: `idempotence.basic_bind_001` remains `PENDING_REAL_TOBI_RUN`.

First command:

```text
tobi.exe canon corpus/idempotence/basic_bind_001/source.tsubasa
```

First result: exit 0, empty stderr, canonical ASCII
`bind(ID(x), DEC(1), ID(x))`, hash
`8529c28715d07069fe135dde07ed73db49fa690d5f7b1874dea47760f3321f06`.

For a direct `f(f(x))` check, the observed canonical ASCII was written to a
transient UTF-8 `.tsubasa` file outside the repository and passed to the same
`tobi.exe canon` command. The transient file was deleted immediately.

Second result: exit 0, empty stderr, canonical ASCII
`CALL(ID(bind), [CALL(ID(ID), [ID(x)]), CALL(ID(DEC), [DEC(1)]), CALL(ID(ID), [ID(x)])])`,
hash `95e695c394519984dc8347ae6176d1f67585126aa08ae116b4c9194800d17710`.

The two results differ. The CLI's canonical ASCII is accepted as ordinary surface
call syntax on re-input, so direct canonical-output idempotence is not established.
No verified idempotence expectation is proposed for v0.1.

## Manifest patch proposal

`docs/verification/MANIFEST_PATCH_PROPOSAL_v0.1.json` proposes promotion of 11
real-run verified cases. `idempotence.basic_bind_001` remains pending. The proposal
does not modify the authoritative manifest; AI Verification PM retains approval and
application ownership.

## Boundary confirmation

- Only the public `.tsubasa` sources in this repository were used as input.
- No private fixtures, private golden corpus, `.tobi-sync`, or private scratch data
  was used as source material.
- No validator source or private implementation detail is included.
- No future-product internal is disclosed.
- Validator acceptance is not universal truth or consensus.
- The emitted hash is optional compatibility identity only.

## Final verdict

`PASSED_WITH_LIMITATIONS`

Eleven cases have real-run expected-output evidence suitable for manifest promotion.
The idempotence case remains pending because direct canonical-output re-input was not
idempotent under this release and command context. Verification is Windows x86_64 and
v0.7.0 package-bound; the executable has no self-reporting `--version` option.
