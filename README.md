# Everything Program Management

<<<<<<< HEAD
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-7F52FF)

> An ECC-structured agent harness for **program managers**, not engineers.

Skills, agents, commands, and rules that codify PM craft — MECE decomposition, the Pyramid Principle, SCR executive narrative, RAID logs, stakeholder mapping, charters, DMAIC, decision memos, and post-mortems — into something a Claude Code (or Codex / Cursor / Gemini) harness can execute reliably across sessions.

Most "agent harness" repositories are dev-focused. This one isn't. It treats program management as a craft with explicit methods, and ships those methods as composable skills the harness can pull in on demand.

---

## Why This Exists

Program managers reinvent the same eight artifacts every week:

- A charter for a new initiative
- A RAID log for a stuck project
- A SCR-formatted update for an exec
- A pyramid-structured brief for a steering committee
- A stakeholder map for a contentious decision
- A DMAIC frame for a process problem
- A decision memo with options and a recommendation
- A blameless post-mortem for an incident

The frameworks are well known. The execution is consistent. The work is repetitive.

If you have an agent harness in your editor, you can codify each of these as a skill, agent, or command — and stop rebuilding them from scratch.

That's what this repo is.

---

## What's In The Box

| Surface | Count | Purpose |
|---|---|---|
| **Skills** | 12 | Self-contained methodologies (MECE, Pyramid, SCR, RAID, etc.) the harness loads on demand. |
| **Agents** | 4 | Long-running roles that compose multiple skills (chief-of-staff-brief, executive-summary, risk-triage, stakeholder-mapper). |
| **Commands** | 8 | Slash commands that trigger common PM workflows (`/charter`, `/raid-update`, `/exec-brief`, `/decision-memo`, etc.). |
| **Rules** | 7 | Always-loaded craft constraints (Pyramid first, MECE before lists, no buried lede, etc.). |
| **Contexts** | 3 | Mode switches (`pm-mode`, `executive-mode`, `crisis-mode`) for steering harness behavior. |
| **Schemas** | 3 | JSON schemas for RAID rows, decision-memo frontmatter, and post-mortem template validation. |
| **Scripts** | 2 | Tiny Python helpers for RAID log CLI and decision-journal review prompts. |

Total surface: ~36 markdown files plus thin Python tooling. No build step. No runtime risk beyond Claude Code's native skill/agent loader.

---

## Install

```bash
# Clone next to your other Claude Code repos
git clone https://github.com/<you>/everything-program-management.git
cd everything-program-management

# Add as a Claude Code plugin
./install.sh
```

Or, vendor selectively — copy any single skill into `~/.claude/skills/<name>/SKILL.md` and it works standalone. There is no required core; every skill is independent.

For Codex / Cursor / Gemini adapters, see `docs/MULTI-HARNESS.md`.

---

## Quick Tour

### Skills

| Skill | Triggered by |
|---|---|
| `mece-decomposition` | "break this problem down", "decompose", "structure this" |
| `pyramid-principle` | "structure this brief", "what's the lede", "argument tree" |
| `scr-narrative` | "exec update", "SCR", "Situation-Complication-Resolution" |
| `raid-log` | "RAID", "risks issues", "track this risk" |
| `stakeholder-mapping` | "stakeholder map", "who needs to know", "RACI" |
| `project-charter` | "charter", "kick off this project", "scope and goals" |
| `dmaic-structuring` | "process problem", "DMAIC", "Six Sigma frame" |
| `decision-memo` | "decision memo", "options doc", "make the call" |
| `post-mortem-facilitation` | "post-mortem", "retro", "what went wrong" |
| `chief-of-staff-brief` | "daily brief", "what should I focus on", "morning prep" |
| `executive-summary-brief` | "exec summary", "one-pager", "BLUF" |
| `risk-triage` | "what's at risk", "triage these risks", "what's red" |

### Agents

| Agent | When it runs |
|---|---|
| `chief-of-staff-brief` | Composes a daily PM brief across calendar + open RAID items + decisions due. |
| `executive-summary` | Takes a long doc or thread and produces a SCR + Pyramid one-pager. |
| `risk-triage` | Re-scores a RAID log against current evidence and recommends owner actions. |
| `stakeholder-mapper` | Builds a power/interest grid, RACI, and influence path for a named decision. |

### Commands

```
/charter          # New project charter from a one-line objective
/raid-update      # Add or update a RAID row with proper schema validation
/exec-brief       # SCR + Pyramid one-pager from any input
/decision-memo    # Options-with-recommendation memo
/post-mortem      # Blameless post-mortem template kickoff
/stakeholder-map  # Power/interest grid for a decision
/pyramid          # Restructure a draft into Pyramid form
/mece             # Audit a list/breakdown for MECE compliance
```

---

## Design Principles

1. **Codify methods, not opinions.** Every skill teaches a named, citable method (Minto, Ishikawa, Six Sigma, etc.). No "vibes" prompts.
2. **One skill per artifact.** A skill produces one thing well — a charter, a memo, a map. Composition happens in agents.
3. **Schemas for structure.** RAID rows, decision-memo frontmatter, and post-mortem templates are schema-validated so downstream automations can rely on them.
4. **Reusable across harnesses.** Markdown-first. No proprietary glue. Adapters live under `docs/MULTI-HARNESS.md`.
5. **No buried lede.** Every output starts with the answer. Pyramid Principle is enforced as a rule, not a suggestion.

---

## What This Is Not

- **Not a project management tool.** Use Asana, Linear, Jira. This is the agent layer that produces artifacts you put into those tools.
- **Not a coaching framework.** PMs already have Lenny, Reforge, IPDS. This is execution scaffolding for the writing-and-thinking part of the role.
- **Not a replacement for judgment.** Every skill ends with a "Reviewer Checklist" you should run before sending. The harness produces; the human signs.

---

## Project Layout

```
everything-program-management/
├── .claude-plugin/         # plugin.json, marketplace.json
├── .claude/                # commands & rules surfaced to Claude Code
├── agents/                 # 4 PM-craft agents
├── commands/               # 8 slash commands
├── contexts/               # mode switches
├── docs/                   # multi-harness, methodology references
├── examples/               # worked artifacts (RAID, charter, decision memo)
├── hooks/                  # optional hooks (charter validation, etc.)
├── manifests/              # selective install profiles
├── mcp-configs/            # optional MCP server hookups
├── rules/                  # always-loaded craft rules
├── schemas/                # JSON schemas for structured artifacts
├── scripts/                # tiny Python helpers
├── skills/                 # 12 skill folders, each with SKILL.md
└── tests/                  # validation tests
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The bar is: a new skill must teach a named method with a citation, include a Reviewer Checklist, and ship at least one worked example under `examples/`.

---

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, vendor it, sell consulting on top of it. The methods themselves (Minto, Ishikawa, Six Sigma) are not owned by anyone; the codification is.
=======
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
>>>>>>> 679dce0e0539b537c4e6d6683208a4d94edc22a0
