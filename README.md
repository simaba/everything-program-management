# Everything Program Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-tested-2ea44f)](.github/workflows/ci.yml)

A practitioner toolkit for producing decision-ready program artifacts: charters, RAID records, risk-review views, decision memos, stakeholder analyses, and executive briefs.

The repository combines authored methods, agent instructions, templates, worked fictional examples, JSON schemas, and a small validation CLI. Its purpose is not to generate polished management prose. Its purpose is to make assumptions, evidence, ownership, trade-offs, and follow-through easier to inspect.

## What makes the toolkit opinionated

Several rules cut across the repository:

- **Facts, estimates, assumptions, interpretations, and unknowns are different evidence classes.** Do not blend them into one confident narrative.
- **Hard constraints are not weighted criteria.** A score must not compensate for a failed legal, safety, privacy, security, or feasibility gate.
- **A decision memo needs a real option set.** Straw alternatives make the memo less trustworthy, not more complete.
- **A RAID score is an ordering aid, not expected-loss mathematics.** State change, proximity, reversibility, and control confidence still matter.
- **Power is not the only stakeholder dimension.** Impact, legitimacy, required consultation, and dissent belong in the analysis.
- **An executive brief may be a decision, exception, progress, or FYI artifact.** Do not invent an ask when none exists, and do not hide a decision inside an FYI note.
- **Public examples must be genuinely fictional.** Renaming people in an internal-looking scenario is not sufficient sanitization.

## Start with the artifact you actually need

| Need | Use | Distinctive constraint |
|---|---|---|
| Authorize or reset an initiative | [`project-charter`](skills/project-charter/SKILL.md) | outcome, non-scope, decision rights, baselines, guardrails |
| Maintain persistent uncertainty and problems | [`raid-log`](skills/raid-log/SKILL.md) | evidence, triggers, next-action owner, preserved history |
| Prepare a risk forum | [`risk-triage`](skills/risk-triage/SKILL.md) | state change, time-to-action, available lever |
| Make a consequential choice | [`decision-memo`](skills/decision-memo/SKILL.md) | real alternatives, hard gates, sensitivity, reversibility |
| Analyze participation and approval | [`stakeholder-mapping`](skills/stakeholder-mapping/SKILL.md) | authority, impact, legitimacy, evidence need, dissent |
| Brief leadership | [`executive-summary-brief`](skills/executive-summary-brief/SKILL.md) | bottom line, load-bearing evidence, uncertainty, explicit classification |
| Prepare the reader’s day or week | [`chief-of-staff-brief`](skills/chief-of-staff-brief/SKILL.md) | decisions due, material changes, leverage, removal of low-value work |

## Worked example family

The core skills use a single, clearly invented case about a fictional research-library network evaluating a metadata and archive-search pilot. The case is deliberately outside the author’s employment history and is used to show how artifacts connect:

1. the charter establishes outcome, boundaries, and evidence milestones;
2. the RAID log records uncertain conditions and current issues;
3. risk triage isolates changed items and near-term decisions;
4. stakeholder analysis identifies authority, impact, legitimate participation, and review needs;
5. the decision memo compares managed, internal, and split processing options;
6. the executive and operating briefs communicate the resulting decisions without copying the source artifacts.

The examples are teaching material, not disguised records of a real program.

## Structured validation

The bundled `pmkit` CLI currently validates:

- RAID rows stored as JSON;
- decision-memo frontmatter stored in Markdown.

```bash
python -m pip install -e .
pmkit validate raid examples/data/raid-row.json
pmkit validate decision-memo examples/data/decision-memo.md
```

Schemas are intentionally narrow. Validation confirms shape and selected semantics; it does not prove that the judgment, evidence, owner, or recommendation is correct.

## Repository map

```text
AGENTS.md              harness-neutral operating guidance
CLAUDE.md              equivalent project instructions
agents/                 orchestration wrappers around the authored skills
skills/                 methods, examples, reviewer checks, and failure modes
commands/               reusable invocation surfaces
templates/              blank artifact structures
examples/               fictional and schema-validated examples
schemas/                machine-readable contracts
src/pmkit/              lightweight validation CLI
tests/                  validator and packaged-CLI tests
rules/                  shared writing and workflow rules
```

## Quality standard for contributions

A contribution should add at least one of the following:

- a sharper decision rule or trade-off;
- a useful failure mode and repair;
- a worked example with explicit evidence classes and assumptions;
- a schema or validator that catches a meaningful defect;
- a source that changes the method rather than decorating it;
- a clearer boundary between two artifacts that are often confused.

Avoid adding another template merely because a business document has a familiar name. New artifacts should have a distinct decision purpose and reviewer contract.

## Maturity

This is a foundation release with working validation, CI, authored skill files, and connected fictional examples. It is not a project-management system of record, autonomous chief of staff, or substitute for experienced judgment.

The most valuable next work is deeper rather than broader:

- calibration and history views for recurring decisions and risks;
- richer cross-artifact linking and change provenance;
- additional schema-backed artifacts only where validation adds real value;
- more worked cases that stress disagreement, weak evidence, and changing assumptions.

## Publication safety

Do not commit real employer, customer, supplier, colleague, roadmap, contract, pricing, incident, risk, decision, stakeholder, or executive-communication material. Use invented organizations, `.example` / `.test` contact domains, and scenarios that cannot reasonably be mistaken for sanitized internal work.

## Scope

The methods and tools are practitioner aids. Adapt them to the organization, decision rights, applicable controls, and evidence available. They do not constitute project, legal, HR, procurement, financial, compliance, or employment advice.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
