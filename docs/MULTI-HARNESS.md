# Multi-Harness Adapters

This plugin is built for Claude Code, but the skills, rules, schemas, and templates are pure Markdown + JSON and work across any agent harness that can read instructions from a file and call a tool. This doc covers how to install or adapt the plugin for Codex, Cursor, Gemini, and bare LLM workflows.

## Compatibility Matrix

| Harness | Skills | Agents | Commands | Rules | Schemas | Notes |
|---|---|---|---|---|---|---|
| **Claude Code** | ✅ native | ✅ native | ✅ slash | ✅ via `.claude/` | ✅ | Default target. Install with `./install.sh`. |
| **OpenAI Codex CLI** | ✅ via `AGENTS.md` | ⚠️ flatten to skills | ⚠️ map to functions | ✅ via `AGENTS.md` | ✅ | See *Codex* section below. |
| **Cursor** | ✅ via `.cursor/rules` | ⚠️ flatten | ❌ no slash equiv | ✅ as Project Rules | ✅ | See *Cursor* section. |
| **Gemini Code Assist** | ✅ as context | ⚠️ flatten | ❌ | ⚠️ system prompt | ✅ | See *Gemini* section. |
| **Bare LLM (Claude API, ChatGPT)** | ✅ paste SKILL.md | ❌ manual | ❌ manual | ✅ paste rules/ | ✅ | Useful for single-skill runs. |

## Claude Code (default)

```bash
git clone https://github.com/<you>/everything-program-management.git
cd everything-program-management
./install.sh
```

The plugin manifest at `.claude-plugin/plugin.json` registers the agents, skills, and commands automatically. Rules under `rules/common/` are surfaced via `CLAUDE.md`.

## Codex (OpenAI Agent CLI)

Codex reads `AGENTS.md` at the repo root, which is provided here as a parity shim mirroring `CLAUDE.md`.

To install:

```bash
# Vendor the plugin into your Codex working tree
git clone https://github.com/<you>/everything-program-management.git
cd everything-program-management

# Codex auto-loads AGENTS.md if present at repo root
# Skills are surfaced by file path; agents become CLI sub-commands
codex run --agent agents/chief-of-staff-brief.md
```

Notes:
- Slash commands don't translate; use `codex run --command commands/<name>.md` instead.
- Rules are loaded by Codex from `AGENTS.md`, which references `rules/common/*.md`.
- Schemas are usable directly via Codex's tool-calling.

## Cursor

Cursor's Project Rules (`.cursor/rules/*.md`) map directly onto this repo's `rules/common/`. To install:

```bash
ln -s ../rules/common .cursor/rules
```

Skills can be surfaced as Cursor "Notepad" entries — paste the SKILL.md content into a notepad and reference it via @mention in chat.

Cursor doesn't have first-class agents; use a Project Rule that says "when the user asks for a chief-of-staff brief, follow agents/chief-of-staff-brief.md."

## Gemini Code Assist

Gemini reads system instructions from a project context file. Concatenate the rules into a single `gemini-system.md`:

```bash
cat rules/common/*.md > .gemini/system-prompt.md
```

Skills work as @-referenced files in Gemini chat. Agents flatten to "operate as if you are the agent in @agents/<name>.md."

## Bare LLM

For single-shot use without a harness:

1. Pick the skill (e.g., `skills/decision-memo/SKILL.md`).
2. Paste the SKILL.md contents into a system prompt.
3. Add the relevant rules from `rules/common/`.
4. Paste your input below.
5. Run.

This is the simplest possible workflow and is how all the skills were originally validated.

## Schema Validation Across Harnesses

Schemas under `schemas/` are pure JSON Schema draft 2020-12 and validate the same way regardless of harness:

```python
from jsonschema import Draft202012Validator
import json

schema = json.load(open("schemas/decision-memo-frontmatter.json"))
Draft202012Validator(schema).validate(your_frontmatter_dict)
```

For non-Python harnesses, any JSON Schema validator (`ajv` for Node, `jsonschema` for Go, etc.) will work.

## Adapter Contract

If you build an adapter for another harness, please:

1. Preserve the rules — they are the load-bearing part of this repo.
2. Map skills to whatever per-task instruction primitive your harness has.
3. Cite the source skill in your adapter so the user can audit.
4. Open a PR adding your adapter to this matrix.
