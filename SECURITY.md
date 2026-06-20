# Security Policy

This repository is public and must not contain secrets, private distribution tokens, validator binaries, or private source code.

## Reporting

Report suspected leakage of private implementation details, binaries, private fixtures, or unauthorized expected-output data through the private Organetic security channel before opening a public issue.

## Public CI boundary

Public CI in this repository should perform structure checks only. It must not download private validator artifacts or use private distribution tokens on untrusted pull requests.
