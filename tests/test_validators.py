from __future__ import annotations

import json
from pathlib import Path

from pmkit.validators import validate_json_file, validate_markdown_frontmatter


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def test_valid_raid_row_passes(tmp_path: Path) -> None:
    payload = {
        "id": "R-0001",
        "type": "risk",
        "title": "Supplier API approval may slip launch date",
        "status": "open",
        "severity": 4,
        "owner": "Sima Bagheri",
        "due_date": "2026-05-10",
        "summary": "Approval from the external supplier is still pending and may push integration.",
    }
    path = tmp_path / "raid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    errors = validate_json_file(path, SCHEMAS / "raid-row.schema.json")
    assert errors == []


def test_invalid_raid_row_fails(tmp_path: Path) -> None:
    payload = {
        "id": "BAD-1",
        "type": "risk",
        "title": "Too short",
        "status": "unknown",
        "severity": 8,
        "owner": "S",
        "due_date": "2026-05-10",
        "summary": "short",
    }
    path = tmp_path / "raid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    errors = validate_json_file(path, SCHEMAS / "raid-row.schema.json")
    assert errors


def test_valid_decision_memo_frontmatter_passes(tmp_path: Path) -> None:
    content = """---
decision_id: DM-0001
title: Choose rollout option for supplier migration
status: in_review
owner: Sima Bagheri
decision_date: 2026-05-01
review_date: 2026-06-01
recommended_option: Option B
linked_raid_ids:
  - R-0001
---

# Decision Memo

Body.
"""
    path = tmp_path / "decision.md"
    path.write_text(content, encoding="utf-8")

    errors = validate_markdown_frontmatter(path, SCHEMAS / "decision-memo-frontmatter.schema.json")
    assert errors == []


def test_invalid_decision_memo_frontmatter_fails(tmp_path: Path) -> None:
    content = """---
decision_id: memo-1
title: Bad
status: maybe
owner: X
decision_date: 2026-05-01
review_date: 2026-06-01
recommended_option: ''
---

# Decision Memo
"""
    path = tmp_path / "decision.md"
    path.write_text(content, encoding="utf-8")

    errors = validate_markdown_frontmatter(path, SCHEMAS / "decision-memo-frontmatter.schema.json")
    assert errors
