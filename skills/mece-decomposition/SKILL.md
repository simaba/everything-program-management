---
name: mece-decomposition
description: >-
  Decompose a problem, scope, or list into Mutually Exclusive and
  Collectively Exhaustive (MECE) branches. Produces a labelled tree,
  checks for overlap and gaps, and rejects or repairs breakdowns that
  fail either property. Method: Barbara Minto (McKinsey).
  TRIGGER when: user asks to "break down", "decompose", "structure
  this problem", "audit this list for MECE", or presents a bullet list
  that needs to be proven exhaustive.
  DO NOT TRIGGER when: the user wants a chronological plan (use
  project-charter), a decision among options (use decision-memo), or
  an exec-brief structure (use pyramid-principle or scr-narrative).
origin: community
---

# MECE Decomposition

Take a fuzzy problem statement or a messy list and produce a tree whose branches are **Mutually Exclusive** (no overlap) and **Collectively Exhaustive** (no gap).

## When to Use

- You have a problem and don't yet know the shape of the solution space.
- A stakeholder has handed you a "list of things to consider" and you suspect it has duplicates or missing branches.
- You're about to write a brief and need to prove the structure before you write prose.
- You need to assign ownership across a team and want to prove no work is double-covered or dropped.

**Do not use** for sequencing (use a project charter's milestones), for multi-option decisions (use `decision-memo`), or for prioritization (MECE is a structure check, not a ranking).

## The Method

MECE is from Barbara Minto's *The Pyramid Principle* (first internal McKinsey use, 1960s). Two properties:

1. **Mutually Exclusive** — every fact, option, or cause belongs in exactly one branch. No item can reasonably appear under two branches.
2. **Collectively Exhaustive** — the branches cover the entire problem space. There is no "other" bucket carrying meaningful weight.

Three common decomposition axes, from most to least preferred:

| Axis | Example | MECE strength |
|---|---|---|
| **Structure / anatomy** | "Costs = fixed + variable" | Strong — derives from definition. |
| **Process / flow** | "User journey = acquire → activate → retain → refer → revenue" | Strong when the process is sequential and non-branching. |
| **Category / enumeration** | "Stakeholders = internal + external + regulatory" | Weak — prone to overlap. Verify by counter-example. |

Prefer structural axes. Use categorical axes only when structural and process axes don't fit.

## How It Works

1. **Restate the problem** as a single question or scope statement. Refuse to decompose until this is concrete. A vague problem produces a vague tree.
2. **Propose an axis** and one decomposition along it. Label the axis explicitly ("decomposing by process").
3. **Test ME**: for each pair of branches, ask "could a real example sit in both?" If yes, redraw.
4. **Test CE**: ask "what is not in any branch?" Construct at least one counter-example from the real domain. If the counter-example doesn't fit anywhere, add a branch or redraw.
5. **Recurse** one level. Stop at the shallowest depth that answers the user's underlying question. Deeper is almost always wrong.
6. **Output** the tree plus a one-paragraph justification of the chosen axis.

## Examples

### Good — Structural axis

> **Problem**: Why is our gross margin dropping?
>
> **Axis**: Revenue − COGS, decomposed structurally.
>
> ```
> Gross margin drop
> ├── Revenue side
> │   ├── Price realization (net of discounts)
> │   └── Product mix
> └── COGS side
>     ├── Unit cost (materials, labor, freight)
>     └── Volume / fixed-cost absorption
> ```
>
> Justified: every gross-margin driver must sit in revenue or COGS, and within each, sits in exactly one of two child branches. ME holds by definition; CE holds because revenue + COGS is gross margin by construction.

### Bad — Categorical overlap

> **Problem**: Why are we missing our sales number?
>
> **Axis** (rejected): "Marketing, product, and sales team issues."
>
> Fails ME: a pricing change is both a product issue and a marketing issue.
> Fails CE: what about macro demand? Channel partners? Sales enablement tooling?
>
> **Repair**: decompose along the revenue funnel (structural) — top-of-funnel volume, funnel conversion rates, deal size, churn. Each sales-number driver sits in exactly one of these.

### Good — Process axis

> **Problem**: Where are we losing users in onboarding?
>
> **Axis**: Onboarding process, sequential.
>
> ```
> Onboarding funnel
> ├── Sign-up (landing → form submit → email verify)
> ├── First-value (first successful action in product)
> ├── Return (day-2, day-7 return rates)
> └── Habit (week-4 retention)
> ```
>
> Justified: the stages are temporally non-overlapping and cover every user from first landing to habituated use.

## Reviewer Checklist

Before presenting the tree, verify:

- [ ] **Axis is labeled.** "Decomposing by [structural / process / categorical]."
- [ ] **ME holds.** For every pair of sibling branches, a real example cannot sit in both.
- [ ] **CE holds.** At least one concrete counter-example from the domain was considered and found a home.
- [ ] **No "other" bucket.** If one exists, it's either empty or the tree needs redrawing.
- [ ] **Depth matches the question.** Not deeper for its own sake.
- [ ] **Each branch is phrased as a noun phrase**, not a full sentence. Branches are categories, not claims.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Branches overlap semantically ("cost reduction" and "efficiency gains") | Pick one label; merge or separate the underlying items. |
| "Other" bucket carries >20% of the weight | Tree is wrong. Redraw with a different axis. |
| Tree is 5 levels deep | User probably asked a 2-level question. Prune. |
| Branches are full sentences ("We should invest in marketing") | Re-label as noun phrases. Claims belong in the Pyramid, not the decomposition. |

## Source

- Barbara Minto, *The Pyramid Principle*, chapter on grouping and summarizing.
- McKinsey internal training materials on MECE use in problem-solving.
- Ethan Rasiel, *The McKinsey Way*, chapter on MECE.
