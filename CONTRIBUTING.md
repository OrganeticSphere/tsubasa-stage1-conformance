# Contributing

This repository is initially operated as a controlled public corpus.

## v0.1 contribution posture

- Issues may report unclear examples, broken structure checks, or documentation problems.
- Pull requests may propose small public-safe examples.
- No semantic changes are accepted through this repository.
- No new language feature may be introduced here.
- No expected output may be added without a real Tobi Validator run.

## Required contribution rules

A contribution must not include:

- validator implementation;
- binaries or archives;
- private fixtures;
- customer artifacts;
- future product internals;
- legacy/private source-file extensions;
- invented canonical output;
- invented diagnostics;
- invented hash values.

Every new example must use `.tsubasa`.

Every expected output must be either:

- `PENDING_REAL_TOBI_RUN`, or
- `VERIFIED_WITH_TOBI` with exact command evidence.

By contributing to this repository, you agree that your contributions are
licensed under the Apache License, Version 2.0.
