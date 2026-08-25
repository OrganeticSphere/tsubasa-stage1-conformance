# Tsubasa Conformance Corpus

**Status:** v0.1.0 public seed corpus — published  
**Maintainer:** OrganeticSphere  
**Public display name:** Tsubasa Conformance Corpus  
**Repository slug:** `tsubasa-stage1-conformance` — retained for link stability  
**Scope:** public-safe `.tsubasa` examples and version-bound conformance evidence for Tobi Validator

This repository is the public Tsubasa conformance and evidence corridor for reasoning artifacts validated by **Tobi Validator**.

It is intended to make observable validator behavior more inspectable without publishing the private validator implementation.

Tobi Validator is Organetic's **Reasoning Artifact Validator**. It deterministically validates and canonicalizes Tsubasa reasoning artifacts for use at workflow boundaries.

## Public naming note

`Stage 1` is no longer the customer-facing product name. Current public copy uses **Tobi Validator** and **Tsubasa Conformance Corpus**.

Historical release names, the repository slug, technical release identifiers, manifest coordinates, and recorded verification evidence may retain `Stage 1` / `stage1` wording for compatibility and historical accuracy.

## What this repository contains

- public-safe `.tsubasa` examples;
- source-only accept / reject / equivalence / idempotence / determinism case structure;
- a manifest format for expected results;
- structure checks for the public corpus;
- documentation explaining public/private boundaries;
- real-run expected-output evidence for 11 cases;
- 1 idempotence case intentionally left pending.

See [`docs/COVERAGE_LIMITATIONS.md`](docs/COVERAGE_LIMITATIONS.md) for the verified v0.1 coverage boundary.

## Current v0.1 status

The current v0.1 corpus contains:

- 12 public Tsubasa cases;
- 11 cases marked `VERIFIED_WITH_TOBI`;
- 1 case, `idempotence.basic_bind_001`, marked `PENDING_REAL_TOBI_RUN`;
- verification evidence from real Tobi Validator `stage1-tobi-validator-v0.7.0` runs;
- Windows x86_64 verification evidence for the current recorded run set.

This is a verified seed corpus. It is not full Tsubasa language coverage.

Linux/macOS cross-platform determinism is not claimed in v0.1.

## Release state

Release `v0.1.0` is published. Its historical release title and tag are retained as issued.

Current `master` includes post-release documentation/governance cleanup. The existing `v0.1.0` tag must not be moved to absorb later editorial changes; any future patch release requires a separate release decision.

## What this repository does not contain

This repository does not contain:

- Tobi compiler or validator source code;
- validator binaries;
- private fixtures;
- private golden corpus;
- private release or distribution logic;
- private engine/core implementation details;
- future product internals;
- a reimplementation of Tobi behavior;
- a certification program;
- a public proof/truth/consensus layer.

The public corpus makes behavior inspectable. It does not make the private validator engine public.

## Repository layout

```text
spec/
  TSUBASA_STAGE1_PUBLIC_SPEC.md
  ARTIFACT_FORMAT.md
  SURFACE_TO_CANONICAL_TABLE.md
  HASH_AND_DIAGNOSTIC_BOUNDARIES.md
  VERSIONING_AND_COMPATIBILITY.md
  NON_GOALS.md

corpus/
  README.md
  manifest.v0.1.json
  schema/MANIFEST_SCHEMA_NOTE.md
  accept/
  reject/
  equivalence/
  idempotence/
  determinism/

docs/
  PUBLIC_PRIVATE_BOUNDARY.md
  HOW_TO_USE_WITH_TOBI_VALIDATOR.md
  COVERAGE_LIMITATIONS.md
  FAQ.md
  verification/

tools/
  run_structure_checks.py
```

The physical filename `spec/TSUBASA_STAGE1_PUBLIC_SPEC.md` remains unchanged for link stability. Its current visible title should follow Tsubasa-owned public naming rather than treating `Stage 1` as the product name.

## Required expected-output discipline

No canonical output, diagnostic expectation, exit code, or compatibility identity may be treated as final unless it comes from a real Tobi Validator run.

Unverified cases must remain marked as:

```json
"expected_status": "PENDING_REAL_TOBI_RUN"
```

A case may be changed to:

```json
"expected_status": "VERIFIED_WITH_TOBI"
```

only when the verification record includes:

- exact Tobi release or package identity;
- platform;
- command;
- exit code;
- stdout;
- stderr;
- observed canonical output, diagnostic output, or optional compatibility identity.

Do not fill expected outputs from memory, prose documentation, or inferred behavior.

## Idempotence limitation

The idempotence category is intentionally reserved in v0.1.

The current idempotence case remains `PENDING_REAL_TOBI_RUN` because direct re-input of canonical ASCII produced a different canonical form and compatibility identity under the verified v0.7.0 context.

This is preserved as a limitation, not hidden as a pass.

v0.1 does not claim verified idempotence coverage.

## Compatibility identity boundary

`_h`, when present, is a compatibility identity only.

It is not:

- a proof of truth;
- a proof of real-world correctness;
- consensus;
- certification;
- semantic authority.

For v0.1, `_h` is optional and version-bound.

Canonical equality does not establish factual truth. Validator acceptance is not universal correctness.

## Coverage boundary

v0.1 covers a narrow public-safe seed set:

- basic `let` binding;
- decimal canonical convergence;
- an `atomic` sequence;
- sequencing skins `;` and `▷`;
- two reject examples;
- single-platform determinism for one case.

v0.1 does not yet cover:

- verified idempotence;
- calls;
- strings;
- `match`;
- `note`;
- logical builtins;
- comparison builtins;
- broader diagnostic families;
- Linux/macOS cross-platform determinism;
- full formal grammar.

Future coverage expansion requires public-safety classification, real Tobi runs, and preservation of the public/private boundary.

## How to use this corpus

1. Review the public examples under [`corpus/`](corpus/).
2. Inspect the manifest at `corpus/manifest.v0.1.json`.
3. Review the verification evidence at `docs/verification/TOBI_RUNS_v0.1.md`.
4. Run public structure checks:

   ```bash
   python tools/run_structure_checks.py
   ```

5. Use authorized Tobi Validator access to reproduce or extend verification runs.
6. Update `corpus/manifest.v0.1.json` only from real command output.

See [`docs/HOW_TO_USE_WITH_TOBI_VALIDATOR.md`](docs/HOW_TO_USE_WITH_TOBI_VALIDATOR.md).

## Relationship to Tobi Validator

**Tsubasa is the language. Tobi is the validator. Organetic is the verification architecture around them.**

Tobi Validator is Organetic's Reasoning Artifact Validator. This repository is not the validator implementation. It is the public Tsubasa conformance corpus and evidence corridor for the released validator contract.

Authorized users may run Tobi Validator against the public examples and compare results with the recorded expected-output evidence.

The private validator implementation, controlled binary distribution, private fixtures, and private golden corpus remain outside this repository.

## Relationship to the public GitHub Action

The public [`OrganeticSphere/tobi-validator`](https://github.com/OrganeticSphere/tobi-validator) repository provides the Tobi Validator GitHub Action wrapper, adoption documentation, examples, and controlled evaluation-access path.

This repository provides open conformance examples and verification evidence.

Together, the public surfaces support this bounded flow:

```text
public .tsubasa examples
→ authorized Tobi Validator execution
→ canonical output / diagnostics / optional _h compatibility identity
→ public expected-output evidence
```

Execution still requires authorized Tobi Validator access.

Useful public links:

- [Tobi Validator](https://github.com/OrganeticSphere/tobi-validator)
- [Organetic documentation](https://organetic.ai/docs.html)
- [Evaluation access](https://organetic.ai/eval-access.html)
- [GitHub Actions guide](https://organetic.ai/docs-github-actions.html)
- [GitLab CI/CD component guide](https://organetic.ai/docs-gitlab-component.html)

## Public/private boundary

The public boundary is intentional.

Public:

- `.tsubasa` examples;
- manifest structure;
- verified expected-output records;
- coverage limitations;
- public/private boundary documentation;
- structure checks.

Private:

- Tobi compiler source;
- validator engine/core implementation;
- private fixtures;
- private golden corpus;
- private release and distribution logic;
- private future-product internals.

See [`docs/PUBLIC_PRIVATE_BOUNDARY.md`](docs/PUBLIC_PRIVATE_BOUNDARY.md).

## Versioning and compatibility

The current corpus line is v0.1, with published release `v0.1.0`.

Expected outputs are version-bound. A future Tobi Validator release may require a new verification pass and a new manifest update.

A verified expectation should always identify the validator release or package identity used to produce it.

See [`spec/VERSIONING_AND_COMPATIBILITY.md`](spec/VERSIONING_AND_COMPATIBILITY.md).

## Trademarks and naming

Use of the Organetic, Tobi, and Tsubasa names is subject to the naming guard in [`TRADEMARKS.md`](TRADEMARKS.md).

This corpus is public evidence and examples. It is not a certification program.

Do not claim:

- “Organetic-certified”;
- “Tobi-certified”;
- “Tsubasa-certified”;
- “official Tsubasa implementation”;
- “official Tobi-compatible implementation”

without written permission.

## License

Repository contents are licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

This license does not license:

- private Tobi binaries;
- private distribution artifacts;
- private compiler source;
- private validator source;
- private engine/core implementation.

## Governance

OrganeticSphere maintains this public corpus. Technical verification of canonical outputs, diagnostics, and optional `_h` values must be grounded in real Tobi Validator runs and recorded with exact release/platform evidence.

Internal project roles do not imply external certification, third-party audit, or public ownership of the private validator implementation.

## Contributing

Contributions must preserve the public/private boundary.

In particular:

- use `.tsubasa` for new source examples;
- do not add `.tbs` examples;
- do not add validator binaries;
- do not add private fixtures;
- do not add private golden corpus material;
- do not add future-product internals;
- do not invent expected canonical outputs, diagnostics, exit codes, or `_h` values;
- do not claim full language coverage.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Do not report private tokens, private binaries, private distribution paths, or private validator internals in public issues.

See [`SECURITY.md`](SECURITY.md).
