#!/usr/bin/env python3
"""
decision_journal_review.py — surface decision memos due for review.

A decision memo (DM-NNNN) lives in examples/decisions/ with YAML
frontmatter validated against schemas/decision-memo-frontmatter.json.

This script walks a directory of decision memos and emits a review
prompt for each one that:

  - is in status 'in_review' and the 'due' date is within N days
    (default 7), OR
  - was 'decided' more than 90 days ago and has not been retrospected
    (no 'retro_date' field).

The output is intended to be pasted into a weekly review or fed to
the harness as the kickoff of a decision-journal retrospection pass.

Usage:
    python scripts/decision_journal_review.py --dir examples/decisions/
    python scripts/decision_journal_review.py --dir examples/decisions/ --window 14
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore[import-untyped]
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    sys.exit(2)


def _coerce_dates(value: Any) -> Any:
    """PyYAML auto-parses ISO dates into datetime.date; the schema and
    this script both treat them as ISO strings. Normalize on read."""
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _coerce_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_coerce_dates(v) for v in value]
    return value


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    return _coerce_dates(yaml.safe_load(text[4:end]) or {})


def find_memos(directory: Path) -> list[tuple[Path, dict[str, Any]]]:
    memos: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(directory.glob("DM-*.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm:
            memos.append((path, fm))
    return memos


def due_for_decision(fm: dict[str, Any], today: dt.date, window_days: int) -> bool:
    if fm.get("status") != "in_review":
        return False
    due_s = fm.get("due")
    if not due_s:
        return False
    try:
        due = dt.date.fromisoformat(due_s)
    except (TypeError, ValueError):
        return False
    return today <= due <= today + dt.timedelta(days=window_days)


def due_for_retrospection(fm: dict[str, Any], today: dt.date) -> bool:
    if fm.get("status") != "decided":
        return False
    if fm.get("retro_date"):
        return False
    decided_s = fm.get("decided")
    if not decided_s:
        return False
    try:
        decided = dt.date.fromisoformat(decided_s)
    except (TypeError, ValueError):
        return False
    return (today - decided).days >= 90


def render_review_prompt(memos: list[tuple[Path, dict[str, Any]]], today: dt.date,
                         window: int) -> str:
    decision_due = [m for m in memos if due_for_decision(m[1], today, window)]
    retro_due = [m for m in memos if due_for_retrospection(m[1], today)]

    lines: list[str] = [f"# Decision Journal Review — {today.isoformat()}", ""]

    lines.append(f"## Decisions due in next {window} days ({len(decision_due)})")
    if not decision_due:
        lines.append("- None.")
    for path, fm in decision_due:
        lines.append(
            f"- **{fm.get('id')}** {fm.get('title','')} — decider: {fm.get('decider','?')} "
            f"— due: {fm.get('due','?')} — {path}"
        )
    lines.append("")

    lines.append(f"## Decisions due for 90-day retrospection ({len(retro_due)})")
    if not retro_due:
        lines.append("- None.")
    for path, fm in retro_due:
        decided = fm.get("decided", "?")
        chosen = fm.get("decision", "?")
        lines.append(
            f"- **{fm.get('id')}** {fm.get('title','')} — decided {decided} -> {chosen} — "
            f"prompt: did the predicted consequences hold? — {path}"
        )
    lines.append("")

    lines.append("## Retrospection prompt template")
    lines.append("For each decided memo above, ask:")
    lines.append("1. Which option did we pick? Was the recommended option chosen?")
    lines.append("2. Did the predicted consequences hold? Which were wrong?")
    lines.append("3. With the benefit of hindsight, would we make the same call?")
    lines.append("4. What lesson, if any, transfers to upcoming decisions?")
    lines.append("")
    lines.append("Add a `retro_date` field to each retrospected memo to take it off this list.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--dir", required=True, type=Path,
                   help="Directory of decision memos (DM-*.md files)")
    p.add_argument("--window", type=int, default=7,
                   help="Days ahead to surface in_review memos (default: 7)")
    p.add_argument("--today", type=str, default=None,
                   help="Override today's date (YYYY-MM-DD), for testing")
    args = p.parse_args(argv)

    if not args.dir.exists():
        print(f"Directory not found: {args.dir}", file=sys.stderr)
        return 1

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    memos = find_memos(args.dir)
    print(render_review_prompt(memos, today, args.window))
    return 0


if __name__ == "__main__":
    sys.exit(main())
