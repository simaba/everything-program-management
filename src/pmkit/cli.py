from __future__ import annotations

import argparse
from pathlib import Path

from .validators import validate_json_file, validate_markdown_frontmatter

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"


def _schema_path(name: str) -> Path:
    mapping = {
        "raid": SCHEMAS / "raid-row.schema.json",
        "decision-memo": SCHEMAS / "decision-memo-frontmatter.schema.json",
    }
    if name not in mapping:
        raise SystemExit(f"Unknown schema alias: {name}")
    return mapping[name]


def main() -> int:
    parser = argparse.ArgumentParser(prog="pmkit")
    sub = parser.add_subparsers(dest="command")

    validate = sub.add_parser("validate", help="Validate a PM artifact against a bundled schema")
    validate.add_argument("kind", choices=["raid", "decision-memo"])
    validate.add_argument("path")

    args = parser.parse_args()

    if args.command != "validate":
        parser.print_help()
        return 1

    schema = _schema_path(args.kind)
    if args.kind == "raid":
        errors = validate_json_file(args.path, schema)
    else:
        errors = validate_markdown_frontmatter(args.path, schema)

    if errors:
        print("INVALID")
        for line in errors:
            print(f"- {line}")
        return 2

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
