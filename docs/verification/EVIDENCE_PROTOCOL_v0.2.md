# Tsubasa Conformance Corpus — Evidence Protocol v0.2

**Status:** DRAFT EVIDENCE PROTOCOL — no release/tag authorization  
**Scope:** Linux x86_64 evidence expansion for the existing v0.1 public case set  
**Public display name:** Tsubasa Conformance Corpus  
**Validator product:** Tobi Validator  
**Pinned validator release identity:** `stage1-tobi-validator-v0.7.0`

## 1. Purpose

This protocol defines a bounded v0.2 evidence-expansion pass for the existing public Tsubasa Conformance Corpus.

The immediate goal is deliberately narrow:

- rerun the existing 12 public `.tsubasa` cases on Linux x86_64;
- record exact real-run evidence from the pinned released Tobi Validator contour;
- compare Linux observations with the existing Windows x86_64 v0.1 evidence;
- preserve any divergence as evidence rather than rewriting it away;
- keep the existing public/private and claim boundaries unchanged.

This protocol does **not** add new Tsubasa semantics, new public syntax families, a new validator mode, a public verification API, certification, truth claims, or Stage 2 surface.

## 2. Fixed case baseline

Phase A uses the existing case set from:

```text
corpus/manifest.v0.1.json
```

The v0.1 manifest remains historical evidence and must not be rewritten merely to attach Linux observations.

Current fixed case count:

```text
12 total
11 VERIFIED_WITH_TOBI
1 PENDING_REAL_TOBI_RUN
```

The pending case is:

```text
idempotence.basic_bind_001
```

Its pending state must not be promoted simply because another platform run is performed.

## 3. Validator provenance requirement

Every Linux evidence record must identify the exact validator executable used.

Required fields:

- release/package identity: `stage1-tobi-validator-v0.7.0`;
- platform/architecture;
- executable filename/path used for the run;
- executable SHA-256;
- source/provenance of the executable or package;
- exact command;
- exit code;
- exact stdout;
- exact stderr.

The executable must come from an authorized released distribution contour. A local build, reimplementation, inferred output, copied documentation value, Playground response, or manually reconstructed output is not acceptable as primary corpus evidence.

If the binary provenance cannot be established, stop the evidence run and report the limitation. Do not manufacture expected output.

## 4. Phase A — Linux x86_64 rerun

Run every existing corpus case using the released validator command form:

```text
tobi canon <relative .tsubasa path>
```

For each case, record the real command and exact process result.

### 4.1 Existing verified accept/equivalence cases

For successful cases record:

- exit code;
- exact stdout;
- exact stderr;
- canonical ASCII parsed from the real output;
- emitted `_h` value as a compatibility identity only.

Compare the Linux observation with the v0.1 Windows evidence.

Classification:

```text
MATCH
DIVERGENCE_OBSERVED
```

A divergence is evidence. It must not be silently normalized or classified as an error without a separate technical explanation.

### 4.2 Existing reject cases

For rejected cases record:

- exit code;
- exact stdout;
- exact stderr;
- diagnostic code;
- diagnostic message;
- diagnostic span when present.

Compare against the Windows evidence, but remember that diagnostic rendering is recorded as release/platform-bound evidence. Any difference must be preserved exactly.

### 4.3 Determinism case

For:

```text
determinism.basic_bind_001
```

run the same command at least three times in the same Linux execution context.

Record whether exit code, stdout and stderr are byte-identical across all repetitions.

This proves only same-binary / same-platform / same-command / same-source repeatability for the observed run set. It does not prove universal cross-platform determinism.

### 4.4 Idempotence observation

For:

```text
idempotence.basic_bind_001
```

preserve the existing v0.1 limitation model.

Procedure:

1. run the authored `.tsubasa` source through `tobi canon`;
2. capture the real canonical ASCII from the successful first result;
3. write that canonical ASCII to a transient UTF-8 `.tsubasa` file outside the repository;
4. run the same pinned validator against that transient file;
5. record both exact results;
6. delete the transient file immediately after the observation.

Do not assume that canonical ASCII is itself an idempotent authoring surface.

Classification should be evidence-oriented, for example:

```text
IDEMPOTENT_REINPUT_OBSERVED
NON_IDEMPOTENT_REINPUT_OBSERVED
NOT_RUN
```

Do not convert the existing manifest case to `VERIFIED_WITH_TOBI` merely because the two-step observation was executed.

## 5. Evidence outputs

After real Linux execution, create or update only evidence-oriented artifacts appropriate to the observed results.

Expected primary report:

```text
docs/verification/TOBI_RUNS_v0.2.md
```

Expected machine-readable matrix:

```text
docs/verification/EVIDENCE_MATRIX_v0.2.json
```

The matrix should reference the v0.1 case baseline and record platform observations without rewriting the historical v0.1 manifest.

Minimum matrix shape:

```json
{
  "evidence_version": "0.2",
  "case_manifest": "corpus/manifest.v0.1.json",
  "validator_release": "stage1-tobi-validator-v0.7.0",
  "platform_runs": [
    {
      "platform": "linux-x86_64",
      "executable_sha256": "<real hash>",
      "cases": []
    }
  ]
}
```

Each case record must be derived from real execution evidence, not inferred expected behavior.

## 6. Comparison boundary

The v0.2 Linux pass asks:

> Does the same released validator contour produce the same observable conformance results for the existing public case set on Linux x86_64 as the recorded Windows x86_64 evidence?

The pass does **not** ask whether the artifacts are factually true.

Required interpretation boundaries:

```text
canonical equality != factual truth
validator acceptance != universal correctness
_h != proof
_h != signature
_h != consensus
conformance != certification
```

`_h` remains a compatibility identity only.

## 7. Security and public/private boundary

Do not commit:

- validator executables;
- release archives;
- private fixtures;
- private golden corpus material;
- credentials or tokens;
- private distribution URLs or secret-bearing logs;
- transient idempotence files.

Only public corpus sources and public-safe evidence derived from authorized real validator runs may enter this repository.

## 8. No coverage widening in Phase A

Phase A intentionally does **not** add new language constructs.

Do not add calls, strings, `match`, `note`, logical builtins, comparison builtins, or other syntax families merely because the implementation may support them internally.

The current public authoring reference explicitly favors narrow accepted examples, convergence families and malformed siblings over speculative breadth.

Additional public-safe constructs require a separate language-owner/public-safety review and a separate coverage-expansion change after the Linux evidence baseline is stable.

## 9. macOS follow-up

macOS evidence is a subsequent platform-evidence phase.

It must use an exact released macOS validator artifact with independently recorded executable identity and must follow the same real-run discipline.

Do not claim macOS conformance or three-platform determinism until that run actually exists.

## 10. Release boundary

This protocol does not authorize a new GitHub release or tag.

Do not create or move:

```text
v0.2.0
v0.1.0
```

Release/version publication remains a separate Aset-authorized decision after exact-head review of the completed evidence set.

## 11. Completion condition for Phase A

Phase A is ready for review only when:

```text
EXACT RELEASE BINARY PROVENANCE RECORDED
+ ALL 12 EXISTING CASES EXECUTED OR EXPLICITLY BLOCKED
+ 11 VERIFIED CASES HAVE EXACT LINUX OBSERVATIONS
+ DETERMINISM CASE REPEATED >= 3 TIMES
+ IDEMPOTENCE TWO-STEP OBSERVATION RECORDED
+ WINDOWS/LINUX COMPARISON MATRIX WRITTEN
+ NO PRIVATE/BINARY MATERIAL COMMITTED
+ STRUCTURE/PUBLIC-BOUNDARY CHECKS PASS
+ GIT DIFF CHECK PASSES
```

Any mismatch remains visible as evidence and must be reviewed before a v0.2 release decision.