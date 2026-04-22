# everything-program-management

A structured harness and toolkit for program managers, delivery leads, chiefs of staff, and PMO-style operators.

## Status

**Incubation repo.**

This repository is being shaped as a reusable operating layer for program-management work. The intent is broad, but the standard for this repository is practical usefulness rather than breadth for its own sake. The first releases should solve repeatable day-to-day PM problems clearly and well.

## Intended scope

This repository is designed to bring together reusable assets for:

- project charters
- stakeholder maps
- decision memos
- RAID logs
- executive brief drafting
- issue triage
- DMAIC-style project structuring
- post-mortem facilitation
- milestone review preparation
- steering-committee narrative support

## Design principles

- **Operator-first**: outputs should help real PM work, not just describe PM theory
- **Reusable over ornamental**: templates and commands should be easy to adapt
- **Executive clarity**: outputs should be brief, structured, and decision-oriented
- **Auditability**: assumptions, decisions, and risks should stay traceable
- **Modular**: skills, agents, commands, and templates should work independently or together

## Planned repository layout

```text
agents/                # specialist PM agents such as executive-summary or risk-triage
commands/              # entry points for common PM workflows
skills/                # repeatable methods such as stakeholder mapping or charter drafting
templates/             # reusable templates for RAID, charters, decision memos, reviews
examples/              # worked examples showing good inputs and outputs
schemas/               # optional structured data formats for trackers and briefs
docs/                  # principles, conventions, and usage notes
```

## First high-value deliverables

The initial gold-standard milestone for this repository is:

1. a strong `AGENTS.md` entry layer
2. a small set of genuinely useful skills
3. a concise executive-summary agent
4. a risk-triage agent
5. a stakeholder-mapper skill
6. reusable templates for RAID, charter, and steering brief
7. at least two worked examples with before and after outputs

## Not yet included

This repository should not pretend to be complete before the above exists. Until then, it should be treated as an incubating toolkit rather than a finished framework.

## Quality bar

Before this repo is presented as mature, it should meet all of the following:

- clear quick-start instructions
- at least one runnable or directly usable workflow
- examples that match the documented structure
- consistent naming across agents, skills, and templates
- no placeholder sections presented as shipped capability

## Relationship to the wider portfolio

This repository complements:

- `lean-ai-ops` for structured improvement thinking
- `job-search-command-center` for execution workflows and tracking patterns
- `decision-journal-agent` for calibration and decision quality
- `ai-platform-pm-playbook` for writing-heavy PM guidance

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
