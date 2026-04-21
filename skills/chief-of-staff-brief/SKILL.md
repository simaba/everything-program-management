---
name: chief-of-staff-brief
description: >-
  Produce a daily or weekly chief-of-staff brief for a program manager —
  a one-page digest that surfaces what needs attention today, which
  decisions are due, which risks have changed state, and what the user
  should walk into their first meeting already knowing. Composes the
  raid-log, stakeholder-mapping, and scr-narrative skills.
  TRIGGER when: user says "daily brief", "chief-of-staff brief", "what
  should I focus on", "morning prep", "what's on my plate", or asks for
  a single-page digest across their program.
  DO NOT TRIGGER when: user wants a status update for an exec (use
  scr-narrative or executive-summary-brief) or a list of tasks (use
  task-management).
origin: community
---

# Chief-of-Staff Brief

Produce a one-page daily or weekly brief that a PM can read in two minutes and walk into their day prepared. Written in the voice a chief of staff uses when the principal has five minutes between meetings.

## When to Use

- First thing in the morning, before calendar starts.
- Monday morning for the week ahead.
- When returning from a day out and catching up fast.
- Before a 1:1 with a sponsor who will ask "what's the status."

**Do not use** for:
- Exec briefs sent upward → use `executive-summary-brief`.
- Full program updates → use `scr-narrative`.
- Task lists → use a tracker, not prose.

## The Structure (One Page, Always)

```markdown
# Brief: [date]

## BLUF
[One sentence. The single most important thing the user should know walking into today/this week. If nothing qualifies, write "Nothing urgent; stay the course on [X]."]

## Decisions due today/this week
- [Decision] — owner: [name] — due: [date] — status: [awaiting input / signed / blocked]
- [...]

## Risks that changed state
- [Risk-id] [title] — was [status], now [status] — because [one line]
- [...]

## Meetings that matter
- [time] [attendee] — the one thing to walk in knowing: [X]
- [...]

## What to do in the first 30 minutes
1. [Specific action, named owner if it needs handoff]
2. [...]
3. [...]

## What I'd skip or defer
- [Item] — [why it can wait]
```

Total: ~20 lines of content. If it doesn't fit, the brief is failing its contract.

## How It Works

1. **Gather inputs** — RAID log, calendar, open decision memos, unread messages from priority stakeholders.
2. **Filter ruthlessly.** A brief is what the user needs *today*, not what happened yesterday. If an item isn't actionable or state-changed, it does not appear.
3. **BLUF first.** One sentence. The rule: if the principal read only this line, what's the one thing they need to know?
4. **Decisions before risks.** Decisions are what the user will be asked for; risks are what might change the decision set. Sequence matters.
5. **Meetings with a "one thing."** Every meeting gets exactly one pre-loaded fact the user should walk in with. If a meeting has no such fact, flag it for cancel/defer.
6. **First-30-minutes is three bullets maximum.** Any more and it's not triage.
7. **What I'd skip** is mandatory, not optional. A brief that only adds items and doesn't remove any is just a todo list.

## Composition With Other Skills

The chief-of-staff brief is a **composition**, not a primitive. It draws on:

- **`raid-log`** → "Risks that changed state" pulls from RAID rows whose `status` changed in the last 24h/7d.
- **`stakeholder-mapping`** → "Meetings that matter" filters the calendar to Manage-Closely + Keep-Satisfied quadrants.
- **`scr-narrative`** → BLUF is the Resolution of an implicit SCR; the brief is not the place to walk through Situation and Complication.
- **`decision-memo`** → "Decisions due" cross-references any `DM-xxxx` with `status: in_review` and `due` within the window.

## Examples

### Good BLUF

> Kenji signed off on the Japan pause last night; today's job is to rerun the regional rollout Gantt and get Maria's budget re-approval before Friday.

(Specific, names the change, names today's action.)

### Bad BLUF

> Several things are in motion across the program this week.

(Useless. Tells the user nothing.)

### Good "meeting that matters" line

> 10:30 Priya 1:1 — walk in knowing: INFRA-1204 ships tomorrow, ack'd by QA, no blockers. She'll ask.

### Bad "meeting that matters" line

> 10:30 Priya 1:1 — discuss updates.

(Discussing updates is the default; the brief's job is to pre-load the *non-default*.)

### Good "what I'd skip"

> The Tuesday design review — the decision it was called to make was already made in Slack on Monday. Suggest canceling and reading the thread.

## Reviewer Checklist

- [ ] Fits on one page (~20 content lines max).
- [ ] BLUF is one sentence and names today's action, not yesterday's event.
- [ ] Every decision has an owner and a due date.
- [ ] Every risk line shows state change (was/now), not just current state.
- [ ] Every meeting has a specific "one thing to walk in knowing."
- [ ] First-30-minutes has ≤ 3 bullets.
- [ ] "Skip or defer" section is non-empty.

## Common Failure Modes

| Failure | Repair |
|---|---|
| BLUF is vague ("lots happening") | Pick the one change that matters most since last brief. If nothing qualifies, say so. |
| Risks section is a RAID dump | Filter to state-changed items. Full log belongs in the log. |
| "Meetings that matter" lists every meeting | Manage-Closely + Keep-Satisfied + any meeting where a decision is due. That's it. |
| No "skip or defer" section | Add one. A brief that doesn't remove items isn't triaging. |
| Two pages | Cut until it fits. A second page means the brief is failing. |

## Source

- Chief of staff role literature — see [Tyler Parson's COS Handbook](https://www.chiefofstaff.co/) and [Dan Ciampa, HBR, 2020, "The Case for a Chief of Staff"](https://hbr.org/2020/05/the-case-for-a-chief-of-staff).
- Andy Grove, *High Output Management*, on leverage of information curation.
- Daily-standup and morning-kickoff patterns from Agile practice, adapted to single-principal use.
