# How to Use with Tobi Validator

This repository does not include Tobi Validator.

Use the free public Action or download a platform bundle and SHA-256 sidecar
from [Tobi Validator Releases](https://github.com/OrganeticSphere/tobi-validator/releases/tag/stage1-tobi-validator-v0.7.0).
No registration, access token, or repository secret is required.

```yaml
- uses: actions/checkout@v4
- uses: OrganeticSphere/tobi-validator@v2
  with:
    mode: canon
    canon_input: corpus/accept/basic_bind_001.tsubasa
```

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

The public wrapper and public release binaries provide free execution. The
validator implementation remains private.
