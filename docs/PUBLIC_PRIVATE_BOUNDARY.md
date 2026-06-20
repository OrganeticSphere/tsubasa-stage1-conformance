# Public / Private Boundary

## Public in this repository

- `.tsubasa` source examples;
- manifest metadata;
- structure-only helper tools;
- documentation for public conformance use;
- expected outputs only after real Tobi Validator runs.

## Private and not included

- validator source;
- compiler source;
- private fixtures;
- private golden corpus;
- binaries or archives;
- private release/distribution logic;
- future product internals;
- customer artifacts.

## Important interpretation boundaries

Validator acceptance means:

```text
this artifact was accepted by the stated Tobi release under the stated command context
```

It does not mean:

```text
this artifact is universally true
```

A hash value, if included, is only a compatibility identity for the stated version/context.

Conformance examples are not certification marks.
