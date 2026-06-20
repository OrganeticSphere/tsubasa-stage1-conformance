# Versioning and Compatibility

## Repository versioning

This repository uses public conformance corpus versions:

```text
v0.1.0
```

## Manifest versioning

The v0.1 manifest file is:

```text
corpus/manifest.v0.1.json
```

## Expected-output versioning

Every verified expected output must state:

- Tobi release;
- platform;
- command;
- observed exit code;
- observed output.

## Compatibility principle

A case can be conformance-relevant without claiming universal permanence.

Version-bound expected output means:

```text
this was observed under this validator release and this command context
```

It does not mean:

```text
this value is proof of truth across all future versions
```
