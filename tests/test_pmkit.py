from __future__ import annotations

import json
from pathlib import Path

from pmkit.cli import main
from pmkit.validators import _split_frontmatter, validate_json_file, validate_markdown_frontmatter


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples" / "data"


def _write_json(tmp_path: Path, payload: dict) -> Path:
    path = tmp_path / "artifact.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _write_memo(tmp_path: Path, frontmatter: str) -> Path:
    path = tmp_path / "memo.md"
    path.write_text(f"---\n{frontmatter}\n---\n\n# Memo\n", encoding="utf-8")
    return path


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
        "---\ndue: 2026-04-26\n---\n\nExample body\n"
    )

    assert payload["due"] == "2026-04-26"
    assert isinstance(payload["due"], str)


def test_frontmatter_accepts_windows_line_endings() -> None:
    payload, body = _split_frontmatter(
        "---\r\nid: DM-0001\r\n---\r\n\r\nExample body\r\n"
    )

    assert payload["id"] == "DM-0001"
    assert "Example body" in body


def test_invalid_raid_date_is_rejected(tmp_path: Path) -> None:
    payload = json.loads((EXAMPLES / "raid-row.json").read_text(encoding="utf-8"))
    payload["due"] = "not-a-date"

    errors = validate_json_file(_write_json(tmp_path, payload), SCHEMAS / "raid-row.schema.json")

    assert any("due" in error and "date" in error for error in errors)


def test_risk_requires_type_specific_fields(tmp_path: Path) -> None:
    payload = json.loads((EXAMPLES / "raid-row.json").read_text(encoding="utf-8"))
    del payload["trigger"]

    errors = validate_json_file(_write_json(tmp_path, payload), SCHEMAS / "raid-row.schema.json")

    assert any("trigger" in error and "required" in error for error in errors)


def test_risk_score_must_match_probability_times_impact(tmp_path: Path) -> None:
    payload = json.loads((EXAMPLES / "raid-row.json").read_text(encoding="utf-8"))
    payload["score"] = 11

    errors = validate_json_file(_write_json(tmp_path, payload), SCHEMAS / "raid-row.schema.json")

    assert any("must equal probability" in error for error in errors)


def test_assumption_requires_validation_plan(tmp_path: Path) -> None:
    payload = {
        "id": "RAID-0002",
        "type": "assumption",
        "title": "Independent review can finish before the pilot",
        "description": "The fictional plan depends on an external review completing before pilot onboarding begins.",
        "category": "external",
        "owner": "owner@example.test",
        "opened": "2026-04-26",
        "due": "2026-05-10",
        "status": "open",
        "last_updated": "2026-04-26"
    }

    errors = validate_json_file(_write_json(tmp_path, payload), SCHEMAS / "raid-row.schema.json")

    assert any("validation_plan" in error and "required" in error for error in errors)


def test_closed_raid_record_requires_resolution(tmp_path: Path) -> None:
    payload = json.loads((EXAMPLES / "raid-row.json").read_text(encoding="utf-8"))
    payload["status"] = "closed"

    errors = validate_json_file(_write_json(tmp_path, payload), SCHEMAS / "raid-row.schema.json")

    assert any("resolution" in error and "required" in error for error in errors)


def test_draft_decision_memo_cannot_contain_a_decision(tmp_path: Path) -> None:
    memo = _write_memo(
        tmp_path,
        "\n".join(
            [
                "id: DM-0002",
                "title: Fictional draft decision",
                "decider: sponsor@example.test",
                "due: 2026-05-10",
                "status: draft",
                "decided: null",
                "decision: Option A",
                "review_date: 2026-06-01",
            ]
        ),
    )

    errors = validate_markdown_frontmatter(
        memo,
        SCHEMAS / "decision-memo-frontmatter.schema.json",
    )

    assert any("decision" in error for error in errors)


def test_deferred_decision_requires_non_null_review_date(tmp_path: Path) -> None:
    memo = _write_memo(
        tmp_path,
        "\n".join(
            [
                "id: DM-0003",
                "title: Fictional deferred decision",
                "decider: sponsor@example.test",
                "due: 2026-05-10",
                "status: deferred",
                "decided: null",
                "decision: Defer pending a larger validation sample",
                "review_date: null",
            ]
        ),
    )

    errors = validate_markdown_frontmatter(
        memo,
        SCHEMAS / "decision-memo-frontmatter.schema.json",
    )

    assert any("review_date" in error for error in errors)


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
