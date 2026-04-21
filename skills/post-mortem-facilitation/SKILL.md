---
name: post-mortem-facilitation
description: >-
  Facilitate a blameless post-mortem for an incident, launch, or
  program outcome. Produces a structured document with timeline,
  contributing factors, what worked, what didn't, and action items
  with owners. Enforces blameless language and uses the
  "learning review" method where possible.
  TRIGGER when: user says "post-mortem", "retro", "what went wrong",
  "incident review", "project wrap-up retro", or needs to process an
  outcome (good or bad) for learning.
  DO NOT TRIGGER when: the user wants to assign blame (redirect to
  a different forum) or is asking for a performance review (use HR
  skills, not this).
origin: community
---

# Post-Mortem Facilitation

Run a blameless post-mortem that produces a document the team will actually use — not a compliance artifact.

## When to Use

- After an incident (outage, launch failure, customer-impacting bug).
- After a completed program, successful or not.
- After a missed milestone with material impact.
- At the end of a quarter, for learning extraction even without a specific incident.

**Do not use** for:
- Performance reviews (different process entirely)
- Blame allocation (wrong tool; this is blameless)
- Status updates (use SCR)

## Blameless — The Hard Rule

**Language**: no names attached to failures. "The deploy was triggered" not "Name triggered the deploy." If an individual action contributed, the goal is to understand *why that action seemed correct at the time* — not to label the person.

**Framing**: the system failed, not the person. If a single person could have prevented the incident, the system let them.

**What this unlocks**: people report near-misses, share what they were thinking, and surface latent issues. Without blamelessness, you get political fiction.

## The Structure

```markdown
# Post-Mortem: [Event name]

**Date of event**: YYYY-MM-DD HH:MM
**Post-mortem date**: YYYY-MM-DD
**Facilitator**: Name
**Severity**: SEV-1 | SEV-2 | SEV-3 | SEV-4
**Status**: draft | in_review | final

## Summary
[1 paragraph. What happened, impact, what changed. Blameless.]

## Impact
- Users affected: [number, segment]
- Duration: [how long]
- Revenue impact: [quantified or TBD]
- Other: [SLA breach, regulatory, reputational]

## Timeline
[UTC timestamps. Only what was observable or recorded, not narrative.]

| Time (UTC) | Event |
|---|---|
| 14:03 | Deploy to prod started |
| 14:07 | First 500-error alerts fire |
| 14:08 | On-call engaged |
| 14:12 | Rollback initiated |
| 14:14 | Error rate returns to baseline |

## What Happened
[Narrative. 2-4 paragraphs. Blameless. Include what the people involved were seeing and believing at each point.]

## Contributing Factors
[Not "causes" — "factors." Incidents are multi-causal.]

1. **[Factor]** — [explanation]
2. **[Factor]** — [explanation]
3. **[Factor]** — [explanation]

## What Worked
[Be specific. Which tools, processes, or behaviors prevented this from being worse?]

- [...]
- [...]

## What Didn't Work
[Specific. System-level, not person-level.]

- [...]
- [...]

## Action Items

| Action | Type | Owner | Due | Tracking |
|---|---|---|---|---|
| [what] | prevent/detect/mitigate | name | date | ticket# |
| [...] |  |  |  |  |

## Lessons
[2-3 durable lessons the team can apply to future work.]

## Appendix
- Links to monitoring dashboards during the event
- Related RAID items
- Prior similar incidents (if any)
```

## How It Works

### Before the meeting

1. **Set the meeting as blameless** in the invite. State it explicitly.
2. **Draft the timeline** from logs, monitoring, and chat history. Timestamps only, no interpretation.
3. **Send the draft timeline to participants** 24 hours ahead, with the question "what's missing or wrong?"
4. **Invite the right people**: those directly involved, those adjacent, and one outsider to ask "why does that make sense?" questions.

### During the meeting (60–90 min)

1. **Restate blamelessness** (30 seconds).
2. **Walk the timeline** together. Fill in what people were seeing at each point.
3. **Identify contributing factors** — plural. Beware the single-root-cause trap.
4. **List what worked** — before what didn't. Sequence matters; starting negative poisons the session.
5. **List what didn't work** — system-level.
6. **Generate action items** — specific, owned, dated, trackable.
7. **Extract lessons** — durable insights beyond this one event.

### After the meeting

1. **Write up within 3 business days.**
2. **Circulate draft to participants** for fact-checking.
3. **Finalize and post** to a searchable archive.
4. **Create tickets** for action items in the normal project tracker.
5. **Schedule 90-day follow-up** to check action items actually shipped.

## Action Item Discipline

Every action item answers three questions:

1. **Type** — is this to *prevent* the class of failure, *detect* it faster next time, or *mitigate* the impact when it occurs? Aim for at least one of each; a post-mortem that only has "prevent" items is overconfident.
2. **Owner** — one human, not a team.
3. **Tracking** — ticket in the real project tracker. Action items in the post-mortem document only are action items that will not happen.

## Examples

### Good contributing factor

> **Factor**: Deploy pipeline did not require acknowledgment of the "schema migration flagged" warning; the engineer saw the warning, judged it non-blocking based on the green CI status, and proceeded. No system-level enforcement existed.

### Bad contributing factor

> **Factor**: Name ignored the warning.

(Blames the individual; tells you nothing about the system.)

### Good action item

> Require schema-migration warnings to block the deploy until manually ack'd with a written justification.
> - Type: prevent
> - Owner: priya@example.com
> - Due: 2026-05-15
> - Tracking: INFRA-1204

### Bad action item

> Be more careful with schema migrations.
> - Owner: the team

(Not actionable, not owned, will not happen.)

### Good "what worked" item

> Automated rollback triggered by error rate threshold worked as designed, limiting customer impact to 7 minutes.

### Bad "what worked" item

> The team handled the incident well.

(Not specific enough to replicate.)

## Reviewer Checklist

- [ ] No individual names attached to failures. Names only appear in "who did the good work" contexts.
- [ ] Timeline is factual (timestamps and events), not narrative.
- [ ] Contributing factors are plural (at least 3). Single-root-cause analyses are a red flag.
- [ ] "What worked" section is non-empty and specific.
- [ ] "What didn't work" is system-level, not person-level.
- [ ] Each action item has type (prevent/detect/mitigate), named owner, date, and tracking link.
- [ ] 90-day follow-up is scheduled to check action items.
- [ ] Document is published in a searchable archive, not just shared as a Google Doc link.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Blame language ("Name should have…") | Rewrite in system terms: "The system did not require…" |
| Single root cause | Ask "why does that cause exist?" recursively; surface the contributing web. |
| Only "prevent" action items | Ask: how would we detect this next time? How would we reduce blast radius? |
| Action items live only in the doc | Create tickets in the project tracker. Track as tickets, not as doc paragraphs. |
| No 90-day follow-up | Schedule one now; most action items silently die at ~45 days without it. |
| Facilitator was in the blast radius | Ideally an outsider; if not, acknowledge the bias explicitly. |

## When to Pick a Variant

- **Learning Review** (Sidney Dekker / resilience engineering) — same principles, sharper focus on what people were thinking during the event. Use when the incident involved a judgment call.
- **5-Whys** — useful within the Contributing Factors section; not sufficient on its own for complex incidents.
- **Cynefin-informed PM** — for incidents in complex (not complicated) domains, be explicit that root causes may not generalize.

## Source

- Google SRE book, chapter on postmortems.
- Etsy's "Blameless PostMortems and a Just Culture" (Allspaw, 2012).
- Sidney Dekker, *The Field Guide to Understanding Human Error* — the canonical reference.
- John Allspaw's "Learning Review" writeups.
- NTSB-style aviation accident investigations as the gold standard of blameless analysis.
