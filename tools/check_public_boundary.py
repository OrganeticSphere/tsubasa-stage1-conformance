#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_SUFFIXES = {
    '.zip', '.tar', '.tgz', '.gz', '.exe', '.dll', '.so', '.dylib', '.bin', '.wasm'
}
TEXT_SUFFIXES = {'.md', '.txt', '.json', '.py', '.yml', '.yaml', '.tsubasa', '.template', ''}
IGNORED_LOCAL_DIRS = {'.git', '.idea', '.vscode', '__pycache__', '.pytest_cache', '.venv'}


def fail(msg: str) -> None:
    print(f'ERROR: {msg}', file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        parts = set(rel.parts)
        if parts & IGNORED_LOCAL_DIRS:
            continue
        if path.is_dir():
            continue
        if path.suffix in FORBIDDEN_SUFFIXES:
            fail(f'binary/archive artifact is not allowed: {rel}')
        if path.suffix not in TEXT_SUFFIXES:
            fail(f'unexpected file suffix {path.suffix!r}: {rel}')
        if path.name.endswith('.tsubasa'):
            continue
    print('OK: public boundary file scan passed')


if __name__ == '__main__':
    main()
