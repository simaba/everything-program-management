---
name: raid-update
description: Add or update a RAID row with schema-validated structure.
---

# /raid-update

Add a new row or update an existing row in a RAID log.

## Usage

```
/raid-update [id?] [short description]
```

Examples:
- `/raid-update China data residency exposure` — creates new row
- `/raid-update RAID-0014 Legal flagged new PIPL draft; re-score to high` — updates existing

## What it does

1. Invokes the `raid-log` skill.
2. If no ID given, generates the next available (`RAID-NNNN`).
3. Prompts for any fields the description doesn't cover (type: Risk/Assumption/Issue/Dependency, severity, likelihood, owner, due).
4. Validates the row against `schemas/raid-row.json`.
5. Appends or updates the row in the log referenced by `WORKING-CONTEXT.md` (or a user-specified path).

## Output

The updated row in the log, plus a one-line summary: "Added RAID-0014 [title] — severity 4, owner Marcus, due 2026-04-22."

## Schema

See `schemas/raid-row.json`. Fields: id, type, title, description, severity (1-5), likelihood (1-5), owner, due, status, last_updated.
