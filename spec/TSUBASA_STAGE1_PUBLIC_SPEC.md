# Tsubasa Stage 1 Public Spec

**Status:** public-safe v0.1 scaffold
**Scope:** Stage 1 only
**File extension:** `.tsubasa`

This document defines the public-safe Stage 1 authoring and conformance corridor for Tsubasa examples in this repository.

It is not a full long-term grammar. It is not semantic authority. It is not a validator implementation.

## Mental model

Tsubasa Stage 1 artifacts are validator-facing reasoning artifacts.

Tobi Validator is the reference validator that accepts, rejects, canonicalizes, and compares these artifacts.

For public conformance, the practical loop is:

```text
write .tsubasa source
→ run authorized Tobi Validator
→ inspect accept/reject result
→ inspect canonical output or diagnostic
→ compare against version-bound expected output
```

## Public-safe authoring corridor

The v0.1 corpus uses small, explicit examples only:

- local binding examples;
- decimal literal examples;
- small atomic block examples;
- sequencing-skin examples;
- malformed sibling examples for reject coverage.

Do not infer broader language completeness from these examples.

## Canonical pipeline boundary

Public examples may describe the canonical pipeline at a high level:

```text
parse → normalize → canonicalize → canonical ASCII → compatibility identity
```

This repository does not expose internal implementation details of those steps.

## Required expected-output discipline

Expected canonical output, diagnostics, exit codes, and optional `_h` values must be copied only from real Tobi Validator runs.

Pending cases must remain marked as `PENDING_REAL_TOBI_RUN`.

## Non-truth boundary

Validator acceptance is not universal truth.

`_h` is not proof of truth.

Conformance is not consensus.
