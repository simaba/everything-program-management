---
name: pyramid-principle
description: >-
  Structure any written brief using Minto's Pyramid Principle — single
  governing answer at the top, MECE supporting arguments beneath,
  evidence under each. Restructures drafts that bury the lede and
  produces new briefs directly in pyramid form.
  TRIGGER when: user asks to "structure this brief", "what's the
  lede", "argument tree", "Minto", "Pyramid", or hands you a draft
  that opens with context instead of the answer.
  DO NOT TRIGGER when: user wants a SCR narrative (use scr-narrative
  — SCR is a specific *instance* of pyramid for exec updates) or a
  chronological walkthrough.
origin: community
---

# Pyramid Principle

Structure every written artifact so the reader knows the answer in the first sentence and can stop reading any time without losing the thread.

## When to Use

- Writing any brief, memo, email, or one-pager to a busy reader.
- Restructuring a draft that opens with context, history, or method.
- Preparing talking points for a meeting where you have <5 minutes.
- Turning a long document into a one-page summary.

**Do not use** for narrative storytelling (fiction, case studies), for step-by-step instructions (runbooks), or for legal/regulatory filings that require specific ordering.

## The Method

From Barbara Minto, *The Pyramid Principle* (1987). Three rules:

1. **One governing thought at the top.** The whole document answers one question. The top is the answer.
2. **Each level down supports the level above.** Every child node is a reason or piece of evidence for its parent.
3. **Siblings are MECE and ordered.** At each level, siblings are mutually exclusive, collectively exhaustive, and in logical order (time, structure, or priority).

```
                    [Governing Answer]
                           │
         ┌────────────┬────┴────┬────────────┐
         │            │         │            │
   [Argument 1] [Argument 2] [Argument 3] [Argument 4]
         │            │         │            │
      [Evidence]   [Evidence] [Evidence]  [Evidence]
```

## How It Works

### For a fresh brief

1. **Identify the question.** What is the reader actually trying to decide or learn? Write it down before you write anything else.
2. **Write the governing answer in one sentence.** If it takes two sentences, the structure isn't clear yet. Keep cutting until it's one.
3. **Brainstorm supporting arguments.** Aim for 3–4. More than 5 means you haven't grouped enough; fewer than 3 means the answer is probably trivial or wrong.
4. **Run MECE check** on the arguments (see `skills/mece-decomposition`).
5. **Order the arguments.** By time if sequential, by structure if parts-of-whole, by priority otherwise. Default to priority-descending for exec audiences.
6. **Fill in evidence.** One to three pieces per argument. Evidence is data, quotes, or prior decisions — not more claims.
7. **Draft prose.** Top = governing answer. One paragraph per argument, opening with the argument as a claim, then evidence.

### For a restructure

1. Read the existing draft. Write down the implicit governing answer — the one the author is actually trying to convey.
2. List every claim in the draft. Group into 3–4 arguments.
3. Rebuild top-down. The new draft's first sentence is the governing answer.

## Examples

### Before (buried lede)

> Last quarter we ran three pilots with the new onboarding flow. The first pilot was in APAC, the second in EMEA, and the third in Americas. APAC showed mixed results due to a translation bug that wasn't caught until week 2. EMEA was cleaner and showed a 4% lift. Americas ran the longest and showed 6%. Average activation was up meaningfully across the three, though the APAC data is noisier. We're recommending we proceed with the rollout.

### After (pyramid)

> **We should ship the new onboarding flow globally in Q3.** Three regional pilots showed an average 5% activation lift with no adverse metrics.
>
> - **Activation lift is real and consistent.** EMEA: +4%. Americas: +6%. APAC: +3% (noisy due to a translation bug; rerun with fix still positive.)
> - **No adverse metrics.** Retention, support volume, and conversion to paid were flat or positive across all three pilots.
> - **Operational readiness is in place.** Localization, rollback plan, and support-team playbook are signed off.

### Before (trivially strong)

> Prices are up in Q2. Q1 average was $12. Q2 average was $18.

### After (same content, pyramid-structured)

> **Average price rose 50% Q-over-Q, from $12 to $18.** The increase was concentrated in enterprise deals; mid-market and self-serve pricing were flat.
>
> (Subsequent paragraphs explain enterprise pricing shift.)

## Length guide

| Audience | Target length | Structure depth |
|---|---|---|
| Exec one-pager | 1 page | Governing answer + 3 arguments, one line of evidence each. |
| Steering committee | 2 pages | Governing answer + 3–4 arguments, paragraph of evidence each. |
| Deep memo | 4–6 pages | Full 3-level pyramid. |
| Board paper | 6–10 pages | Full pyramid + appendix with raw data. |

## Reviewer Checklist

- [ ] **First sentence is the governing answer.** Not context. Not method. Not history.
- [ ] **Reader can stop after any paragraph and still know the main point.**
- [ ] **Arguments are MECE.** Run `skills/mece-decomposition` check.
- [ ] **Each argument begins with a claim**, not a context-setting intro.
- [ ] **Evidence is evidence**, not restated claims.
- [ ] **Number of arguments is 3–4.** Not 7. Not 2.
- [ ] **Ordering is justified.** Time / structure / priority — and you can state which one.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Opens with "This memo covers…" | Cut the intro. First sentence is the answer. |
| Governing answer is two sentences with "however" | Pick one. Put the nuance in an argument. |
| Arguments are not parallel (one is a claim, another is a method) | Rewrite to all-claims or all-methods. Parallelism is a correctness check. |
| Evidence paragraph is another set of claims | Replace with data, quotes, or decisions. |

## Source

- Barbara Minto, *The Pyramid Principle: Logic in Writing and Thinking*, 3rd ed.
- McKinsey internal "Say it with confidence" training.
- Bezos's six-pager memo format is a pyramid in prose.
