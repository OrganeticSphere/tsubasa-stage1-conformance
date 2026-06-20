# How to Use with Tobi Validator

This repository does not include Tobi Validator.

Use an authorized Tobi Validator distribution or public CI wrapper according to the current evaluation access flow.

## Structure checks

Run:

```bash
python tools/run_structure_checks.py
```

These checks validate only repository structure and manifest discipline.

## Real verification

Use Tobi Validator commands against individual `.tsubasa` files.

Example shape:

```bash
tobi canon corpus/accept/basic_bind_001.tsubasa
```

For reject cases, record the real command, exit code, and observed diagnostic output.

## Updating expected outputs

A manifest case may be changed from:

```json
"expected_status": "PENDING_REAL_TOBI_RUN"
```

to:

```json
"expected_status": "VERIFIED_WITH_TOBI"
```

only when exact command evidence is recorded.

## Public wrapper handshake

The public Tobi Validator wrapper repository should link to this corpus as the open conformance/reference example set.

This repository should link users back to the public wrapper and evaluation access flow for controlled execution.
