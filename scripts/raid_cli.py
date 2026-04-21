#!/usr/bin/env python3
"""
raid_cli.py — tiny helper for working with a RAID log file.

A RAID log is stored as a Markdown file with a YAML frontmatter block
containing a list of rows. Each row validates against
schemas/raid-row.json.

Subcommands:
  list                  show all rows
  add                   add a new row interactively
  update <id> <field=val ...>  update fields on an existing row
  validate              validate the entire log against the schema
  triage                emit a Now/This Week/This Month/Watch view

Designed to be small, dependency-light (PyYAML + jsonschema only), and
mirror the behavior the harness applies when invoking the raid-log skill.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore[import-untyped]
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("jsonschema required: pip install jsonschema\n")
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "raid-row.json"


def load_schema() -> dict[str, Any]:
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return (frontmatter_dict, body_after_frontmatter)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end + 5 :]
    return yaml.safe_load(fm_raw) or {}, body


def _coerce_dates(value: Any) -> Any:
    """Convert PyYAML-parsed date/datetime values to ISO strings.

    PyYAML auto-parses ISO date literals into datetime.date objects,
    but the schema defines 'due' and 'last_updated' as string with
    format: date. Normalize on the way out so consumers and validators
    see strings regardless of how the YAML was authored.
    """
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _coerce_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_coerce_dates(v) for v in value]
    return value


def write_log(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{fm_yaml}---\n{body}", encoding="utf-8")


def next_id(rows: list[dict[str, Any]]) -> str:
    nums = [
        int(r["id"].split("-")[1])
        for r in rows
        if isinstance(r.get("id"), str) and r["id"].startswith("RAID-")
    ]
    return f"RAID-{(max(nums) + 1 if nums else 1):04d}"


def cmd_list(args: argparse.Namespace) -> int:
    fm, _ = split_frontmatter(Path(args.log).read_text(encoding="utf-8"))
    rows = [_coerce_dates(r) for r in fm.get("rows", [])]
    for r in rows:
        print(
            f"{r.get('id'):<10} {r.get('type','?'):<11} "
            f"sev={r.get('severity','?')} lik={r.get('likelihood','?')} "
            f"owner={r.get('owner','?'):<14} status={r.get('status','?'):<11} "
            f"{r.get('title','')}"
        )
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    schema = load_schema()
    validator = Draft202012Validator(schema)
    fm, _ = split_frontmatter(Path(args.log).read_text(encoding="utf-8"))
    rows = [_coerce_dates(r) for r in fm.get("rows", [])]
    errors: list[str] = []
    for r in rows:
        for err in validator.iter_errors(r):
            errors.append(f"{r.get('id','<no-id>')}: {err.message}")
    if errors:
        print("Validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"Validation OK ({len(rows)} rows)")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    schema = load_schema()
    log_path = Path(args.log)
    fm, body = split_frontmatter(log_path.read_text(encoding="utf-8"))
    rows = fm.setdefault("rows", [])
    row: dict[str, Any] = {
        "id": next_id(rows),
        "type": args.type,
        "title": args.title,
        "severity": args.severity,
        "likelihood": args.likelihood,
        "owner": args.owner,
        "status": args.status,
        "last_updated": dt.date.today().isoformat(),
    }
    if args.description:
        row["description"] = args.description
    if args.due:
        row["due"] = args.due
    Draft202012Validator(schema).validate(row)
    rows.append(row)
    write_log(log_path, fm, body)
    print(f"Added {row['id']}")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    schema = load_schema()
    log_path = Path(args.log)
    fm, body = split_frontmatter(log_path.read_text(encoding="utf-8"))
    rows = fm.get("rows", [])
    target = next((r for r in rows if r.get("id") == args.id), None)
    if target is None:
        print(f"ID {args.id} not found", file=sys.stderr)
        return 1
    for kv in args.fields:
        k, _, v = kv.partition("=")
        if not k or not v:
            print(f"Bad field assignment: {kv}", file=sys.stderr)
            return 2
        if k in {"severity", "likelihood"}:
            target[k] = int(v)
        else:
            target[k] = v
    target["last_updated"] = dt.date.today().isoformat()
    Draft202012Validator(schema).validate(target)
    write_log(log_path, fm, body)
    print(f"Updated {args.id}")
    return 0


def cmd_triage(args: argparse.Namespace) -> int:
    fm, _ = split_frontmatter(Path(args.log).read_text(encoding="utf-8"))
    rows = [
        _coerce_dates(r)
        for r in fm.get("rows", [])
        if r.get("status") not in {"closed", "transferred"}
    ]
    today = dt.date.today()
    horizon = today + dt.timedelta(days=args.window)

    def bucket(r: dict[str, Any]) -> str:
        due_s = r.get("due")
        if due_s is None:
            return "WATCH"
        due = dt.date.fromisoformat(due_s)
        if due <= today + dt.timedelta(days=1):
            return "NOW"
        if due <= today + dt.timedelta(days=7):
            return "THIS WEEK"
        if due <= horizon:
            return "THIS MONTH"
        return "WATCH"

    buckets: dict[str, list[dict[str, Any]]] = {
        "NOW": [],
        "THIS WEEK": [],
        "THIS MONTH": [],
        "WATCH": [],
    }
    for r in rows:
        buckets[bucket(r)].append(r)

    for label in ["NOW", "THIS WEEK", "THIS MONTH", "WATCH"]:
        items = buckets[label]
        print(f"\n## {label} ({len(items)})")
        for r in items:
            print(
                f"  - {r.get('id')} sev={r.get('severity')} "
                f"owner={r.get('owner')} due={r.get('due','-')} "
                f"{r.get('title','')}"
            )
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--log", required=True, help="Path to RAID log markdown file")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list").set_defaults(func=cmd_list)
    sub.add_parser("validate").set_defaults(func=cmd_validate)

    a = sub.add_parser("add")
    a.add_argument("--type", required=True, choices=["Risk", "Assumption", "Issue", "Dependency"])
    a.add_argument("--title", required=True)
    a.add_argument("--severity", type=int, required=True, choices=range(1, 6))
    a.add_argument("--likelihood", type=int, required=True, choices=range(1, 6))
    a.add_argument("--owner", required=True)
    a.add_argument("--status", default="open",
                   choices=["open", "mitigating", "watch", "accepted", "closed", "transferred"])
    a.add_argument("--due", help="ISO date YYYY-MM-DD")
    a.add_argument("--description")
    a.set_defaults(func=cmd_add)

    u = sub.add_parser("update")
    u.add_argument("id")
    u.add_argument("fields", nargs="+", help="field=value pairs, e.g. severity=4 status=mitigating")
    u.set_defaults(func=cmd_update)

    t = sub.add_parser("triage")
    t.add_argument("--window", type=int, default=30, help="days for THIS MONTH bucket horizon")
    t.set_defaults(func=cmd_triage)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
