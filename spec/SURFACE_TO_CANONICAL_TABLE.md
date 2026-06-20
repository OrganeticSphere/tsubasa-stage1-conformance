# Surface to Canonical Table

This table is intentionally conservative. Canonical output cells remain pending until real Tobi Validator runs verify them.

| Case | Surface source | Expected canonical output | Status |
|---|---|---:|---|
| `accept.basic_bind_001` | `let x = 1 in x` | `PENDING_REAL_TOBI_RUN` | pending |
| `accept.basic_bind_002` | `let y = 2 in y` | `PENDING_REAL_TOBI_RUN` | pending |
| `accept.atomic_sequence_001` | `atomic{ let x = 1 in x; let y = 2 in y }` | `PENDING_REAL_TOBI_RUN` | pending |
| `equivalence.decimal_convergence.*` | decimal surface variants | `PENDING_REAL_TOBI_RUN` | pending |
| `equivalence.sequence_skin_convergence.*` | sequencing skin variants | `PENDING_REAL_TOBI_RUN` | pending |

Do not fill this table from memory or documentation. Fill it only after real Tobi runs.
