# Manifest Schema Note

This is a lightweight schema note, not a formal JSON Schema.

## Required fields per case

- `case_id`
- `class`
- `source_path`
- `expected_status`
- `expected`

## Allowed classes

- `accept`
- `reject`
- `equivalence`
- `idempotence`
- `determinism`

## Allowed expected statuses

- `PENDING_REAL_TOBI_RUN`
- `VERIFIED_WITH_TOBI`

## Pending rule

When `expected_status` is `PENDING_REAL_TOBI_RUN`, `expected` must be `null`.

## Verified rule

When `expected_status` is `VERIFIED_WITH_TOBI`, the case must include `verified_with` and non-null `expected`.

## Hash rule

If `expected.h` is present, it must include:

```json
{
  "required": false,
  "meaning": "compatibility_identity_only",
  "value": "... or null"
}
```
