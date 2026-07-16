---
name: chief-of-staff-brief
description: >-
  Produce a daily or weekly operating brief that surfaces decisions due,
  material state changes, consequential meetings, and the few actions that
  deserve the user's attention. Composes RAID, decision, stakeholder, and
  calendar context without turning the result into a task dump.
  TRIGGER when: the user asks for a morning brief, weekly focus view, meeting
  preparation, or a concise answer to “what needs my attention?”
  DO NOT TRIGGER when: the user needs an executive communication, a full status
  report, or an unfiltered task list.
origin: community
---

# Chief-of-Staff Brief

A chief-of-staff brief is a prioritization layer over existing information. It should tell the reader what changed, which decisions are approaching, where their intervention has leverage, and what can safely wait.

The brief is not a digest of everything that happened. It should be intentionally incomplete.

## Selection logic

Include an item only when at least one condition is true:

- a decision or commitment is due in the brief window;
- new evidence changed the recommended action or risk state;
- the reader’s intervention can materially unblock an outcome;
- a meeting requires a position, pre-read, or negotiation choice;
- delay today creates a disproportionate downstream cost.

Exclude stable status, routine meetings, and tasks already progressing under a clear owner unless the user explicitly requests them.

## Recommended structure

```markdown
# Operating brief — [date / week]

## Bottom line
[The one changed condition or decision that should shape the reader’s attention.]

## Decisions due
| Decision | Decider | Due | Missing input | Recommended preparation |
|---|---|---|---|---|

## Material changes
| Item | Previous state | New evidence / state | Implication | Owner |
|---|---|---|---|---|

## Meetings with leverage
| Meeting | Why it matters | Position / evidence to carry | Desired outcome |
|---|---|---|---|

## First actions
1. ...
2. ...
3. ...

## Defer, delegate, or cancel
- [Item] — [reason and destination]

## Watch
- [Trigger or evidence expected; owner; date]
```

The number of items should reflect actual priority, not an arbitrary quota. A brief with no urgent item may state that directly.

## Worked example: fictional library pilot

All facts, people, and systems below are invented.

```markdown
# Operating brief — 9 September 2026

## Bottom line
The fictional Northstar Library pilot should not load another dataset until tomorrow’s deletion-control decision; protect the afternoon for that decision rather than continuing routine pilot preparation.

## Decisions due
| Decision | Decider | Due | Missing input | Recommended preparation |
|---|---|---|---|---|
| Extend or exit the managed-service pilot | Executive sponsor | Thursday 16:00 | provider root-cause note; independent retest result | Prepare a two-option memo with exit cost and residual data risk |
| Move staff onboarding by three weeks | Product owner | Friday 12:00 | revised accessibility estimate | Confirm whether the revised date preserves the year-end expansion decision |

## Material changes
| Item | Previous state | New evidence / state | Implication | Owner |
|---|---|---|---|---|
| RAID-014 deletion verification | monitoring | second failed verification test | next data load paused | Pilot owner |
| RAID-021 accessibility | remediation planned | two critical flows affected, not one | schedule estimate likely increases | Product owner |

## Meetings with leverage
| Meeting | Why it matters | Position / evidence to carry | Desired outcome |
|---|---|---|---|
| 10:00 provider review | determines whether failure is contractual, product, or integration-related | deletion timeline, test logs, exit clause | written root-cause and retest commitment |
| 15:30 sponsor check-in | decision window closes tomorrow | pilot options, cost range, unresolved controls | agree decision criteria before final memo |

## First actions
1. Ask the provider for the raw deletion-event timeline before the 10:00 review.
2. Draft the pilot extension/exit option table using measured facts and explicit assumptions.
3. Confirm the latest viable onboarding date with operations and accessibility reviewers.

## Defer, delegate, or cancel
- Routine roadmap review — delegate to the product owner; no decision or material change this week.
- Search-interface copy review — defer until the accessibility remediation path is agreed.

## Watch
- Legacy-record matching sample: data lead reports Friday; escalate only if false merges exceed the agreed tolerance.
```

## How to build the brief

1. Define the time window: today, the next business day, or the week.
2. Pull open decisions, recent state changes, high-leverage meetings, and approaching triggers.
3. Rank by consequence of delay and need for the reader’s personal intervention.
4. Separate preparation from ownership: the reader may need context without becoming the action owner.
5. Include the minimum evidence needed to enter each consequential meeting with a position.
6. Explicitly remove work through defer, delegate, or cancel choices.
7. Preserve links to source records rather than rewriting their full history.
8. State “nothing urgent” when that is the truthful result.

## Reviewer checklist

- [ ] Bottom line identifies a changed condition or decision, not generic activity.
- [ ] Every decision has a decider, date, and missing-input view.
- [ ] Material changes compare previous state with new evidence.
- [ ] Meetings are included because they have leverage, not merely because they exist.
- [ ] First actions are concrete and limited to the brief window.
- [ ] At least one defer, delegate, cancel, or explicit “none” judgment is present.
- [ ] Stable status and routine tasks are excluded.
- [ ] Source artifacts remain the authoritative record.

## Common failure modes

| Failure | Repair |
|---|---|
| Brief mirrors the calendar | Include only meetings with a decision, negotiation, or material unblock. |
| Every open risk appears | Include state changes and approaching triggers only. |
| The user becomes owner of every action | Distinguish awareness, preparation, escalation, and direct ownership. |
| “Skip” section contains low-value filler | Make a real trade-off or state that nothing should be removed. |
| Bottom line summarizes yesterday | State what today’s attention should change. |
| Brief creates facts not present in sources | Mark unknowns and request the missing input. |

## Sources

- Andy Grove, *High Output Management*, for leverage and management by exception.
- Chief-of-staff practice literature on principal attention, preparation, and decision follow-through.
- RAID, decision-log, and calendar practices adapted into a single operating view.
