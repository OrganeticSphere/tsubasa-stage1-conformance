# Release Notes v0.1 Draft

Status: release-candidate scaffold, not yet tagged.

## Included

- Public Stage 1 `.tsubasa` conformance corpus structure.
- Public/private boundary documentation.
- Manifest-driven accept/reject/equivalence/idempotence/determinism cases.
- Structure-only public checks.
- Technical verification report for real Tobi Validator `v0.7.0` runs.
- Apache License, Version 2.0, for repository contents.

## Verification status

- 12 public `.tsubasa` cases exist in `corpus/manifest.v0.1.json`.
- 11 cases are marked `VERIFIED_WITH_TOBI`.
- `idempotence.basic_bind_001` remains `PENDING_REAL_TOBI_RUN`.

The idempotence category is intentionally reserved in v0.1. The current
idempotence case remains `PENDING_REAL_TOBI_RUN` because direct re-input of
canonical ASCII produced a different canonical form and hash under the verified
v0.7.0 context. This is preserved as a limitation, not hidden as a pass. v0.1
does not claim verified idempotence coverage.

## Boundary

This repository does not contain Tobi validator source, validator binaries, private fixtures, private golden corpus, `.tobi-sync`, or Stage 2 internals.

`_h` values, where present, are optional version-bound compatibility identities only. They are not proof, truth, consensus, or certification.

## Release readiness checklist

- [x] Structure checks pass.
- [x] The manifest has 12 cases.
- [x] 11 cases are verified with real Tobi
  `stage1-tobi-validator-v0.7.0`.
- [x] 1 idempotence case remains pending.
- [x] No private fixtures are included.
- [x] No private golden corpus is included.
- [x] No `.tbs` files are included.
- [x] No `.tobi-sync` files are included.
- [x] No validator binary is included.
- [x] No private distribution logic is included.
- [x] No Stage 2 internals are included.
- [x] `_h` remains optional compatibility identity only.
- [x] Coverage limitations are documented.
- [x] The trademark and naming guard is included.
- [x] The structure workflow supports pushes to both `main` and `master`.
