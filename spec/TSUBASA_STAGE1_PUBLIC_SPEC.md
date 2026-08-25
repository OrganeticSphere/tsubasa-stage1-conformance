# Tsubasa Public Spec — v0.1 Conformance Corridor

**Status:** public-safe v0.1 scaffold  
**Scope:** narrow v0.1 conformance corridor; not the complete Tsubasa language reference  
**File extension:** `.tsubasa`  
**Physical filename:** retained for link stability

This document describes the public-safe v0.1 authoring and conformance corridor for Tsubasa examples in this repository.

It is not a full long-term grammar. It is not semantic authority. It is not a validator implementation.

The filename retains `STAGE1` as a compatibility/historical coordinate. Current public language ownership belongs to **Tsubasa**, while the current public validator product is **Tobi Validator**.

## Mental model

Tsubasa artifacts in this corpus are explicit validator-facing reasoning artifacts.

Tobi Validator is the reference validator that accepts, rejects, and canonicalizes submitted Tsubasa artifacts under the released validator contract.

For public conformance, the practical loop is:

```text
write .tsubasa source
→ run authorized Tobi Validator
→ inspect accept/reject result
→ inspect canonical output or deterministic diagnostic
→ compare against version-bound expected output
```

Authored source is not assumed to be canonical.

## Public-safe authoring corridor

The v0.1 corpus uses small, explicit examples only:

- local binding examples;
- decimal literal examples;
- small atomic block examples;
- sequencing-skin examples;
- malformed sibling examples for reject coverage.

Do not infer broader language completeness from these examples.

## Canonical pipeline boundary

Public examples may describe the validator-facing pipeline at a high level:

```text
authored Tsubasa source
→ validation and Tsubasa canonicalization through Tobi
→ canonical ASCII + optional _h compatibility identity
```

Rejected source produces deterministic diagnostics instead of canonical output.

This repository does not expose internal implementation details of those steps.

## Required expected-output discipline

Expected canonical output, diagnostics, exit codes, and optional `_h` values must be copied only from real Tobi Validator runs.

Pending cases must remain marked as `PENDING_REAL_TOBI_RUN`.

## Interpretation boundary

`_h` is compatibility identity only.

Canonical equality does not establish factual truth.

Validator acceptance is not universal correctness.

Conformance is not consensus or certification.
