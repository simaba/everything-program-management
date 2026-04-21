---
name: decision-memo
description: >-
  Draft a decision memo — a structured document that presents a
  question, ≥2 viable options, evaluation criteria, a recommendation,
  and the consequences of each path. Enforces the "no single-option
  memo" rule and surfaces ruled-out options explicitly. Output
  validates against schemas/decision-memo-frontmatter.json.
  TRIGGER when: user says "decision memo", "options doc", "make the
  call", "we need to decide X", or describes a pending decision that
  has more than one reasonable path.
  DO NOT TRIGGER when: there is no real decision pending (use a
  status update) or the decision is purely operational and has no
  strategic tradeoff (use a task).
origin: community
---

# Decision Memo

Draft a one- to three-page memo that presents a decision, the real options, the criteria, a recommendation, and the consequences — in a form a busy decider can act on without a meeting.

## When to Use

- A decision is pending that involves a tradeoff (cost vs speed, scope vs quality, build vs buy).
- The deciding stakeholder isn't in every working-group meeting and needs a briefing to decide.
- You want a written artifact that preserves the rationale for a future post-mortem or audit.
- You are proposing something that will be controversial; a written memo depersonalizes the discussion.

**Do not use** for status updates (use SCR), for single-path operational tasks (use a ticket), or for decisions already made (use a decision *log*, not a memo).

## The Hard Rule: ≥2 Options

A memo with one option is not a decision memo; it is a pitch. If you believe only one option is viable, write that explicitly and document what was ruled out. The rule:

> If you present fewer than 2 viable options, you must include a "Ruled Out" section listing ≥2 alternatives you considered and why they failed to qualify. No exceptions.

This prevents the most common failure mode: the author has already decided and is performing option analysis for the record.

## Structure

```markdown
---
id: DM-0012
title: "Should we pause Japan launch given the regulatory delay?"
decider: david@example.com
due: 2026-05-10
status: draft | in_review | decided | deferred
decided: null | 2026-05-08
decision: null | "Option B"
---

## Question
[One sentence. A yes/no or A-vs-B framing if possible.]

## Context
[2-3 sentences. What's the baseline? What changed?]

## Criteria
[3-5 criteria we will use to evaluate options. Weighted if appropriate.]

## Options

### Option A: [name]
[Description, 2-3 sentences.]
- **Cost**: [quantified]
- **Speed**: [quantified]
- **Risk**: [quantified]
- **Reversibility**: [one-way / two-way door]

### Option B: [name]
[...]

### Option C: [name]  (optional, 3rd option)
[...]

## Ruled Out
- [Option we considered and rejected] — [reason]
- [Option we considered and rejected] — [reason]

## Recommendation
[One paragraph. State the recommended option and the single most important reason.]

## Consequences
- **If A**: [what happens, including second-order effects]
- **If B**: [...]
- **If C**: [...]

## Asks
[What the decider needs to do: sign the memo, schedule a discussion, approve budget, etc. Be explicit.]

## Open Questions
[If any remain. Leaving this blank is suspicious — most decisions have residual uncertainty.]
```

## How It Works

1. **Sharpen the question.** One sentence, ideally yes/no. If it takes three sentences, you have multiple decisions; split them.
2. **Write the criteria before the options.** Criteria written after options tend to be reverse-engineered to justify a preferred choice.
3. **Brainstorm ≥4 options**, then filter to ≥2 that are genuinely viable. Put the others in "Ruled Out."
4. **Quantify each option** on the criteria. "Cost: $38K/Q" not "Cost: moderate."
5. **Mark reversibility explicitly** (one-way door vs two-way door — Bezos's framing). This drives the decision threshold.
6. **Make the recommendation.** Not a summary of the options — a stance.
7. **State consequences** of each path, including the second-order effects decision makers often miss.
8. **State the ask** concretely: sign, approve, discuss.
9. **Validate frontmatter** against `schemas/decision-memo-frontmatter.json`.
10. **Log the decision** after it's made by updating `decided`, `decision`, and archiving.

## Example

```markdown
---
id: DM-0014
title: "Should we run VoxOS China LLM intent classifier on-device or in-cloud?"
decider: priya@example.com
due: 2026-05-20
status: draft
---

## Question
Should the VoxOS China voice-assistant intent classifier run on-device (NPU) or in the regional cloud?

## Context
Current voice-assistant stack routes all utterances to cloud. Latency p95 is 480ms; target is ≤ 300ms. NPU compute on the target SoC is sufficient for a 700M-param model. Cost structure differs materially between the two paths.

## Criteria
1. **Latency (p95)** — target ≤ 300ms
2. **Accuracy** — target ≥ 92% top-1 on China test set
3. **Cost per vehicle per year** — target ≤ $4
4. **Privacy** — in-cabin audio sensitivity
5. **Update velocity** — how quickly we can ship model improvements

## Options

### Option A: Cloud-only (status quo)
- Latency: 480ms p95 (misses target by 180ms)
- Accuracy: 94.1% (exceeds target)
- Cost: $2.80/veh/yr (exceeds target, favorable)
- Privacy: Audio egresses vehicle → regional cloud; regulatory exposure under PRC PIPL
- Update velocity: Weekly (fast)
- Reversibility: Two-way door

### Option B: On-device only
- Latency: 120ms p95 (exceeds target)
- Accuracy: 91.3% (misses target by 0.7pt on current model)
- Cost: $0.40/veh/yr (strongly favorable)
- Privacy: Audio stays on vehicle; PIPL exposure minimal
- Update velocity: OTA-bound, 4–6 week cycles
- Reversibility: One-way door (binds SoC choice for 3+ years)

### Option C: Hybrid — on-device for top 80% of intents, cloud for tail
- Latency: 180ms p95 for on-device path, 480ms for cloud fallback
- Accuracy: 93.7% blended
- Cost: $1.10/veh/yr
- Privacy: ~85% of utterances stay on-device
- Update velocity: On-device monthly, cloud weekly
- Reversibility: Two-way door (can tune split)

## Ruled Out
- Third-party voice platform — evaluated and rejected; doesn't meet PIPL data-residency requirements for audio.
- Federated learning — too early; infrastructure not ready this planning cycle.

## Recommendation
**Option C (hybrid)**. It is the only option that meets all five criteria, preserves two-way-door optionality, and lets us ship improvements quickly via the cloud path while moving the bulk of traffic on-device.

## Consequences
- **If A**: Miss latency target; continued PIPL exposure; no cost benefit. Likely triggers regulatory inquiry by Q4.
- **If B**: Meet latency; accept 0.7pt accuracy drop (possibly addressable via QAT); lock in SoC choice; slow shipping cadence.
- **If C**: Hit all targets. Added complexity in routing layer (1 eng-month) and a second accuracy model to maintain. Cloud fallback means PIPL exposure reduced but not eliminated.

## Asks
- Priya: sign by May 20 or flag concerns in #program-voxos-china.
- Finance: confirm $1.10/veh/yr cost can be absorbed in the revised gross-margin model.
- Legal: confirm hybrid path satisfies PIPL guidance (Marcus has a draft opinion).

## Open Questions
- Can we close the 0.7pt accuracy gap with quantization-aware training in-cycle? (Owner: Chen; answer by May 15)
- If not, is 93.7% (hybrid) acceptable or do we need 94%+? (Owner: Priya decision in-memo)
```

## Reviewer Checklist

- [ ] Question is one sentence.
- [ ] Context fits in 3 sentences.
- [ ] Criteria are written before options and are not reverse-engineered.
- [ ] ≥ 2 options, or an explicit "Ruled Out" section.
- [ ] Every option is quantified on every criterion.
- [ ] Reversibility is marked (one-way vs two-way).
- [ ] Recommendation is a stance, not a summary.
- [ ] Consequences include second-order effects.
- [ ] Asks are concrete and addressed to named people.
- [ ] Frontmatter validates against `schemas/decision-memo-frontmatter.json`.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Single-option memo | Add a "Ruled Out" section or find the real second option. |
| Options differ on 8 criteria, all of which favor one | Criteria were reverse-engineered. Pick 3–5 criteria *before* re-scoring. |
| Recommendation summarizes the options | Take a stance. If you can't, the author isn't the right decision-owner. |
| No consequences section | Add it. The decider needs second-order effects, not just first-order. |
| "We'll revisit in 3 months" as the recommendation | Deferral is a legitimate choice; state it as "Option D: defer, with criteria for revisit." |

## Source

- Jeff Bezos, 2015 letter to shareholders — one-way vs two-way doors framing.
- Amazon's internal six-pager / PR-FAQ culture — memos over decks.
- Alex Komoroske's memo on decision-making; Shreyas Doshi's writing on PM decision quality.
- Andy Grove, *High Output Management* — "staff meetings" decision framing.