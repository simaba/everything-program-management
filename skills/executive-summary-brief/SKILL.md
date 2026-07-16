---
name: executive-summary-brief
description: >-
  Produce a concise executive brief that opens with the decision, recommendation,
  or material change; supports it with the smallest sufficient evidence set; and
  ends with a clear action or FYI classification. Uses answer-first structure
  without forcing every situation into the same number of sections or bullets.
  TRIGGER when: a long source needs a decision-ready leadership summary.
  DO NOT TRIGGER when: the user needs a multi-option decision memo, a detailed
  status report, or a daily personal operating brief.
origin: community
---

# Executive Summary Brief

An executive brief is an attention-allocation instrument. Its job is to let a reader understand what changed, why it matters, what judgment is being recommended, and what action—if any—is required.

It is not a compressed transcript. It should preserve the decision-relevant evidence and uncertainty while removing chronology, meeting detail, and decorative context.

## Choose the brief type first

| Type | Lead with | End with |
|---|---|---|
| **Decision brief** | recommendation and decision deadline | explicit decision ask |
| **Exception brief** | material variance or control failure | intervention or escalation needed |
| **Progress brief** | outcome achieved or forecast change | next milestone / no action required |
| **FYI brief** | important fact and implications | explicit “no decision requested” |

Do not manufacture an ask when the appropriate classification is FYI. Conversely, do not label an unresolved decision as FYI to avoid naming the decider.

## Information hierarchy

A strong brief usually contains:

1. **Bottom line:** decision, recommendation, or material change.
2. **Stakes:** consequence of action, delay, or inaction.
3. **Load-bearing evidence:** the few facts that support the bottom line.
4. **Uncertainty and risk:** what is not known and what could change the recommendation.
5. **Action:** named owner, decision, date, and immediate follow-through—or a clear statement that no action is requested.

Use headings that fit the situation. “Exactly three supporting points” and “exactly one page” can be useful editing constraints, but they are not substitutes for judgment. The brief should be as short as possible without omitting material evidence or caveats.

## Recommended structure

```markdown
# [Decision or material change]

**To:** [reader / decision owner]
**From:** [author]
**Date:** [date]
**Classification:** Decision | Exception | Progress | FYI

## Bottom line
[One or two sentences: recommendation, decision, or material change.]

## Why it matters now
[Stakes, timing, and cost of delay or inaction.]

## Evidence
- [Fact, source, and implication]
- [Fact, source, and implication]

## Uncertainty and risks
- [Uncertainty or residual risk; mitigation / evidence plan]

## Action
[Decision or action, accountable owner, and date. If FYI, state “No action requested.”]

## Sources
- [Links to decision memo, RAID log, analysis, or report]
```

## Worked example: fictional library pilot

All facts, organizations, dates, and amounts below are invented.

### Good decision brief

```markdown
# Delay the archive-search pilot three weeks

**To:** Executive sponsor
**From:** Product owner
**Date:** 8 September 2026
**Classification:** Decision

## Bottom line
Delay the fictional Northstar Library pilot by three weeks and use the reserved window to remediate accessibility and deletion-verification failures. The delay adds an estimated $45,000 in project cost but avoids beginning staff onboarding with two unresolved control defects.

## Why it matters now
The pilot onboarding schedule becomes difficult to change after Friday because training and site coverage are booked. Proceeding on the current date would either exclude keyboard-only users from critical tasks or require a manual data-deletion process that has not been independently verified.

## Evidence
- Accessibility testing found that two critical correction flows cannot be completed without a pointer device; remediation is estimated at eight working days.
- Two of twelve deletion-verification cases remained discoverable beyond the documented interval; the cause is not yet isolated.
- The three-week delay preserves the year-end expansion decision date if retesting passes by 30 September.

## Uncertainty and risks
- The deletion defect may be provider-specific rather than integration-specific. A joint log review is scheduled tomorrow.
- The cost estimate excludes a second accessibility-review cycle; finance has reserved a $15,000 contingency.

## Action
Approve the revised pilot date by 12:00 Friday and authorize the product owner to cancel the pilot if either control remains unresolved at the 30 September readiness review.
```

### Weak version

> The pilot has encountered several challenges and the team has been working cross-functionally to evaluate options. Leadership feedback would be appreciated.

This version hides the recommendation, omits evidence and timing, and does not identify a decision owner.

## How to produce the brief

1. Identify the decision, exception, progress change, or FYI classification.
2. Write the bottom line before the context.
3. Trace each supporting claim to a source or accountable owner.
4. Remove chronology unless sequence changes the judgment.
5. Quantify stakes with ranges and assumptions rather than invented precision.
6. Include the uncertainty most likely to change the recommendation.
7. Name the action and deadline, or state clearly that no action is requested.
8. Link the underlying artifacts so the brief does not become the only record.

## Reviewer checklist

- [ ] The brief type is explicit.
- [ ] The first paragraph contains the decision, recommendation, or material change.
- [ ] Stakes include timing and consequence of delay or inaction.
- [ ] Evidence is factual, sourced, and load-bearing.
- [ ] Estimates and assumptions are distinguishable from measured facts.
- [ ] Material uncertainty is visible.
- [ ] The action names an owner and date, or the brief states no action is requested.
- [ ] Source artifacts are linked.
- [ ] The brief is concise without deleting decision-relevant caveats.

## Common failure modes

| Failure | Repair |
|---|---|
| The brief begins with meeting history | Start with the judgment or changed condition. |
| “Leadership feedback requested” | Name the actual decision, decider, and deadline. |
| Precise cost or forecast with no assumptions | Use a range and cite the model or owner. |
| Risk section lists generic concerns | Include the uncertainty that could change the recommendation. |
| FYI note contains a hidden approval request | Reclassify it as a decision brief. |
| Compression removes dissent or control failures | Preserve material evidence even when it complicates the narrative. |

## Sources

- Barbara Minto, *The Pyramid Principle*, for answer-first structure.
- U.S. military BLUF writing traditions, for decision-relevant opening statements.
- Andy Grove, *High Output Management*, for management attention and exception-based reporting.
