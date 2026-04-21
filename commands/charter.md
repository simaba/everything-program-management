---
name: charter
description: Generate a project charter from a one-line objective using the project-charter skill.
---

# /charter

Generate a one- to two-page project charter.

## Usage

```
/charter [one-line objective]
```

Examples:
- `/charter Build EU AI Act conformity assessment workflow before Feb 2027 enforcement`
- `/charter Launch VoxOS China voice assistant beta wave 2 by end of Q3`

## What it does

1. Invokes the `project-charter` skill.
2. Asks (at most one) clarifying question if the objective is too vague to charter.
3. Produces a charter following `templates/project-charter.md` + the skill's structure.
4. Seeds the top risk into the RAID log as `RAID-0001` (or next available ID).
5. Returns the charter as Markdown for the user to circulate to the sponsor.

## Output

Saved to `examples/charters/charter-<slug>-YYYY-MM-DD.md` and printed inline.

## Reviewer

The skill's Reviewer Checklist runs automatically before the charter is returned.
