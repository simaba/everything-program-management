# Rule: MECE Before Lists

**Always load.**

Any list, breakdown, or decomposition the harness produces must be tested for MECE before publishing.

## Rule

A list of "things to consider" is not a structure. Before producing one, the harness must:

1. Label the axis ("decomposing by [structural / process / categorical]").
2. Verify Mutually Exclusive — no item belongs in two branches.
3. Verify Collectively Exhaustive — at least one counter-example from the domain finds a home.

If either fails, the list is wrong and must be redrawn before output.

## Application

- "Five reasons why X happened" — must pass ME and CE before publication.
- "Three options for Y" — see also `decision-memo-needs-2-options`.
- "Workstreams of program Z" — must be MECE; overlapping workstreams produce double-staffed work and dropped work.
- "Risks in this program" — RAID rows can co-exist (a risk and a dependency are different categories), but within a category, items should be MECE.

## What the harness must do

When producing any list with > 2 items, internally run the MECE check from `skills/mece-decomposition/SKILL.md`. If the check fails:

1. Either repair the list (preferred — usually means switching axis).
2. Or label the list as "non-MECE working list" and explain why MECE doesn't apply (rare; only for true brainstorm output).

Silently producing non-MECE lists with no flag is a rule violation.

## Counter-examples the harness should reject

- "Stakeholders: marketing, product, sales team" — categorical, prone to overlap.
- "Reasons we're behind: scope, time, team morale, dependencies, budget" — overlap (scope and dependencies often the same root cause).

## Source

- Barbara Minto, *The Pyramid Principle*, on grouping and MECE.
- McKinsey internal training, MECE as the universal structural test.
