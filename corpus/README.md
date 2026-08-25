# Tsubasa Conformance Corpus — corpus directory

This directory contains public-safe `.tsubasa` examples for the **Tsubasa Conformance Corpus**.

The repository slug and some technical/historical identifiers retain `stage1` wording for compatibility and link stability. `Stage 1` is not the current customer-facing product name.

## Classes

- `accept/` — source examples expected to be accepted after verification.
- `reject/` — source examples expected to be rejected after verification.
- `equivalence/` — source variants expected to converge after verification.
- `idempotence/` — repeated-run stability examples.
- `determinism/` — same-version same-command stability examples.

## Expected outputs

Expected outputs are not stored next to source files. They are recorded in:

```text
manifest.v0.1.json
```

Cases without real Tobi Validator evidence must keep their expected outputs pending.

## Current v0.1 verification status

The current manifest contains 12 cases:

- 11 cases marked `VERIFIED_WITH_TOBI` from real Tobi Validator `stage1-tobi-validator-v0.7.0` runs on Windows x86_64;
- 1 case, `idempotence.basic_bind_001`, remains `PENDING_REAL_TOBI_RUN` because direct canonical-output re-input did not preserve the same canonical form or compatibility identity under the verified release and command context.

The idempotence category is intentionally reserved in v0.1. Direct re-input of canonical ASCII produced a different canonical form and compatibility identity under the verified v0.7.0 context, so the result is preserved as a limitation rather than recorded as a pass. v0.1 does not claim verified idempotence coverage.

`_h` is compatibility identity only. Canonical equality does not establish factual truth, and validator acceptance is not universal correctness.

See `../docs/verification/TOBI_RUNS_v0.1.md`.
