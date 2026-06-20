# Corpus

This directory contains public-safe `.tsubasa` examples for the Stage 1 conformance corridor.

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

- 11 cases marked `VERIFIED_WITH_TOBI` from real Tobi Validator `v0.7.0` runs on Windows x86_64;
- 1 case, `idempotence.basic_bind_001`, remains `PENDING_REAL_TOBI_RUN` because direct canonical-output re-input did not preserve the same canonical form/hash under the verified release and command context.

See `../docs/verification/TOBI_RUNS_v0.1.md`.
