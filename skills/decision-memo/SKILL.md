---
name: decision-memo
description: >-
  Draft a decision memo that presents a clear question, at least two
  genuinely viable options, decision criteria, a recommendation, and
  consequences. Rejects single-option advocacy disguised as analysis and
  validates frontmatter against schemas/decision-memo-frontmatter.schema.json.
  TRIGGER when: a consequential choice has more than one reasonable path,
  the user asks for an options memo, or a decider needs a written recommendation.
  DO NOT TRIGGER when: there is no unresolved choice, the work is a routine task,
  or the decision has already been made and only needs to be logged.
origin: community
---

# Decision Memo

Write a memo that lets a named decider understand the choice, challenge the assumptions, and make the call without reconstructing the analysis from meeting history.

## When to use it

Use a decision memo when:

- two or more viable paths produce materially different outcomes;
- the decision crosses functions, budgets, or risk boundaries;
- the rationale will matter later during review, audit, or reversal;
- disagreement is partly about criteria or assumptions, not only preferences.

Do not use it for status updates, routine execution, or decisions that have already been taken. A post-decision record is a decision log, not a decision memo.

## The non-negotiable rule: expose the real option set

A memo with one viable option is a proposal. That can be legitimate, but it should not be presented as comparative analysis.

Present at least two viable options. When only one path survives a hard constraint, include a **Ruled out** section that records the alternatives, the disqualifying evidence, and who confirmed the constraint.

This distinction prevents a common failure mode: inventing weak alternatives after the preferred answer is already chosen.

## Decision-quality checks before writing

1. **Name the decider.** Consultation can be distributed; accountability for the decision cannot be vague.
2. **State the deadline and cost of delay.** A decision without a decision date quietly becomes indefinite deferral.
3. **Separate hard gates from weighted criteria.** A weighted score must not compensate for a failed legal, safety, privacy, security, or feasibility constraint.
4. **Write criteria before scoring options.** Otherwise the criteria are easily reverse-engineered around a preferred path.
5. **Record uncertainty.** Identify which numbers are measured, estimated, or assumed.
6. **Mark reversibility.** A difficult-to-reverse decision deserves stronger evidence and a higher approval threshold.
7. **Include the baseline.** “Do nothing” or “continue the current path” is often a real option and should be evaluated honestly.

## Frontmatter contract

Frontmatter validates against [`schemas/decision-memo-frontmatter.schema.json`](../../schemas/decision-memo-frontmatter.schema.json).

```yaml
---
id: DM-0012
title: "Which metadata-processing model should Northstar Library adopt?"
decider: sponsor@example.test
due: 2026-09-15
status: draft | in_review | decided | deferred | superseded
decided: null
decision: null
review_date: 2026-10-15
decision_scope: "Choose the processing model for the fictional pilot only."
linked_raid_ids: [RAID-0017]
tags: [fictional, platform-decision]
---
```

State rules enforced by the validator:

- `draft` and `in_review` keep `decided` and `decision` null;
- `decided` requires a decision date and decision value;
- `deferred` requires a non-null review date and a decision value explaining the deferral;
- `superseded` requires `supersedes: DM-####`.

## Recommended body structure

```markdown
## Decision
[One sentence. Prefer A-vs-B wording or a clearly bounded question.]

## Why now
[What changed, why a decision is required now, and the cost of delay.]

## Hard constraints
- [Constraint, source of evidence, and confirming owner]

## Criteria
| Criterion | Weight or gate | Evidence quality | Notes |
|---|---:|---|---|
|  |  | measured / estimated / assumed |  |

## Options
### Option A: [name]
- Description:
- Evidence:
- Key assumptions:
- Reversibility:
- Consequences:

### Option B: [name]
...

## Ruled out
- [Option] — [disqualifying constraint and evidence]

## Recommendation
[Recommended option, why it wins, and the most important residual risk.]

## Sensitivity and uncertainty
[Which assumption could change the recommendation? What would trigger a revisit?]

## Decision and follow-through
- Decision owner:
- Decision due:
- Immediate action if approved:
- Review trigger / review date:
```

## Worked example: fictional library metadata service

The following case is invented for this repository. The organization, costs, systems, people, and dates are fictional.

### Decision

Should the fictional **Northstar Research Library** process its public catalog metadata through a managed service, an internal platform, or a split model?

### Why now

The current overnight batch misses the 06:00 publication window on roughly one run in eight. A planned catalog expansion will double volume in six months. Deferring the decision preserves short-term flexibility but increases manual recovery work and makes the expansion date less credible.

### Hard constraints

- Patron records and access logs may not leave the library-controlled environment.
- Public bibliographic metadata may be processed externally.
- Recovery from a failed nightly run must complete within two hours.
- The annual operating envelope is capped at fictional **$125,000**.

### Criteria

| Criterion | Weight or gate | Evidence quality |
|---|---:|---|
| Data boundary | Hard gate | confirmed architecture constraint |
| 06:00 completion reliability | 30% | measured baseline; vendor result estimated |
| Three-year total cost | 25% | estimated with stated assumptions |
| Recovery time | 20% | proof-of-concept evidence |
| Exit and migration effort | 15% | architecture estimate |
| Delivery time | 10% | delivery-team estimate |

### Options

#### Option A: Managed service for all metadata

- **Cost:** $92,000/year.
- **Delivery:** six weeks.
- **Reliability:** vendor reports 99.5%; not yet verified on the fictional workload.
- **Constraint result:** fails the patron-data boundary because the current export mixes public and restricted records.
- **Reversibility:** medium; proprietary transformation rules would need to be rebuilt.

#### Option B: Build and operate internally

- **Cost:** $158,000 in year one, then $104,000/year.
- **Delivery:** sixteen weeks.
- **Reliability:** controllable, but the recovery path is not yet proven.
- **Constraint result:** passes the data boundary.
- **Reversibility:** high at the technology level, lower at the staffing level.

#### Option C: Split pipeline

Keep restricted records and orchestration internally; send only public bibliographic records to the managed processor.

- **Cost:** $121,000/year including internal operations.
- **Delivery:** ten weeks.
- **Reliability:** proof of concept completed 99 of 100 scheduled runs before 06:00; confidence remains limited by sample size.
- **Constraint result:** passes the data boundary when export classification succeeds.
- **Reversibility:** medium-high because the internal canonical format is retained.

### Ruled out

- **Continue the current batch unchanged:** does not support the planned volume and has no credible two-hour recovery path.
- **Replace the entire catalog platform:** broader than the decision and not justified by the metadata-processing problem.

### Recommendation

Choose **Option C**, subject to an independent review of the export-classification control. It is the only viable option inside the annual cost envelope that preserves the restricted-data boundary and meets the delivery window. Its main residual risk is misclassification at the internal-to-managed-service boundary.

### Sensitivity and uncertainty

The recommendation changes if either:

- the managed service cannot contractually support deletion, audit, and exit requirements; or
- the internal classification control cannot demonstrate an acceptably low rate of restricted-record leakage.

Run a larger controlled sample and complete the contract review before committing beyond the pilot.

## Reviewer checklist

- [ ] The memo names one decider and one decision date.
- [ ] The question is a single bounded choice.
- [ ] Hard constraints are separated from weighted criteria.
- [ ] At least two options are genuinely viable, or ruled-out alternatives have evidence.
- [ ] The baseline / defer option is considered where relevant.
- [ ] Every quantitative claim is marked as measured, estimated, or assumed.
- [ ] Reversibility and exit cost are explicit.
- [ ] The recommendation states the leading residual risk.
- [ ] A sensitivity or revisit trigger is documented.
- [ ] Frontmatter validates against `schemas/decision-memo-frontmatter.schema.json`.

## Common failure modes

| Failure | Repair |
|---|---|
| One strong option and two straw alternatives | Rebuild the option set or present a proposal with explicit disqualifiers. |
| Weighted average overrides a failed hard constraint | Separate gates from scored criteria. |
| Precise numbers without provenance | Mark each number measured, estimated, or assumed and cite its source. |
| Recommendation repeats the table | State why the option wins and which residual risk remains. |
| “Revisit later” with no trigger | Name the evidence, date, or threshold that reopens the decision. |

## Sources

- Barbara Minto, *The Pyramid Principle*, for answer-first written structure.
- Annie Duke, *How to Decide*, for separating decision quality from outcome quality and recording uncertainty.
- Jeff Bezos, 2015 shareholder letter, for the one-way-door / two-way-door distinction.
- Andy Grove, *High Output Management*, for decision leverage and management by exception.
