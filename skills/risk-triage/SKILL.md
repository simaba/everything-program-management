---
name: risk-triage
description: >-
  Re-prioritize an existing risk and issue set against current evidence.
  Produces a time-to-action view, identifies what changed, and assigns one
  next action to one accountable owner. Built for recurring risk-review forums.
  TRIGGER when: the user asks what changed, what needs action now, or how to
  prepare a weekly risk review from an existing RAID log.
  DO NOT TRIGGER when: the user is creating the source RAID log or needs a
  decision-grade analysis of one issue.
origin: community
---

# Risk Triage

Risk triage is not another risk register. It is a temporary operating view that answers three questions:

1. What changed since the last review?
2. What action or decision is now time-critical?
3. Who owns that action and by when?

The value comes from state change and action timing, not from copying severity scores into a new table.

## When to use it

- weekly risk-review preparation;
- after an incident, dependency slip, or new evidence changes the program state;
- when inheriting a large RAID log and needing an actionable subset;
- before an executive brief that should show movement rather than inventory.

Do not use triage to create new RAID entries, hide unresolved ownership, or substitute urgency labels for analysis.

## Time-to-action buckets

```text
NOW         action or decision required within 24 hours
THIS WEEK   action or decision required before the weekly window closes
THIS MONTH  active treatment with a dated checkpoint this month
WATCH       no immediate lever; retain a specific recheck trigger or date
```

These are not severity bands. A severe risk can remain on watch when no decision is due and the control is functioning. A moderate issue can belong in `NOW` when it blocks a scheduled decision tomorrow.

## Triage logic

Evaluate each open item in this order:

### 1. State change

Record the new evidence, missed milestone, changed assumption, owner change, control failure, or external event. “Still high” is not a state change.

### 2. Decision or action clock

Identify the latest date by which a useful action can still change the outcome. Use that date—not anxiety—to set the bucket.

### 3. Available lever

Name the decision, mitigation, escalation, or evidence-gathering action that can move the item. Risks with no current lever normally belong in `WATCH`, with a defined trigger.

### 4. Accountable owner

Assign one person accountable for the next action. Contributors may be many; the action owner should not be “the team.”

### 5. Escalation reason

When moving an item upward, state why the existing owner or forum can no longer manage it within the required window.

## Output contract

```markdown
# Risk triage — [date]

**Source:** [RAID log or review pack]
**Review window:** [start] → [end]
**Material changes since last review:** [count]

## NOW
| ID | What changed | Decision / next action | Owner | Due | Consequence of delay |
|---|---|---|---|---|---|

## THIS WEEK
| ID | What changed | Decision / next action | Owner | Due | Escalate if |
|---|---|---|---|---|---|

## THIS MONTH
| ID | Current treatment | Owner | Next checkpoint | Evidence expected |
|---|---|---|---|---|

## WATCH
| ID | Why no action now | Recheck date or trigger | Owner |
|---|---|---|---|

## Removed from active view
- [ID] — closed / accepted / transferred / superseded — [one-line rationale]
```

## Worked example: fictional library migration

The following records are invented and do not describe a real organization or program.

### NOW

| ID | What changed | Decision / next action | Owner | Due | Consequence of delay |
|---|---|---|---|---|---|
| RAID-014 | The managed-service pilot failed two deletion-verification tests | Pause the next data load and decide whether to extend the pilot or exit | Pilot owner | 17:00 tomorrow | Restricted records could remain outside the approved retention window |

### THIS WEEK

| ID | What changed | Decision / next action | Owner | Due | Escalate if |
|---|---|---|---|---|---|
| RAID-021 | The accessibility review found keyboard-navigation defects in the search results page | Agree the remediation scope and revised pilot date | Product owner | Friday | The revised estimate moves beyond the reserved test window |
| RAID-026 | The archive team confirmed 8% of legacy records lack a stable identifier | Approve a temporary matching rule and quantify false-merge risk | Data lead | Thursday | The validation sample exceeds the agreed error tolerance |

### THIS MONTH

| ID | Current treatment | Owner | Next checkpoint | Evidence expected |
|---|---|---|---|---|
| RAID-011 | Exit-format mapping is being tested against the internal canonical schema | Platform lead | 30 September | Successful round-trip export for the representative sample |

### WATCH

| ID | Why no action now | Recheck date or trigger | Owner |
|---|---|---|---|
| RAID-008 | No recurrence of the intermittent queue delay after the configuration change | Reopen if two scheduled runs exceed the two-hour recovery objective | Operations lead |

## Capacity rules

Do not use hard caps as universal truth, but treat an overloaded top bucket as a signal that the forum has lost prioritization discipline.

A practical review should normally be able to answer:

- Which three to five items could materially change the program this week?
- Which decisions cannot wait for the next forum?
- Which items are being kept active without an owner, lever, or evidence plan?

If every item is urgent, move from routine triage to incident or recovery management and reduce the active decision set.

## Reviewer checklist

- [ ] Every `NOW` and `THIS WEEK` item names a concrete state change.
- [ ] Every active item has one next action or an explicit reason for watch status.
- [ ] Owners and dates refer to the next action, not merely the underlying risk.
- [ ] Upward moves include an escalation reason.
- [ ] `WATCH` items have a recheck trigger or date.
- [ ] Accepted and closed items are removed from the active view with rationale.
- [ ] The view is small enough for the forum to make decisions, not merely read statuses.

## Common failure modes

| Failure | Repair |
|---|---|
| Severity score determines the bucket automatically | Use time-to-action and available leverage; retain severity as context. |
| “Risk remains elevated” appears as the change | Name the new evidence or leave the item in its prior state. |
| Every item has a different contributor but no accountable owner | Assign one owner for the next move. |
| Watch has no trigger | Add the condition that reactivates the item. |
| The triage view is almost the same size as the RAID log | Remove stable items and focus on changed decisions and actions. |

## Sources

- ISO 31000, for iterative risk review and treatment.
- PMI standards and guidance on monitoring risks, issues, and responses.
- Andy Grove, *High Output Management*, for management by exception and attention to changed conditions.
