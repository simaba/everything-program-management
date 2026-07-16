---
name: project-charter
description: >-
  Draft a concise project charter that establishes the objective, rationale,
  scope boundaries, decision rights, resources, milestones, success measures,
  and initial uncertainties. Produces a reviewable charter and a seed RAID entry.
  TRIGGER when: a new cross-functional initiative needs authorization or a stale
  initiative needs re-chartering.
  DO NOT TRIGGER when: the work is a routine task, an operating process, or a
  single unresolved decision.
origin: community
---

# Project Charter

A charter is a compact agreement about why a project exists, what outcome it owns, which boundaries apply, who can make which decisions, and what evidence will show whether the work is succeeding.

It should reduce ambiguity before detailed planning. It should not pretend that uncertain scope, estimates, or benefits are already known.

## When to use it

- a new cross-functional project needs sponsor authorization;
- an initiative has drifted and needs a reset;
- ownership or scope boundaries are disputed;
- a program is moving between phases or accountable leaders;
- a proposal needs enough definition to justify discovery funding.

A charter is not a detailed delivery plan, product requirements document, business case, or project schedule. Link those artifacts rather than compressing them into the charter.

## The core questions

| Question | Charter section | Quality test |
|---|---|---|
| What outcome are we trying to create? | Objective | states a changed condition, not only an activity |
| Why now? | Rationale | identifies the trigger, opportunity, or cost of delay |
| What is inside and outside the project? | Scope / non-scope | names boundaries that could otherwise be misunderstood |
| Who decides and who delivers? | Governance | separates sponsorship, project leadership, and work ownership |
| What must be true? | Assumptions / dependencies | records the plan’s uncertain foundations |
| What is the initial path? | Milestones | shows decision and evidence points, not every task |
| How will we judge progress and outcome? | Measures | distinguishes leading signals, outputs, and outcomes |

## Recommended structure

```markdown
# Project Charter: [Project name]

**Status:** Draft | In review | Authorized | Superseded
**Version:** 0.1
**Sponsor / authorizing owner:**
**Project lead:**
**Target authorization date:**
**Next charter review:**

## Objective
[The outcome, target population or process, and relevant time horizon.]

## Why now
[What changed; cost of delay; why this is preferable to competing uses of capacity.]

## Scope
### In scope
- ...

### Explicitly out of scope
- ...

## Decision rights and team
| Decision / responsibility | Accountable role | Contributors / reviewers |
|---|---|---|

## Milestones and evidence
| Milestone | Target | Evidence or decision produced |
|---|---|---|

## Resources and constraints
- budget / capacity envelope:
- fixed constraints:
- major dependencies:

## Measures
| Measure | Type | Baseline | Target or decision threshold | Source |
|---|---|---:|---:|---|
|  | leading / output / outcome / guardrail |  |  |  |

## Initial assumptions and risks
- Assumption:
- Validation plan:
- Top risk:
- Trigger / first response:

## Authorization and review
- decision:
- conditions:
- next review trigger or date:
```

## Measure design

Avoid treating “launch” as success. A credible charter usually includes:

- **leading measures:** evidence that the project is progressing toward the outcome;
- **output measures:** what the team will produce;
- **outcome measures:** the change the project is intended to cause;
- **guardrails:** harms, costs, or quality losses that must not be traded away.

State the baseline and measurement source where possible. When a baseline does not yet exist, make baseline discovery an early milestone rather than inventing a target.

## Worked example: fictional library search pilot

All organizations, figures, systems, and dates below are invented.

### Objective

Pilot a multilingual archive-search service across three fictional libraries so staff can locate and correct catalog records without relying on manual spreadsheet searches. The pilot should establish whether the service reduces median lookup time while preserving accessibility, data-boundary, and correction-quality guardrails.

### Why now

The library network plans to combine two archive collections next year. Current search and correction work is fragmented across local tools, and the merger estimate assumes a more consistent catalog workflow. A bounded pilot can test the assumption before a larger migration commitment.

### Scope

**In scope**

- search across a synthetic and public-safe catalog sample;
- staff correction workflow with review and rollback;
- English and one fictional second-language interface;
- accessibility, privacy, and recovery testing;
- decision package for whether to expand.

**Out of scope**

- patron-account or borrowing-history data;
- replacement of the core catalog system;
- public self-service launch;
- automated deletion or modification without staff confirmation;
- production migration of restricted archive records.

### Decision rights and team

| Decision / responsibility | Accountable role | Contributors / reviewers |
|---|---|---|
| Pilot authorization and conditions | Executive sponsor | Product, operations, privacy, accessibility |
| Technical design | Platform lead | Data and operations leads |
| Data-boundary approval | Privacy reviewer | Platform lead |
| Pilot operations | Library operations lead | Pilot-site representatives |
| Expansion recommendation | Product owner | All reviewers; sponsor decides |

### Milestones and evidence

| Milestone | Target | Evidence or decision produced |
|---|---|---|
| Baseline complete | 15 September | lookup-time baseline, error taxonomy, representative sample |
| Design review | 30 September | approved data flow, correction path, and recovery design |
| Controlled test | 31 October | accessibility, deletion, rollback, and quality results |
| Staff pilot | 30 November | observed usage, correction quality, support load |
| Expansion decision | 15 December | options memo with residual risks and cost range |

### Measures

| Measure | Type | Baseline | Pilot target / guardrail | Source |
|---|---|---:|---:|---|
| Median record lookup time | Outcome | to be measured | 30% reduction from baseline | observed task sample |
| Correction accepted without rework | Outcome | to be measured | improvement demonstrated with confidence range | reviewed corrections |
| Restricted-record exposure | Guardrail | 0 known | 0 critical events | access and audit logs |
| Keyboard-only task completion | Guardrail | not available | all critical flows complete | accessibility test |
| Support requests per pilot user | Leading | not available | tracked; no universal threshold assumed | support log |

### Initial assumption and risk

- **Assumption:** the synthetic/public-safe test sample represents the difficult legacy-record patterns well enough to inform a pilot decision.
- **Validation:** compare sample composition with the archive taxonomy before design approval.
- **Top risk:** identifier inconsistency causes false record merges.
- **Trigger:** false-merge rate exceeds the agreed sample tolerance.
- **Initial response:** disable automatic merge suggestions and route ambiguous cases to review.

## How to write the charter

1. Start with the outcome and decision horizon.
2. Name the cost of delay and competing priorities honestly.
3. Write non-scope before detailed planning; this exposes hidden expectations early.
4. Separate decision rights from team membership.
5. Use milestones as evidence and decision points, not a task list.
6. Design measures with baselines, sources, and guardrails.
7. Record the plan’s most important assumption and how it will be tested.
8. Authorize discovery with conditions when uncertainty is too high for a full commitment.
9. Set a review trigger so the charter can be superseded when material conditions change.

## Reviewer checklist

- [ ] Objective describes an outcome, not only an activity.
- [ ] Rationale includes the trigger and cost of delay.
- [ ] Non-scope addresses likely misunderstandings.
- [ ] Decision rights are explicit.
- [ ] Milestones produce evidence or decisions.
- [ ] Measures distinguish outputs, outcomes, leading signals, and guardrails.
- [ ] Baselines and sources are stated or scheduled for discovery.
- [ ] Initial assumptions have validation plans.
- [ ] The charter can be authorized with explicit conditions rather than false certainty.
- [ ] A review trigger or date is defined.

## Common failure modes

| Failure | Repair |
|---|---|
| Charter is a mini project plan | Keep authorization-level decisions; link the plan. |
| Objective begins with “build” or “implement” only | Add the intended changed condition and target user/process. |
| Success means shipping | Add outcome and guardrail measures. |
| Sponsor listed but decision rights unclear | Name which decisions the sponsor owns. |
| Exact target without baseline | Make baseline discovery an early milestone. |
| No review trigger | Add the condition or date that forces re-chartering. |

## Sources

- PMI standards and guidance on project charters and authorization.
- UK Association for Project Management guidance on project initiation and governance.
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done*, for reference-class thinking and risk realism.
