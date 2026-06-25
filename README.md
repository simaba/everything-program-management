# Everything Program Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)
![Program Management](https://img.shields.io/badge/focus-program%20management-1f6feb)

A structured harness toolkit for program managers, delivery leads, chiefs of staff, and PMO-style operators.

This repository packages repeatable PM work into reusable agents, skills, templates, examples, schemas, and lightweight validation utilities so work is faster, more consistent, and easier to review.

## Maturity

**Foundation release.**

The repository includes a working entry layer, core skills, specialist agents, practical templates, commands, worked examples, JSON schemas, a small `pmkit` validation CLI, and automated CI checks for the packaged utility layer.

It is early, but it is no longer an incubation placeholder.

### Public release materials

- [Public Release Checklist](docs/PUBLIC_RELEASE_CHECKLIST.md): final repository/history/Actions review before visibility changes.
- [Draft v0.1.0 release notes](docs/releases/v0.1.0.md): intended published scope and release record.
- [Changelog](CHANGELOG.md): user-visible version history.

## Purpose

Use this repository when you need help producing structured PM artifacts such as:

- project charters
- RAID logs and risk updates
- executive summaries and steering briefs
- stakeholder maps
- decision memos
- daily chief-of-staff style PM briefs

This is not a system of record for project execution. It is an artifact-generation and validation layer that sits beside Jira, Asana, Excel, Confluence, or similar tools.

## Publication safety

Use fictional, generic, or fully sanitized examples in this repository.

Do not publish:

- real employer, customer, vendor, supplier, or colleague information
- confidential project names, roadmaps, escalations, or delivery risks
- internal steering materials or executive communications
- real RAID logs, decision memos, or stakeholder maps
- private performance, HR, legal, procurement, or financial information
- non-public product details, architecture, defects, launch gates, or audit findings

## Current capabilities

| Surface | Included | Purpose |
|---|---|---|
| **Root entry layer** | `AGENTS.md`, `CLAUDE.md` | Tells a harness or human where to start and how the repository is structured |
| **Skills** | multiple | Core methods for chartering, executive briefing, stakeholder mapping, decision memos, RAID management, and chief-of-staff briefing |
| **Agents** | 3 | Focused roles for executive summarization, risk triage, and daily PM briefing |
| **Commands** | multiple | Reusable command prompts for common PM workflows |
| **Templates** | multiple | Reusable markdown artifacts |
| **Examples** | multiple | Worked fictional examples and validated example data |
| **Schemas** | 2 | JSON schemas for structured RAID rows and decision-memo frontmatter |
| **Utility layer** | `pmkit` CLI | Validates structured artifacts against bundled schemas |
| **Automation** | CI workflow | Runs tests and validates bundled example artifacts automatically |
| **Docs and rules** | included | Quick-start guidance and always-on writing rules |

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
.github/workflows/
```

## Skill families

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
5. Compare your draft to the fictional worked examples before sending.

## Validate structured artifacts

The bundled `pmkit` CLI validates two artifact types today:

- RAID rows stored as JSON
- decision-memo frontmatter stored in Markdown

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
- **Honest maturity**: this repository should only claim what is actually shipped.
- **Public-safe examples**: examples should teach structure without exposing private work.

## Roadmap

The next release should add:

1. richer worked examples across stakeholder maps and decision memos
2. a small formatter for RAID JSON and memo frontmatter
3. optional CSV import and export helpers for RAID data
4. one additional structured schema for charter frontmatter or executive briefs
5. broader publication-safety review before any real artifact is adapted into an example

## Related repositories

- `lean-ai-ops` complements this repository with process-improvement framing and DMAIC thinking.
- `decision-journal-agent` complements this repository with decision tracking over time.
- `ai-platform-pm-playbook` complements this repository with AI platform PM guidance.
- `governance-playbook` complements this repository with AI governance operating-model design.

## Scope and disclaimer

This repository is shared in a personal capacity. It is not project, legal, HR, procurement, financial, compliance, or employment advice.

The templates, agents, and skills are practitioner aids. Adapt them to your organization, project context, stakeholders, governance model, and review process before use.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*