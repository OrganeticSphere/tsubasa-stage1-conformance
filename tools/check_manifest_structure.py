#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'corpus' / 'manifest.v0.1.json'
ALLOWED_CLASSES = {'accept', 'reject', 'equivalence', 'idempotence', 'determinism'}
ALLOWED_STATUSES = {'PENDING_REAL_TOBI_RUN', 'VERIFIED_WITH_TOBI'}


def fail(msg: str) -> None:
    print(f'ERROR: {msg}', file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not MANIFEST.exists():
        fail(f'missing manifest: {MANIFEST}')

    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if data.get('stage') != 'stage1':
        fail('manifest stage must be stage1')
    if data.get('source_extension_policy') != '.tsubasa':
        fail('source_extension_policy must be .tsubasa')

    cases = data.get('cases')
    if not isinstance(cases, list) or not cases:
        fail('manifest cases must be a non-empty list')

    seen = set()
    for idx, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(f'case {idx} is not an object')

        case_id = case.get('case_id')
        if not case_id or not isinstance(case_id, str):
            fail(f'case {idx} missing case_id')
        if case_id in seen:
            fail(f'duplicate case_id: {case_id}')
        seen.add(case_id)

        cls = case.get('class')
        if cls not in ALLOWED_CLASSES:
            fail(f'{case_id}: invalid class {cls!r}')

        src = case.get('source_path')
        if not src or not isinstance(src, str):
            fail(f'{case_id}: missing source_path')
        if not src.endswith('.tsubasa'):
            fail(f'{case_id}: source_path must end with .tsubasa')
        if '..' in Path(src).parts:
            fail(f'{case_id}: source_path must not traverse upward')
        path = ROOT / src
        if not path.exists():
            fail(f'{case_id}: source_path does not exist: {src}')

        status = case.get('expected_status')
        if status not in ALLOWED_STATUSES:
            fail(f'{case_id}: invalid expected_status {status!r}')

        expected = case.get('expected')
        if status == 'PENDING_REAL_TOBI_RUN':
            if expected is not None:
                fail(f'{case_id}: pending cases must have expected=null')
            if 'verified_with' in case:
                fail(f'{case_id}: pending cases must not include verified_with')
        elif status == 'VERIFIED_WITH_TOBI':
            if expected is None:
                fail(f'{case_id}: verified cases must have expected object')
            if 'verified_with' not in case:
                fail(f'{case_id}: verified cases must include verified_with')

    print(f'OK: manifest structure valid ({len(cases)} cases)')


if __name__ == '__main__':
    main()
