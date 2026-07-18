from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


class _FrontmatterLoader(yaml.SafeLoader):
    """Safe loader that keeps ISO-looking dates as strings for JSON Schema."""


_FrontmatterLoader.yaml_implicit_resolvers = {
    first_char: [
        resolver
        for resolver in resolvers
        if resolver[0] != "tag:yaml.org,2002:timestamp"
    ]
    for first_char, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _load_schema(schema_path: str | Path) -> dict[str, Any]:
    path = Path(schema_path)
    return json.loads(path.read_text(encoding="utf-8"))


def _format_errors(errors: list[Any]) -> list[str]:
    lines: list[str] = []
    for error in sorted(errors, key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        lines.append(f"{location}: {error.message}")
    return lines


def _schema_errors(payload: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return _format_errors(list(validator.iter_errors(payload)))


def _raid_semantic_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("type") == "risk":
        probability = payload.get("probability")
        impact = payload.get("impact")
        score = payload.get("score")
        if (
            isinstance(probability, int)
            and not isinstance(probability, bool)
            and isinstance(impact, int)
            and not isinstance(impact, bool)
            and isinstance(score, int)
            and not isinstance(score, bool)
            and score != probability * impact
        ):
            errors.append(
                "score: risk score must equal probability multiplied by impact "
                f"({probability} × {impact} = {probability * impact})"
            )
    return errors


def _decision_memo_semantic_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    status = payload.get("status")
    decided = payload.get("decided")
    decision = payload.get("decision")
    review_date = payload.get("review_date")

    if status == "decided" and (not decided or not decision):
        errors.append("status: decided memos require both decided and decision values")
    if status in {"draft", "in_review"} and (decided is not None or decision is not None):
        errors.append("status: draft and in_review memos must keep decided and decision null")
    if status == "deferred" and not review_date:
        errors.append("review_date: deferred decisions require a non-null review date")
    if status == "superseded" and not payload.get("supersedes"):
        errors.append("supersedes: superseded decisions require the prior decision id")
    return errors


def validate_json_file(data_path: str | Path, schema_path: str | Path) -> list[str]:
    payload = json.loads(Path(data_path).read_text(encoding="utf-8"))
    schema = _load_schema(schema_path)
    errors = _schema_errors(payload, schema)
    if errors:
        return errors
    if schema.get("title") == "RAID Row" and isinstance(payload, dict):
        errors.extend(_raid_semantic_errors(payload))
    return errors


def _split_frontmatter(markdown_text: str) -> tuple[dict[str, Any], str]:
    normalized = markdown_text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("Markdown file does not start with YAML frontmatter")

    parts = normalized.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Markdown frontmatter is not closed with '---'")

    frontmatter_text = parts[0][4:]
    body = parts[1]
    payload = yaml.load(frontmatter_text, Loader=_FrontmatterLoader) or {}
    if not isinstance(payload, dict):
        raise ValueError("Markdown frontmatter must parse to an object")
    return payload, body


def validate_markdown_frontmatter(
    data_path: str | Path,
    schema_path: str | Path,
) -> list[str]:
    payload, _body = _split_frontmatter(Path(data_path).read_text(encoding="utf-8"))
    schema = _load_schema(schema_path)
    errors = _schema_errors(payload, schema)
    if errors:
        return errors
    if schema.get("title") == "Decision Memo Frontmatter":
        errors.extend(_decision_memo_semantic_errors(payload))
    return errors
