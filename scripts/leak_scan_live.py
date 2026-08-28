#!/usr/bin/env python3
"""Fail CI if live/ contains poll keys or staff phrasing."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "live"
BANNED = (
    '"answer"',
    "Answer:",
    "**Answer:**",
    "*Pairs with:*",
    "polls-keyed",
    "staffToken",
)


def main() -> int:
    errors = []
    if not LIVE.is_dir():
        print("live/ missing", file=sys.stderr)
        return 1
    polls = LIVE / "polls.json"
    if not polls.is_file():
        print("live/polls.json missing", file=sys.stderr)
        return 1
    data = json.loads(polls.read_text(encoding="utf-8"))
    if data.get("schema") != "mgt816-live-polls-v1":
        errors.append("unexpected schema")
    if len(data.get("sessions", [])) != 10:
        errors.append("expected 10 sessions")
    for ses in data.get("sessions", []):
        for q in ses.get("questions", []):
            if "answer" in q or "note" in q:
                errors.append(f"{ses.get('id')} {q.get('id')} has staff fields")
            if set(q.get("choices", {})) != {"A", "B", "C", "D"}:
                errors.append(f"{ses.get('id')} {q.get('id')} missing A-D")
    for path in LIVE.rglob("*"):
        if not path.is_file() or path.suffix in {".png", ".jpg", ".webp"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for bad in BANNED:
            if bad in text and path.name != "leak_scan_live.py":
                errors.append(f"{path.relative_to(ROOT)} contains {bad!r}")
    if errors:
        print("live leak-scan FAIL:", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        return 1
    print("live leak-scan PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
