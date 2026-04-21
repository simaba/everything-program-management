---
name: decision-memo
description: Draft an options-with-recommendation decision memo.
---

# /decision-memo

Draft a structured decision memo: question, criteria, options, recommendation, consequences, asks.

## Usage

```
/decision-memo [one-sentence question]
```

Examples:
- `/decision-memo Should we pause Japan launch given the regulatory delay?`
- `/decision-memo Should the VoxOS China voice assistant run on-device or in cloud?`

## What it does

1. Invokes the `decision-memo` skill.
2. Enforces the hard rule: ≥ 2 viable options, or an explicit "Ruled Out" section listing ≥ 2 alternatives.
3. Generates frontmatter (id, title, decider, due, status) validated against `schemas/decision-memo-frontmatter.json`.
4. Asks (at most one) clarifying question — typically about criteria or decider — if missing.
5. Writes criteria before options to prevent reverse-engineering.
6. Produces a ≤ 3-page memo ready to circulate.

## Output

Markdown file saved to `examples/decisions/DM-NNNN-<slug>.md` with auto-incremented ID.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: ≥ 2 options, criteria written before options, every option quantified on every criterion, reversibility marked (one-way vs two-way), recommendation is a stance, explicit asks addressed to named peop