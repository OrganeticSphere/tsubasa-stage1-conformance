# Coverage Limitations

v0.1 is a verified seed corpus, not full Tsubasa language coverage.

## Covered in v0.1

- basic `let` binding;
- decimal canonical convergence;
- an `atomic` sequence;
- sequencing skins `;` and `▷`;
- two reject examples;
- single-platform determinism for one case.

## Pending or not covered

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

## Requirements for future expansion

Future coverage expansion requires:

- AI Verification PM ownership;
- Tobi Compiler / Architect public-safety classification;
- real Tobi runs;
- no private fixtures;
- no private golden corpus;
- no Stage 2 internals.
