from __future__ import annotations

import json
from pathlib import Path

from pmkit.validators import validate_json_file, validate_markdown_frontmatter


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def test_valid_raid_row_passes(tmp_path: Path) -> None:
    payload = {
        "id": "RAID-0001",
        "type": "risk",
        "title": "External interface decision may delay the fictional pilot",
        "description": "The fictional library pilot depends on an interface decision that may arrive after the planned validation window.",
        "category": "schedule",
        "owner": "fictional-delivery-lead@example.test",
        "opened": "2026-04-26",
        "due": "2026-05-10",
        "status": "mitigating",
        "last_updated": "2026-04-27",
        "probability": 3,
        "impact": 4,
        "score": 12,
        "mitigation": "Confirm the dependency and define a reversible fallback scope.",
        "trigger": "The decision remains unresolved five working days before validation starts.",
    }
    path = tmp_path / "raid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    errors = validate_json_file(path, SCHEMAS / "raid-row.schema.json")
    assert errors == []


def test_invalid_raid_row_fails(tmp_path: Path) -> None:
    payload = {
        "id": "BAD-1",
        "type": "risk",
        "title": "Bad",
        "description": "short",
        "category": "unknown",
        "owner": "X",
        "opened": "not-a-date",
        "due": "2026-05-10",
        "status": "unknown",
        "last_updated": "2026-04-27",
        "probability": 8,
        "impact": 0,
        "score": 99,
    }
    path = tmp_path / "raid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    errors = validate_json_file(path, SCHEMAS / "raid-row.schema.json")
    assert errors


def test_valid_decision_memo_frontmatter_passes(tmp_path: Path) -> None:
    content = """---
id: DM-0001
title: Choose the processing model for the fictional library pilot
decider: fictional-sponsor@example.test
due: 2026-05-01
status: in_review
decided: null
decision: null
review_date: 2026-06-01
decision_scope: Choose the processing model for the bounded pilot only.
linked_raid_ids:
  - RAID-0001
---

# Decision Memo

Body.
"""
    path = tmp_path / "decision.md"
    path.write_text(content, encoding="utf-8")

    errors = validate_markdown_frontmatter(
        path,
        SCHEMAS / "decision-memo-frontmatter.schema.json",
    )
    assert errors == []


def test_invalid_decision_memo_frontmatter_fails(tmp_path: Path) -> None:
    content = """---
id: memo-1
title: Bad
decider: X
due: not-a-date
status: maybe
decided: 2026-05-01
decision: ''
review_date: 2026-06-01
---

# Decision Memo
"""
    path = tmp_path / "decision.md"
    path.write_text(content, encoding="utf-8")

    errors = validate_markdown_frontmatter(
        path,
        SCHEMAS / "decision-memo-frontmatter.schema.json",
    )
    assert errors
