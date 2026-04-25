from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


def _load_schema(schema_path: str | Path) -> dict[str, Any]:
    path = Path(schema_path)
    return json.loads(path.read_text(encoding="utf-8"))


def _build_validator(schema_path: str | Path) -> Draft202012Validator:
    return Draft202012Validator(_load_schema(schema_path))


def _format_errors(errors: list[Any]) -> list[str]:
    lines: list[str] = []
    for error in sorted(errors, key=lambda e: list(e.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        lines.append(f"{location}: {error.message}")
    return lines


def validate_json_file(data_path: str | Path, schema_path: str | Path) -> list[str]:
    payload = json.loads(Path(data_path).read_text(encoding="utf-8"))
    validator = _build_validator(schema_path)
    return _format_errors(list(validator.iter_errors(payload)))


def _split_frontmatter(markdown_text: str) -> tuple[dict[str, Any], str]:
    if not markdown_text.startswith("---\n"):
        raise ValueError("Markdown file does not start with YAML frontmatter")

    parts = markdown_text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Markdown frontmatter is not closed with '---'")

    frontmatter_text = parts[0][4:]
    body = parts[1]
    payload = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(payload, dict):
        raise ValueError("Markdown frontmatter must parse to an object")
    return payload, body


def validate_markdown_frontmatter(data_path: str | Path, schema_path: str | Path) -> list[str]:
    payload, _body = _split_frontmatter(Path(data_path).read_text(encoding="utf-8"))
    validator = _build_validator(schema_path)
    return _format_errors(list(validator.iter_errors(payload)))
