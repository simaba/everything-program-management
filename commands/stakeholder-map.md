---
name: stakeholder-map
description: Build a power/interest grid, RACI, and influence path for a program or decision.
---

# /stakeholder-map

Produce three artifacts for a named program or decision: Mendelow power/interest grid, RACI matrix, and influence path.

## Usage

```
/stakeholder-map [program name | decision]
```

Examples:
- `/stakeholder-map Japan launch pause decision`
- `/stakeholder-map EU AI Act conformity assessment program`

## What it does

1. Invokes the `stakeholder-mapper` agent.
2. Pulls candidate stakeholders from `WORKING-CONTEXT.md`, the RAID log, and any prior maps.
3. Proposes power/interest scores; asks the user to ratify before plotting.
4. Builds the grid, a RACI matrix for the major deliverables, and an ordered influence path.
5. Flags missing advocates in Manage-Closely quadrant as program risks.

## Output

Markdown file saved to `examples/stakeholder-maps/<slug>-YYYY-MM-DD.md`.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: no "team" or "leadership" rows, exactly one A per RACI row, Cs capped at 3, influence path ordered with a reason per step.

## Rules enforced

- All high-power stakeholders get a strategy.
- Hostile stakeholders in A or B quadrant get an explicit plan.
