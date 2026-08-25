# Release Notes v0.1

**Current release state:** `v0.1.0` is a published public seed-corpus release.

The tag was created from the original v0.1 release-candidate line. Current `master` contains post-tag documentation and governance cleanup. The historical tag/release title and technical `Stage 1` / `stage1` identifiers remain as issued.

Release hygiene policy: do not move `v0.1.0` to absorb later editorial changes. Any future patch release requires a separate release decision and must not silently rewrite the historical evidence basis.

## Included

- Public `.tsubasa` conformance corpus structure.
- Public/private boundary documentation.
- Manifest-driven accept/reject/equivalence/idempotence/determinism cases.
- Structure-only public checks.
- Technical verification report for real Tobi Validator `stage1-tobi-validator-v0.7.0` runs.
- Apache License, Version 2.0, for repository contents.

The current public display name is **Tsubasa Conformance Corpus**. The repository slug and historical v0.1 release material retain `stage1` wording where required for compatibility and historical accuracy.

## Verification status

- 12 public `.tsubasa` cases exist in `corpus/manifest.v0.1.json`.
- 11 cases are marked `VERIFIED_WITH_TOBI`.
- `idempotence.basic_bind_001` remains `PENDING_REAL_TOBI_RUN`.

The idempotence category is intentionally reserved in v0.1. The current idempotence case remains `PENDING_REAL_TOBI_RUN` because direct re-input of canonical ASCII produced a different canonical form and compatibility identity under the verified v0.7.0 context. This is preserved as a limitation, not hidden as a pass. v0.1 does not claim verified idempotence coverage.

## Boundary

This repository does not contain Tobi validator source, validator binaries, private fixtures, private golden corpus, `.tobi-sync`, or future-product internals.

`_h` values, where present, are optional version-bound compatibility identities only. They are not proof, truth, consensus, or certification.

Canonical equality does not establish factual truth. Validator acceptance is not universal correctness.

## Release checklist state

The published v0.1.0 seed release was prepared with these boundaries:

- [x] Structure checks pass.
- [x] The manifest has 12 cases.
- [x] 11 cases are verified with real Tobi `stage1-tobi-validator-v0.7.0` runs.
- [x] 1 idempotence case remains pending.
- [x] No private fixtures are included.
- [x] No private golden corpus is included.
- [x] No `.tbs` files are included.
- [x] No `.tobi-sync` files are included.
- [x] No validator binary is included.
- [x] No private distribution logic is included.
- [x] No future-product internals are included.
- [x] `_h` remains optional compatibility identity only.
- [x] Coverage limitations are documented.
- [x] The trademark and naming guard is included.
- [x] The structure workflow supports pushes to both `main` and `master`.
