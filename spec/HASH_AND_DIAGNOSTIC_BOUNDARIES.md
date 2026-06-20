# Hash and Diagnostic Boundaries

## `_h` boundary

`_h` is a compatibility identity only.

It is not:

- proof of real-world truth;
- consensus;
- a certification mark;
- a universal semantic guarantee;
- a substitute for review.

For v0.1, `_h` is optional and version-bound.

## Diagnostic boundary

Diagnostic expectations must come from real Tobi Validator runs.

A diagnostic expectation should record:

- command;
- exit code;
- diagnostic code, if emitted;
- diagnostic message or stable excerpt, if emitted;
- platform;
- Tobi release;
- limitations.

Do not invent diagnostic codes or messages.

## Version boundary

A diagnostic or `_h` value is valid only for the stated Tobi release and verification context.
