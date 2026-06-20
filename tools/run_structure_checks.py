#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ROOT / 'tools' / 'check_manifest_structure.py',
    ROOT / 'tools' / 'check_public_boundary.py',
]


def main() -> None:
    for check in CHECKS:
        print(f'==> {check.relative_to(ROOT)}')
        subprocess.run([sys.executable, str(check)], cwd=ROOT, check=True)
    print('OK: all public structure checks passed')


if __name__ == '__main__':
    main()
