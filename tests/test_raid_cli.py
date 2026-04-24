from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "raid_cli.py"

spec = importlib.util.spec_from_file_location("raid_cli", SCRIPT_PATH)
raid_cli = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(raid_cli)


def test_split_frontmatter_parses_rows() -> None:
    text = """---
rows:
  - id: RAID-0001
    type: Risk
    title: Supplier delay
    severity: 4
    likelihood: 3
    owner: Sima
    status: open
---
# RAID Log
"""
    fm, body = raid_cli.split_frontmatter(text)
    assert fm["rows"][0]["id"] == "RAID-0001"
    assert body.strip() == "# RAID Log"


def test_next_id_advances_from_existing_rows() -> None:
    rows = [{"id": "RAID-0001"}, {"id": "RAID-0007"}]
    assert raid_cli.next_id(rows) == "RAID-0008"


def test_coerce_dates_normalizes_python_date_objects() -> None:
    import datetime as dt

    value = {"due": dt.date(2026, 4, 24)}
    assert raid_cli._coerce_dates(value)["due"] == "2026-04-24"
