# CLAUDE.md

## Project overview

This repo contains PM-oriented agents, skills, commands, templates, and rules.

## Architecture

- `agents/`: specialized PM subagents
- `skills/`: reusable PM craft patterns
- `commands/`: command shims and entry points
- `rules/`: always-on standards for PM outputs
- `templates/`: artifact templates
- `examples/`: sample inputs and outputs

## Conventions

- Agents use markdown with YAML frontmatter.
- Skills live under `skills/<name>/SKILL.md`.
- Commands are short wrappers that invoke a skill or agent.
- Templates should be concise enough to fill in during live work.

## Quality bar

Outputs should be:
- decision-oriented
- structurally clear
- politically aware but not vague
- auditable and reusable
