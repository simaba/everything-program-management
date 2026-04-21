---
name: exec-brief
description: Produce a one-page SCR + Pyramid executive brief from any input.
---

# /exec-brief

Compress any input (long doc, thread, transcript, RAID log) into a one-page executive brief.

## Usage

```
/exec-brief [paste source or path] [--audience exec|board|sponsor]
```

Examples:
- `/exec-brief @docs/japan-launch-q2-status.md --audience sponsor`
- `/exec-brief [paste long Slack thread] --audience exec`

## What it does

1. Invokes the `executive-summary` agent.
2. Asks (at most one) clarifying question for audience or ask if not supplied.
3. Applies the `executive-summary-brief` skill (BLUF first, Pyramid structure, explicit Ask).
4. Cuts to one page (~300–400 words).
5. Returns the brief inline and saves to `examples/briefs/exec-brief-<slug>-YYYY-MM-DD.md`.

## Output

A one-page Markdown brief with metadata header (To/From/Date/Re), BLUF, Why-This-Matters, three supporting points, recommendation, risks, and the Ask.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: BLUF on line 1, ≤ one page, the Ask is explicit and dated.
