---
name: mece
description: Audit a list or breakdown for MECE (Mutually Exclusive, Collectively Exhaustive) compliance.
---

# /mece

Take a list, breakdown, or decomposition and audit it for MECE compliance. Surface overlaps (non-ME) and gaps (non-CE), then propose a repair.

## Usage

```
/mece [paste list or @path]
```

Examples:
- `/mece Why we're missing the sales number: marketing, product, sales team, macro conditions`
- `/mece @strategy/q3-priorities.md`

## What it does

1. Invokes the `mece-decomposition` skill.
2. Labels the axis of the existing breakdown (structural / process / categorical).
3. Tests each pair of branches for overlap (ME).
4. Constructs counter-examples from the domain to test exhaustiveness (CE).
5. If ME or CE fails, proposes a repair — typically by switching axis from categorical to structural or process.
6. Returns:
   - Audit result (pass / fail with reasons)
   - Repaired tree, if needed
   - One-paragraph justification

## Output

Markdown inline reply. Saves to `examples/mece-audits/<slug>-YYYY-MM-DD.md` if the audit is non-trivial.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: axis labeled, ME held (or flagged), CE held (or flagged), no "other" bucket over 20% weight, branches phrased as noun phrases.
