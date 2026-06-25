# Surface to Canonical Table

This table contains only values already verified in
`corpus/manifest.v0.1.json` and `docs/verification/TOBI_RUNS_v0.1.md`.

## Accepted surfaces

| Case | Surface source | Verified canonical output |
|---|---|---|
| `accept.basic_bind_001` | `let x = 1 in x` | `bind(ID(x), DEC(1), ID(x))` |
| `accept.basic_bind_002` | `let y = 2 in y` | `bind(ID(y), DEC(2), ID(y))` |
| `accept.atomic_sequence_001` | `atomic{ let x = 1 in x; let y = 2 in y }` | `seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])` |

## Rejected surfaces

| Case | Surface source | Verified diagnostic code |
|---|---|---:|
| `reject.invented_syntax_001` | `let! x := 1 => x` | `E023` |
| `reject.malformed_decimal_001` | `let x = 01..0 in x` | `E013` |

## Decimal convergence

These verified surface forms all converge to
`bind(ID(x), DEC(1), ID(x))`:

- `let x = 1 in x`
- `let x = 1.0 in x`
- `let x = 01.000 in x`

## Sequencing-skin convergence

The verified semicolon and triangle (`▷`) forms both converge to
`seq([bind(ID(x), DEC(1), ID(x)), bind(ID(y), DEC(2), ID(y))])`.

## Boundaries

- Values are version-bound to `stage1-tobi-validator-v0.7.0` and the
  verification report.
- `_h`, if referenced, is optional compatibility identity only.
- This table is not full grammar coverage.
- This table is not semantic authority.
