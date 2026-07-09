# PR Sequence for v0.1

Status: completed for the v0.1 release-candidate flow. The `v0.1.0` tag
was created before the README governance wording cleanup now present on
`master`. Do not move `v0.1.0`; use `v0.1.1` for the release-state
cleanup.

## PR 0 — Repository bootstrap

Create governance, README, security policy, Apache-2.0 license, and empty structure.

## PR 1 — Public/private boundary docs

Add public/private boundary, FAQ, and non-goals.

## PR 2 — Stage 1 public spec scaffold

Add public-safe Stage 1 spec documents. Do not claim full grammar completeness.

## PR 3 — Corpus structure and manifest skeleton

Add corpus directories, manifest, manifest schema note, and structure-only helper tools.

## PR 4 — Source-only public examples

Add public-safe `.tsubasa` examples with all expected outputs marked `PENDING_REAL_TOBI_RUN`.

## PR 5 — Tobi technical verification

Tobi Compiler / Architect verifies examples with real Tobi runs and records exact command evidence.

## PR 6 — Fill verified expected outputs

AI Verification PM updates the manifest from the technical verification report.

## PR 7 — Equivalence / idempotence / determinism suites

Stabilize v0.1 suite classes after verified output evidence exists.

## PR 8 — Handshake with public Tobi Validator docs

Completed: cross-link this repository with the public Tobi Validator wrapper/docs and evaluation access flow.

## PR 9 — v0.1 release candidate

Completed: final audit, release notes, license confirmation, and tag `v0.1.0`.
