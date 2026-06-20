# Artifact Format

## Source files

Every new public source artifact must use:

```text
.tsubasa
```

Source files must be UTF-8 text.

## Case layout

Recommended layout:

```text
corpus/<class>/<case_id>.tsubasa
```

For grouped cases:

```text
corpus/equivalence/<family>/<variant>.tsubasa
corpus/idempotence/<family>/source.tsubasa
corpus/determinism/<family>/source.tsubasa
```

## Expected outputs

Expected outputs live in `corpus/manifest.v0.1.json`.

The source files themselves must not embed expected canonical outputs or diagnostics.

## Pending expected outputs

Before real Tobi verification:

```json
{
  "expected_status": "PENDING_REAL_TOBI_RUN",
  "expected": null
}
```

After real Tobi verification:

```json
{
  "expected_status": "VERIFIED_WITH_TOBI",
  "verified_with": {
    "tobi_release": "...",
    "platform": "...",
    "command": "..."
  },
  "expected": {
    "exit_code": 0,
    "canonical_ascii": "...",
    "diagnostic": null,
    "h": {
      "required": false,
      "meaning": "compatibility_identity_only",
      "value": null
    }
  }
}
```
