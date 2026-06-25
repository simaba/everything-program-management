from __future__ import annotations

import json
from pathlib import Path

from pmkit.cli import main
from pmkit.validators import _split_frontmatter, validate_json_file, validate_markdown_frontmatter


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples" / "data"


def test_valid_raid_example_passes() -> None:
    errors = validate_json_file(EXAMPLES / "raid-row.json", SCHEMAS / "raid-row.schema.json")
    assert errors == []


def test_valid_decision_memo_example_passes() -> None:
    errors = validate_markdown_frontmatter(
        EXAMPLES / "decision-memo.md",
        SCHEMAS / "decision-memo-frontmatter.schema.json",
    )
    assert errors == []


def test_frontmatter_iso_dates_remain_schema_compatible_strings() -> None:
    payload, _body = _split_frontmatter(
        "---\ndecision_date: 2026-04-26\n---\n\nExample body\n"
    )

    assert payload["decision_date"] == "2026-04-26"
    assert isinstance(payload["decision_date"], str)


def test_invalid_raid_example_fails(tmp_path) -> None:
    bad = {
        "id": "R-99",
        "type": "risk",
        "title": "Bad",
        "status": "open",
        "severity": 9,
        "owner": "X",
        "due_date": "not-a-date",
        "summary": "too short",
    }
    path = tmp_path / "bad-raid.json"
    path.write_text(json.dumps(bad), encoding="utf-8")

    errors = validate_json_file(path, SCHEMAS / "raid-row.schema.json")
    assert errors


def test_cli_validate_raid_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["pmkit", "validate", "raid", str(EXAMPLES / "raid-row.json")],
    )
    assert main() == 0
    captured = capsys.readouterr()
    assert "VALID" in captured.out


def test_cli_validate_decision_memo_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["pmkit", "validate", "decision-memo", str(EXAMPLES / "decision-memo.md")],
    )
    assert main() == 0
    captured = capsys.readouterr()
    assert "VALID" in captured.out
