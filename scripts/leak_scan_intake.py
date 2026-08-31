#!/usr/bin/env python3
"""Fail CI if student intake/ contains staff secrets or poll keys."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "intake"
BANNED = (
    "polls-keyed",
    "staffToken",
    "secrets/",
    '"secret"',
    "FIREBASE_STAFF",
    "*Pairs with:*",
)


def main() -> int:
    errors = []
    index = INTAKE / "index.html"
    if not index.is_file() or index.stat().st_size < 100:
        print("intake/index.html missing", file=sys.stderr)
        return 1
    for path in INTAKE.rglob("*"):
        if not path.is_file() or path.suffix in {".png", ".jpg", ".webp"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for bad in BANNED:
            if bad in text:
                errors.append(f"{path.relative_to(ROOT)} contains {bad!r}")
    text = index.read_text(encoding="utf-8", errors="ignore")
    if "mgt816-intake-2026-v2" not in text and "mgt816-intake-2026-v1" not in text:
        errors.append("intake schema missing")
    if errors:
        print("intake leak-scan FAIL:", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        return 1
    print("intake leak-scan PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
