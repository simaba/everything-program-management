# Everything Program Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)
![Program Management](https://img.shields.io/badge/focus-program%20management-1f6feb)

A structured harness toolkit for program managers, delivery leads, chiefs of staff, and PMO-style operators.

This repository packages repeatable PM work into reusable agents, skills, templates, examples, schemas, and lightweight validation utilities so the work is faster, more consistent, and easier to review.

## Status

**Foundation release.**

This repository now includes a working entry layer, core skills, specialist agents, practical templates, commands, worked examples, JSON schemas, and a small `pmkit` validation CLI. It is still early, but it is no longer an incubation placeholder.

## Choose this repo when

Use this repository when you need help producing structured PM artifacts such as:

- project charters
- RAID logs and risk updates
- executive summaries and steering briefs
- stakeholder maps
- decision memos
- daily chief-of-staff style PM briefs

Do **not** use this repository as your system of record for project execution. It is the artifact-generation and validation layer that sits beside Jira, Asana, Excel, Confluence, or similar tools.

## What is included now

| Surface | Included now | Purpose |
|---|---|---|
| **Root entry layer** | `AGENTS.md`, `CLAUDE.md` | Tells a harness or human where to start and how the repo is structured |
| **Skills** | multiple | Core methods for chartering, executive briefing, stakeholder mapping, decision memos, RAID management, and chief-of-staff briefing |
| **Agents** | 3 | Focused roles for executive summarization, risk triage, and daily PM briefing |
| **Commands** | multiple | Reusable command prompts for common PM workflows |
| **Templates** | multiple | Reusable markdown artifacts |
| **Examples** | multiple | Before-and-after examples for practical PM outputs |
| **Schemas** | 2 | JSON schemas for RAID rows and decision-memo frontmatter |
| **Utility layer** | `pmkit` CLI | Validates structured artifacts against bundled schemas |
| **Docs and rules** | included | Quickstart and always-on writing rules |

## Repository structure

```text
AGENTS.md
CLAUDE.md
agents/
commands/
docs/
examples/
rules/
schemas/
skills/
src/
templates/
tests/
```

## Included skill families

| Skill family | What it helps produce |
|---|---|
| Chartering | project charter with scope, goals, assumptions, risks, and success measures |
| Executive communication | one-page briefs, BLUF summaries, SCR narratives |
| Stakeholder alignment | stakeholder maps, influence notes, and communication strategy |
| Decision support | options memo with recommendation, rationale, and risks |
| RAID discipline | structured RAID entries and update hygiene |
| Daily operating cadence | chief-of-staff style PM briefing |

## Included agents

| Agent | Purpose |
|---|---|
| `executive-summary` | turns long material into a concise executive-ready brief |
| `risk-triage` | reviews risks and issues, re-scores them, and recommends actions |
| `chief-of-staff-brief` | composes a one-page daily PM brief from context, RAID state, and decisions due |

## Quick start

1. Read [`docs/QUICKSTART.md`](docs/QUICKSTART.md).
2. Start with [`AGENTS.md`](AGENTS.md).
3. Pick the closest command or skill for the artifact you need.
4. Use the relevant template.
5. Compare your draft to the worked examples before sending.

## Validate structured artifacts

The bundled `pmkit` CLI validates two artifact types today:

- RAID rows stored as JSON
- decision memo frontmatter stored in Markdown

Install and run:

```bash
python -m pip install -e .
pmkit validate raid examples/data/raid-row.json
pmkit validate decision-memo examples/data/decision-memo.md
```

## Design principles

- **Operator first**: outputs should help real PM work, not just describe PM theory.
- **Reusable over ornamental**: templates and methods should be easy to adapt.
- **Executive clarity**: outputs should surface the answer early.
- **Auditability**: assumptions, decisions, owners, and risks should stay traceable.
- **Honest maturity**: this repo should only claim what is actually shipped.

## Next maturity step

The next release should add:

1. richer worked examples across stakeholder maps and decision memos
2. a small formatter for RAID JSON and memo frontmatter
3. optional CSV import and export helpers for RAID data
4. CI to run `pmkit` validation tests automatically

## Relationship to adjacent repos

- `lean-ai-ops` complements this repo for process-improvement framing and DMAIC thinking.
- `decision-journal-agent` complements this repo for decision tracking over time.
- `ai-platform-pm-playbook` complements this repo with writing-heavy PM guidance.
- `job-search-command-center` applies similar operating discipline in a different workflow domain.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*