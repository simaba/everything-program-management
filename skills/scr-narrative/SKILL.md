---
name: scr-narrative
description: >-
  Construct executive updates in Situation–Complication–Resolution
  (SCR) form. Takes a situation + what changed + what you propose and
  produces a one-paragraph or one-page brief that leads with tension
  and resolves it. Method: Minto (SCR is the top-of-pyramid narrative
  hook).
  TRIGGER when: user asks for "exec update", "SCR", "Situation
  Complication Resolution", "board update", "status narrative", or
  needs to frame a change that requires leadership attention.
  DO NOT TRIGGER when: the user wants a general pyramid-structured
  brief without tension (use pyramid-principle), or a RAID risk row
  (use raid-log).
origin: community
---

# SCR Narrative

Frame an executive update as a three-beat story: **Situation → Complication → Resolution**. Leads with what the reader already knows, introduces what changed, and proposes what to do.

## When to Use

- Weekly / monthly program update to a leadership team.
- Any brief where the reader needs to know "why am I reading this now?" — SCR answers it.
- Opening paragraph of a larger memo (SCR sits on top of a Pyramid).
- Re-framing bad news so the response is structural, not emotional.

**Do not use** when there's no genuine complication (use a plain status update), or when the complication is minor and a RAID row is sufficient.

## The Method

From Barbara Minto's *Pyramid Principle*, chapter on introductions. Every executive narrative has three parts, in this order:

1. **Situation** — a single sentence the reader already believes. Common ground. Not controversial.
2. **Complication** — what has changed, what's new, what's at stake. This is the *reason* the reader is reading.
3. **Resolution** — the governing answer that the rest of the document supports.

The complication creates the "question in the reader's mind" that the resolution answers. If the complication doesn't create a question, you don't have SCR — you have a list of facts.

### Template

```
[Situation: one sentence stating the baseline the reader accepts.]
[Complication: one to two sentences stating what changed and why it matters.]
[Resolution: one to two sentences stating what we propose or decided.]
```

## How It Works

1. **Write the situation.** What does the reader already believe about this program? If your situation sentence surprises the reader, it's actually the complication; move it down.
2. **Write the complication.** What specifically changed? Be concrete: a metric crossed a threshold, a dependency slipped, a stakeholder asked for a decision, a regulation is now in force.
3. **Write the resolution.** What do you propose, decide, or need? The resolution must *answer the question the complication raised*. If the resolution is disconnected from the complication, the framing is off.
4. **Read all three aloud as one paragraph.** If the flow feels forced, the three parts aren't aligned. Rewrite until it reads like a natural "here's the story" paragraph.
5. **Attach the supporting pyramid below.** SCR is the hook; the rest of the brief supports the resolution with MECE arguments.

## Examples

### Good — Program delay

> **Situation**: VoxOS China beta wave 2 was scheduled to begin next Tuesday with 8 dealerships.
>
> **Complication**: Two of the eight dealer sites failed pre-flight connectivity checks over the weekend. Rerunning checks takes three days and pushes the wave start to the following Monday.
>
> **Resolution**: We recommend starting wave 2 with six dealers on the original date and adding the remaining two in wave 2.5 a week later, rather than delaying the full cohort.

### Good — Budget ask

> **Situation**: The cockpit-LLM eval harness has been running on a shared dev cluster since January.
>
> **Complication**: At current request volume, we're preempting other teams' jobs ~30% of the time, and our own evals fail intermittently due to resource contention. Expanding from 10 to 40 scenarios (planned in Q3) will make this unworkable.
>
> **Resolution**: We propose allocating a dedicated $38K/quarter cluster slice, with a 90-day review to confirm utilization justifies the spend.

### Bad — No complication

> **Situation**: The team shipped 14 stories last sprint.
> **Complication**: We are on track.
> **Resolution**: No action needed.

This isn't SCR — there's no question raised, no tension to resolve. Use a plain status update instead.

### Bad — Complication doesn't match resolution

> **Situation**: Our customer satisfaction score has been at 72 for four quarters.
> **Complication**: One of our largest customers churned last week.
> **Resolution**: We should invest in onboarding tooling for new customers.

The complication is about losing an existing customer; the resolution is about acquiring new ones. The two don't connect. Either restate the complication ("churn risk is rising in our top-20 segment") or the resolution ("we should run a save campaign on the next-at-risk tier").

## SCR variants

| Variant | Use when |
|---|---|
| **Standard SCR** | Normal update with a clear ask. |
| **S-C-C-R (double complication)** | When the reader also needs to know a counter-factor. "We could do X, *but* Y, *so* we propose Z." |
| **S-C-Q-A (Question-Answer form)** | When the reader needs to see the question explicitly before the answer. Useful for briefs that pre-empt expected objections. |

## Reviewer Checklist

- [ ] **Situation is non-controversial.** The reader nods at it.
- [ ] **Complication creates a question.** After reading it, the reader should implicitly be asking something.
- [ ] **Resolution answers that exact question.** Not a different one.
- [ ] **All three fit in one paragraph.** If they don't, the story is too complex — break into multiple SCRs or escalate to a deeper memo.
- [ ] **No hedging** in the resolution. If it's a proposal, state it plainly. If it's a decision request, ask for it explicitly.
- [ ] **Situation and complication are not the same sentence.** If they are, you're missing one of the two beats.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Situation is actually the complication | Move it down; find a true baseline sentence for situation. |
| Resolution hedges ("we might consider…") | Make it declarative. Hedging belongs in the supporting pyramid, not the hook. |
| Three paragraphs instead of three sentences | SCR is the hook, not the whole brief. Compress; move detail below. |
| No actual change (just status) | Don't use SCR. Use a plain status update. |

## Source

- Barbara Minto, *The Pyramid Principle*, chapter on the introduction.
- McKinsey's "Situation–Complication–Question–Answer" variant, used in internal write-ups.
- The opening paragraph of almost any *Financial Times* leader is a live example.
