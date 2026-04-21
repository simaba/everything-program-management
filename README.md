# Everything Program Management

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
