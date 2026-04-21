---
name: post-mortem
description: Kick off a blameless post-mortem template.
---

# /post-mortem

Produce a blameless post-mortem document for an incident, launch, or program outcome.

## Usage

```
/post-mortem [event name] [--severity SEV-1|SEV-2|SEV-3|SEV-4]
```

Examples:
- `/post-mortem Japan launch pause decision --severity SEV-3`
- `/post-mortem Prod deploy rollback 2026-04-18 --severity SEV-2`

## What it does

1. Invokes the `post-mortem-facilitation` skill.
2. Pulls observable events from any linked logs, monitoring dashboards, or chat-history sources (if MCP connectors are available).
3. Drafts a structured timeline from the pulled events — timestamps only, no interpretation.
4. Produces the full post-mortem template: summary, impact, timeline, what happened, contributing factors (≥3), what worked, what didn't, action items, lessons, appendix.
5. Runs the blameless-language pass — any row with a personal name in a failure context is rewritten in system terms.

## Output

Markdown file saved to `examples/post-mortems/PM-<slug>-YYYY-MM-DD.md`.

## Reviewer

The skill's Reviewer Checklist runs automatically. Hard gates: no individual names attached to failures, ≥ 3 contributing factors, every action item has type/owner/date/tracking link, 90-day follow-up scheduled.

## Rules enforced

- `rules/common/blameless-postmortem.md` — blameless language is non-negotiable.
- Action items live in the real project tracker, not only in the document.
