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

The idempotence case remains pending because direct re-input of canonical ASCII produced ordinary call-syntax canonicalization rather than the original canonical form/hash under the verified release and command context.

## Boundary

This repository does not contain Tobi validator source, validator binaries, private fixtures, private golden corpus, `.tobi-sync`, or Stage 2 internals.

`_h` values, where present, are optional version-bound compatibility identities only. They are not proof, truth, consensus, or certification.
