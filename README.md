# Tsubasa Stage 1 Conformance Corpus

**Status:** v0.1 public seed corpus / release candidate
**Maintainer:** OrganeticSphere
**Product line:** Stage 1 Tobi Validator
**Scope:** public-safe Stage 1 conformance examples for `.tsubasa` artifacts

This repository is a public conformance and authoring corridor for the released Stage 1 Tobi Validator product line.

It is intended to make Stage 1 validator behavior more inspectable without publishing the private validator implementation.

## What this repository contains

* public-safe `.tsubasa` examples;
* source-only accept / reject / equivalence / idempotence / determinism case structure;
* a manifest format for expected results;
* structure checks for the public corpus;
* documentation explaining public/private boundaries;
* real-run expected-output evidence for 11 cases;
* 1 idempotence case intentionally left pending.

See [`docs/COVERAGE_LIMITATIONS.md`](docs/COVERAGE_LIMITATIONS.md) for the verified v0.1 coverage boundary.

## Current v0.1 status

The current v0.1 corpus contains:

* 12 public Stage 1 cases;
* 11 cases marked `VERIFIED_WITH_TOBI`;
* 1 case, `idempotence.basic_bind_001`, marked `PENDING_REAL_TOBI_RUN`;
* verification evidence from real Tobi Validator `stage1-tobi-validator-v0.7.0` runs;
* Windows x86_64 verification evidence for the current recorded run set.

This is a verified seed corpus. It is not full Tsubasa language coverage.

Linux/macOS cross-platform determinism is not claimed in v0.1.

## What this repository does not contain

This repository does not contain:

* Tobi compiler or validator source code;
* validator binaries;
* private fixtures;
* private golden corpus;
* private release or distribution logic;
* private engine/core implementation details;
* future product internals;
* a reimplementation of Tobi behavior;
* a certification program;
* a public proof/truth/consensus layer.

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

## Required expected-output discipline

No canonical output, diagnostic expectation, exit code, or hash value may be treated as final unless it comes from a real Tobi Validator run.

Unverified cases must remain marked as:

```json
"expected_status": "PENDING_REAL_TOBI_RUN"
```

A case may be changed to:

```json
"expected_status": "VERIFIED_WITH_TOBI"
```

only when the verification record includes:

* exact Tobi release or package identity;
* platform;
* command;
* exit code;
* stdout;
* stderr;
* observed canonical output, diagnostic output, or optional hash output.

Do not fill expected outputs from memory, prose documentation, or inferred behavior.

## Idempotence limitation

The idempotence category is intentionally reserved in v0.1.

The current idempotence case remains `PENDING_REAL_TOBI_RUN` because direct re-input of canonical ASCII produced a different canonical form and hash under the verified v0.7.0 context.

This is preserved as a limitation, not hidden as a pass.

v0.1 does not claim verified idempotence coverage.

## Hash boundary

`_h`, when present, is a compatibility identity only.

It is not:

* a proof of truth;
* a proof of real-world correctness;
* consensus;
* certification;
* semantic authority.

For v0.1, `_h` is optional and version-bound.

## Coverage boundary

v0.1 covers a narrow public-safe Stage 1 seed set:

* basic `let` binding;
* decimal canonical convergence;
* an `atomic` sequence;
* sequencing skins `;` and `▷`;
* two reject examples;
* single-platform determinism for one case.

v0.1 does not yet cover:

* verified idempotence;
* calls;
* strings;
* `match`;
* `note`;
* logical builtins;
* comparison builtins;
* broader diagnostic families;
* Linux/macOS cross-platform determinism;
* full formal grammar.

Future coverage expansion requires public-safety classification, real Tobi runs, and preservation of the public/private boundary.

## How to use this corpus

1. Review the public examples under [`corpus/`](corpus/).

2. Inspect the manifest:

   ```text
   corpus/manifest.v0.1.json
   ```

3. Review the verification evidence:

   ```text
   docs/verification/TOBI_RUNS_v0.1.md
   ```

4. Run public structure checks:

   ```bash
   python tools/run_structure_checks.py
   ```

5. Use an authorized Tobi Validator distribution to reproduce or extend verification runs.

6. Update `corpus/manifest.v0.1.json` only from real command output.

See [`docs/HOW_TO_USE_WITH_TOBI_VALIDATOR.md`](docs/HOW_TO_USE_WITH_TOBI_VALIDATOR.md).

## Relationship to Tobi Validator

Tobi Validator is the Stage 1 validator product line.

This repository is not the validator implementation. It is the public conformance corpus and documentation corridor for Stage 1 `.tsubasa` artifacts.

Authorized users may run Tobi Validator against the public examples and compare results with the recorded expected-output evidence.

The private validator implementation, private binary distribution, private fixtures, and private golden corpus remain outside this repository.

## Relationship to the public GitHub Action

The public Tobi Validator GitHub Action / wrapper repository provides adoption and CI usage material.

This repository provides open conformance examples and verification evidence.

Together, they support the public Stage 1 trust surface:

```text
public .tsubasa examples
→ authorized Tobi Validator execution
→ canonical output / diagnostics / optional _h
→ public expected-output evidence
```

Execution still requires authorized Tobi Validator access.

## Public/private boundary

The public boundary is intentional.

Public:

* `.tsubasa` examples;
* manifest structure;
* verified expected-output records;
* coverage limitations;
* public/private boundary documentation;
* structure checks.

Private:

* Tobi compiler source;
* validator engine/core implementation;
* private fixtures;
* private golden corpus;
* private release and distribution logic;
* private future-product internals.

See [`docs/PUBLIC_PRIVATE_BOUNDARY.md`](docs/PUBLIC_PRIVATE_BOUNDARY.md).

## Versioning and compatibility

The current corpus is v0.1.

Expected outputs are version-bound. A future Tobi Validator release may require a new verification pass and a new manifest update.

A verified expectation should always identify the validator release or package identity used to produce it.

See [`spec/VERSIONING_AND_COMPATIBILITY.md`](spec/VERSIONING_AND_COMPATIBILITY.md).

## Trademarks and naming

Use of the Organetic, Tobi, and Tsubasa names is subject to the naming guard in [`TRADEMARKS.md`](TRADEMARKS.md).

This corpus is public evidence and examples. It is not a certification program.

Do not claim:

* “Organetic-certified”;
* “Tobi-certified”;
* “Tsubasa-certified”;
* “official Tsubasa implementation”;
* “official Tobi-compatible implementation”;

without written permission.

## License

Repository contents are licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

This license does not license:

* private Tobi binaries;
* private distribution artifacts;
* private compiler source;
* private validator source;
* private engine/core implementation.

## Governance

This repository is maintained as part of the Stage 1 Tobi Validator product line by OrganeticSphere.

Operational ownership remains with the AI Verification PM function. Technical verification of canonical outputs, diagnostics, and optional `_h` values may be performed by the Tobi Compiler / Architect role using real Tobi Validator runs.

These roles are internal Organetic project functions. They do not imply external certification, third-party audit, or public ownership of the private validator implementation.

## Contributing

Contributions must preserve the public/private boundary.

In particular:

* use `.tsubasa` for new source examples;
* do not add `.tbs` examples;
* do not add validator binaries;
* do not add private fixtures;
* do not add private golden corpus material;
* do not add future-product internals;
* do not invent expected canonical outputs, diagnostics, exit codes, or `_h` values;
* do not claim full language coverage.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Do not report private tokens, private binaries, private distribution paths, or private validator internals in public issues.

See [`SECURITY.md`](SECURITY.md).
