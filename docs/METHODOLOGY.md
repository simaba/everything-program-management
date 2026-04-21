# Methodology

Why these skills, in this shape.

## The Thesis

Program management is a craft with a known canon. The problem is not that PMs lack frameworks — it's that the frameworks live in books (Minto, Grove, Dekker, Bezos's shareholder letters) and get reinvented every week in the moment. An agent harness can codify each framework once and invoke it on demand.

This repo is that codification for ten frameworks that cover ~80% of what a program manager writes.

## The Canon This Repo Draws From

| Framework | Source | Skill |
|---|---|---|
| MECE | Barbara Minto, *The Pyramid Principle* (1987) | `mece-decomposition` |
| Pyramid Principle | Barbara Minto, same | `pyramid-principle` |
| SCR (Situation-Complication-Resolution) | McKinsey consulting, 1970s–present | `scr-narrative` |
| RAID log | UK APM *Body of Knowledge* | `raid-log` |
| Power/Interest grid | Mendelow (1991) | `stakeholder-mapping` |
| RACI | BABOK / PMI PMBOK | `stakeholder-mapping` |
| Project charter | PMI *PMBOK Guide* | `project-charter` |
| DMAIC | Motorola / GE Six Sigma canon | `dmaic-structuring` |
| One-way vs two-way doors | Jeff Bezos, 2015 letter to shareholders | `decision-memo` |
| Blameless post-mortem | Etsy (Allspaw, 2012), Google SRE | `post-mortem-facilitation` |
| BLUF | US military staff writing (AR 25-50) | `executive-summary-brief` |
| Chief-of-staff morning brief | COS literature, Andy Grove | `chief-of-staff-brief` |
| Risk re-triage | PMI PMBOK, ISO 31000 | `risk-triage` |

Every skill has a "Source" section citing its lineage. The codification is ours; the methods are not.

## Why These Specifically

The selection criterion: a PM running a cross-functional program of 5+ people over 3+ months will need every one of these in a quarter. Frameworks excluded on purpose:

- **OKRs** — adequately covered by every other PM tool; not a craft gap.
- **Scrum / Kanban** — team-level, not program-level.
- **Roadmapping** — better served by dedicated products (Productboard, Aha); the writing craft is in `project-charter` and `scr-narrative`.
- **Stakeholder interviews** — a research skill, adjacent but not PM-craft.

These are all useful; they just aren't the gap this repo fills.

## Design Choices

### One skill = one artifact

A skill produces one thing well. A charter is not a RAID log is not a brief. Composition happens at the agent layer, not inside skills. This keeps each SKILL.md short enough to read and test.

### Reviewer checklists are mandatory

Every skill ends with a checklist. Without it, the skill produces output that looks right but fails quietly. The checklist is the closest thing the craft has to unit tests.

### Schemas live at the repo level, not inside skills

RAID rows, decision-memo frontmatter, and post-mortem templates are schema-validated JSON. This lets the Python helper scripts (`scripts/raid_cli.py`, `scripts/decision_journal_review.py`) manipulate them outside of the LLM path, which is both cheaper and more reliable.

### Rules are always on

`rules/common/*.md` are loaded every session. They encode the five hardest constraints: Pyramid first, MECE before lists, no buried lede, cite the method, blameless post-mortems. These are non-negotiable; the skills expand on them but don't get to override them.

### Contexts are mode switches

`contexts/pm-mode.md`, `executive-mode.md`, and `crisis-mode.md` adjust defaults (length, tone, cadence) without changing the skill set. This is how the same Pyramid skill produces a 400-word exec brief in one context and a 150-word crisis status in another.

## What Gets Worse Without This Scaffolding

A PM without this harness produces, on average:

- Briefs that bury the lede (preamble first, recommendation on page 2)
- RAID logs that accumulate open items without re-triage
- Decision memos with one option and a ratification vote
- Post-mortems that name names and produce political fiction
- Stakeholder maps where "the team" is a row

Every one of these is a known failure mode with a documented repair. The harness doesn't prevent them — it just makes the default correct.

## What Won't Get Better

The harness doesn't replace:

- Judgment about which program to run
- Relationship capital with stakeholders
- Taste in what to say yes or no to
- The career work of being trusted

The harness handles the writing craft. Everything else is still the PM's job.

## Related Bodies of Work

If this repo is useful, you may also like:

- *The Pyramid Principle*, Barbara Minto — read the grouping and summarizing chapters twice.
- *High Output Management*, Andy Grove — still the best one book for operational rigor.
- *The Field Guide to Understanding Human Error*, Sidney Dekker — everything post-mortem-facilitation borrows.
- Amazon's PR-FAQ / six-pager tradition — Bezos's 2004/2005 essays on memos over decks.
- *The Goal*, Eliyahu Goldratt — the grandfather of DMAIC thinking even if Six Sigma doesn't cite it.
