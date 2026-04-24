# Everything Program Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)
![Program Management](https://img.shields.io/badge/focus-program%20management-1f6feb)

A structured harness toolkit for program managers, delivery leads, chiefs of staff, and PMO-style operators.

This repository packages repeatable PM work into reusable agents, skills, templates, examples, and schemas so the work is faster, more consistent, and easier to review.

## Status

**Foundation release.**

This repository now includes a working entry layer, four core skills, two specialist agents, practical templates, schemas, commands, and worked examples. It is still early, but it is no longer an incubation placeholder.

## Choose this repo when

Use this repository when you need help producing structured PM artifacts such as:

- project charters
- RAID logs and risk updates
- executive summaries and steering briefs
- stakeholder maps
- decision memos

Do **not** use this repository as your system of record for project execution. It is the artifact-generation layer that sits beside Jira, Asana, Excel, Confluence, or similar tools.

## What is included now

| Surface | Included now | Purpose |
|---|---|---|
| **Root entry layer** | `AGENTS.md` | Tells a harness or human where to start and how the repo is structured |
| **Skills** | 4 | Core methods for chartering, stakeholder mapping, decision memos, and RAID management |
| **Agents** | 2 | Focused roles for executive summarization and risk triage |
| **Commands** | 4 | Reusable command prompts for common PM workflows |
| **Templates** | 5 | Reusable markdown artifacts |
| **Examples** | 4 | Before and after examples for chartering and executive updates |
| **Schemas** | 2 | JSON schemas for RAID rows and decision-memo frontmatter |
| **Docs** | 1 | Quickstart guidance |

## Repository structure

```text
AGENTS.md
agents/
commands/
docs/
examples/
schemas/
skills/
templates/
```

## Included skills

| Skill | What it helps produce |
|---|---|
| `project-charter` | project charter with scope, goals, assumptions, risks, and success measures |
| `stakeholder-mapping` | stakeholder map, influence notes, and communication strategy |
| `decision-memo` | options memo with recommendation, rationale, and risks |
| `raid-log` | structured RAID entries and update discipline |

## Included agents

| Agent | Purpose |
|---|---|
| `executive-summary` | turns long material into a concise executive-ready brief |
| `risk-triage` | reviews risks and issues, re-scores them, and recommends actions |

## Quick start

1. Read [`docs/QUICKSTART.md`](docs/QUICKSTART.md).
2. Start with [`AGENTS.md`](AGENTS.md).
3. Pick the closest command or skill for the artifact you need.
4. Use the relevant template.
5. Compare your draft to the worked examples before sending.

## Design principles

- **Operator first**: outputs should help real PM work, not just describe PM theory.
- **Reusable over ornamental**: templates and methods should be easy to adapt.
- **Executive clarity**: outputs should surface the answer early.
- **Auditability**: assumptions, decisions, owners, and risks should stay traceable.
- **Honest maturity**: this repo should only claim what is actually shipped.

## Next maturity step

The next release should add:

1. one more agent for chief-of-staff style briefing
2. structured tests or validators for template frontmatter and artifact shape
3. richer examples across decision memos and stakeholder maps
4. a small utility layer for tracker validation and formatting

## Relationship to adjacent repos

- `lean-ai-ops` complements this repo for process-improvement framing and DMAIC thinking.
- `decision-journal-agent` complements this repo for decision tracking over time.
- `ai-platform-pm-playbook` complements this repo with writing-heavy PM guidance.
- `job-search-command-center` applies similar operating discipline in a different workflow domain.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*