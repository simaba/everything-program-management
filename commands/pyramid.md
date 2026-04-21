---
name: pyramid
description: Restructure a draft into Pyramid Principle form.
---

# /pyramid

Take a draft document, message, or brief and restructure it into Pyramid Principle form: answer first, then supporting points, then evidence.

## Usage

```
/pyramid [paste draft or @path]
```

Examples:
- `/pyramid [paste long email that buries the ask]`
- `/pyramid @drafts/q2-sponsor-update.md`

## What it does

1. Invokes the `pyramid-principle` skill.
2. Identifies the current lede and the buried answer.
3. Restructures:
   - **Top**: one-sentence conclusion / BLUF
   - **Level 2**: 3 supporting points (MECE)
   - **Level 3**: evidence under each point
4. Flags any hedging language in the top line and suggests a firmer alternative.
5. Returns the restructured version.

## Output

Markdown inline reply with the restructured document. Also saves to `examples/briefs/pyramid-<slug>-YYYY-MM-DD.md` if the input is a file.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: answer on line 1, exactly 3 supporting points at level 2, MECE holds across points, no buried lede anywhere.
