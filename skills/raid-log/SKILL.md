---
name: raid-log
description: >-
  Maintain a RAID log for risks, assumptions, issues, and dependencies with
  owner, date, evidence, and action discipline. Validates structured rows
  against schemas/raid-row.json and supports weekly review and archival.
  TRIGGER when: the user needs a RAID log, risk register, assumption record,
  issue entry, dependency record, or structured program-risk artifact.
  DO NOT TRIGGER when: the user needs a decision memo or a temporary triage view.
origin: community
---

# RAID Log

A useful RAID log is a decision-support record, not a warehouse for every concern ever mentioned. Each row should preserve enough context to answer: what is uncertain or wrong, why it matters, what evidence would change our view, and who is responsible for the next move.

## The four record types

| Type | Definition | Minimum decision value |
|---|---|---|
| **Risk** | A future event or condition that may affect objectives | trigger, response, owner, review date |
| **Assumption** | An unverified belief the plan depends on | validation method, owner, deadline |
| **Issue** | A condition already affecting delivery or outcomes | containment/fix, owner, ETA |
| **Dependency** | An external input, decision, or deliverable required for progress | provider, need-by date, blocked work |

When a risk occurs, close or supersede the risk record and create an issue. Do not silently change its meaning while preserving the old score and history.

## Row contract

Each structured row validates against `schemas/raid-row.json`.

```yaml
id: RAID-0042
kind: risk | assumption | issue | dependency
title: "One-line statement of the condition or event"
description: "Context, affected objective, and why this belongs in the log"
category: scope | schedule | cost | quality | resource | external
owner: owner@example.test
opened: 2026-09-01
due: 2026-09-15 | null
status: open | monitoring | closed

# Risk fields
probability: 1-5
impact: 1-5
score: probability * impact
mitigation: "Action intended to reduce probability or impact"
trigger: "Observable condition that changes the response"

# Assumption fields
validation_plan: "Evidence, method, owner, and deadline"

# Issue fields
fix_plan: "Containment and resolution plan"
eta: 2026-09-12

# Dependency fields
provider: provider@example.test | team-name
blocks: [RAID-0012]
```

Use the exact field names defined by the schema in the repository. The example above illustrates the information model; the validator remains the source of truth for accepted keys.

## Scoring discipline

Probability and impact scores are ordinal judgments, not precise arithmetic. Multiplying them can help sort a review list, but it does not produce a calibrated estimate of expected loss.

Record the rationale behind material score changes. For important risks, add qualitative context that a number cannot capture:

- proximity: how soon the event could occur;
- detectability: whether warning is likely before impact;
- reversibility: whether recovery is practical;
- concentration: whether one event affects several objectives;
- control confidence: whether the mitigation is tested or merely planned.

Never allow a medium numeric score to hide a failed non-negotiable constraint or a low-probability catastrophic outcome.

## How to create a record

1. **Classify the record.** Future uncertainty, unverified belief, current problem, or external dependency?
2. **Tie it to an objective.** Explain what scope, milestone, quality bar, budget, or outcome is affected.
3. **Assign the next-action owner.** A functional team may contribute, but one person should own the next move.
4. **Define evidence.** State what would increase, decrease, validate, close, or convert the record.
5. **Set a review clock.** Use a due date, trigger, or checkpoint appropriate to the item.
6. **Avoid false precision.** Mark estimates and uncertain dates as such.
7. **Preserve history.** Close or supersede records; do not delete the rationale.

## Weekly review

Review changes, not every line equally.

- Reclassify assumptions that have been validated or disproved.
- Convert occurred risks into issues with explicit links.
- Re-score only when evidence or time horizon changed.
- Close stale records that no longer affect an objective.
- Challenge items with no owner action, evidence plan, or review trigger.
- Move time-critical items into the `risk-triage` view for action sequencing.

## Worked examples: fictional library migration

All entities, facts, dates, and quantities below are invented.

```yaml
- id: RAID-0017
  kind: risk
  title: "Legacy records may not map cleanly to the canonical identifier"
  description: "A sample found inconsistent identifiers in older archive records. A high false-merge rate would undermine the planned catalog migration."
  category: quality
  owner: data-lead@example.test
  opened: 2026-09-02
  due: 2026-09-12
  status: monitoring
  probability: 3
  impact: 4
  score: 12
  mitigation: "Run a stratified validation sample and route ambiguous records to a review queue."
  trigger: "False-merge rate exceeds the agreed sample tolerance."

- id: RAID-0018
  kind: assumption
  title: "Accessibility review can complete within the pilot window"
  description: "The plan assumes the independent accessibility review finishes before pilot onboarding begins."
  category: external
  owner: product-owner@example.test
  opened: 2026-09-03
  due: 2026-09-10
  status: open
  validation_plan: "Reviewer confirms scope, availability, and written completion date by 10 September."

- id: RAID-0019
  kind: issue
  title: "Deletion verification failed in the managed-service sandbox"
  description: "Two test records remained discoverable after the documented deletion interval. The next data load is paused."
  category: quality
  owner: pilot-owner@example.test
  opened: 2026-09-07
  due: 2026-09-09
  status: open
  fix_plan: "Contain the pilot, obtain provider logs, repeat the test with an independent observer, and decide whether to exit the pilot."
  eta: 2026-09-09

- id: RAID-0020
  kind: dependency
  title: "Security review required before restricted-record testing"
  description: "The test environment cannot receive restricted sample records until the security review confirms the approved access pattern."
  category: external
  owner: platform-lead@example.test
  opened: 2026-09-04
  due: 2026-09-14
  status: open
  provider: security-review@example.test
  blocks: [RAID-0017]
```

## Reviewer checklist

- [ ] The record type matches the actual condition.
- [ ] The affected objective is clear.
- [ ] One person owns the next action.
- [ ] Risks have a trigger and response, not only a score.
- [ ] Assumptions have a validation method and date.
- [ ] Issues distinguish containment from permanent resolution.
- [ ] Dependencies identify the provider, need-by date, and blocked work.
- [ ] Score changes cite new evidence or time-horizon changes.
- [ ] Closed records preserve resolution rationale.
- [ ] The active log remains small enough to review meaningfully.

## Anti-patterns

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| “Schedule risk” with no event or trigger | Cannot be observed or acted on | Name the event, affected milestone, trigger, and response. |
| Team as owner | Accountability for the next action is unclear | Assign one accountable person and list contributors separately. |
| Every risk scores 9 or 12 | Scoring has become ritual | Revisit definitions and record the rationale for material items. |
| Score treated as expected-loss mathematics | Ordinal scales do not support that precision | Use score for rough ordering and add qualitative dimensions. |
| Hundreds of open rows | The log stops supporting decisions | Archive resolved records and maintain a separate triage view. |
| Issue has only a final fix | Immediate containment is missing | Separate containment, diagnosis, correction, and verification. |

## Sources

- PMI standards and practice guidance on project risk and issue management.
- ISO 31000, for risk identification, analysis, treatment, monitoring, and review.
- Douglas Hubbard, *The Failure of Risk Management*, for cautions about ordinal risk matrices and false precision.
