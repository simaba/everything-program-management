---
name: executive-summary-brief
description: >-
  Produce a one-page executive summary of any input (long doc, thread,
  meeting transcript, RAID log) that opens with BLUF, follows the
  Pyramid Principle, and ends with the explicit ask. Enforces the
  "one page or it's not an exec brief" rule.
  TRIGGER when: user says "exec summary", "exec brief", "one-pager",
  "BLUF", "summarize for the CEO", "TL;DR for leadership", or asks to
  compress something for an executive audience.
  DO NOT TRIGGER when: user wants a status report (use scr-narrative)
  or a daily PM brief (use chief-of-staff-brief).
origin: community
---

# Executive Summary Brief

Compress any input into a one-page brief an executive can read in 60 seconds, decide on, and act from. Pyramid-structured. BLUF first. Ask last. Nothing else.

## When to Use

- A 30-page document needs to land in 60 seconds of executive attention.
- A long Slack/email thread needs to be turned into a decision-ready summary.
- A program update needs to go to a steering committee.
- A board memo, exec staff pre-read, or sponsor briefing.

**Do not use** for:
- Daily PM brief → use `chief-of-staff-brief`.
- Status reports with no decision implied → use `scr-narrative`.
- Multi-option decisions → use `decision-memo` (which is its own format).

## The One-Page Contract

Hard rules:
1. **One page.** ~300–400 words. No appendix in the brief itself; appendix is a separate document.
2. **BLUF on line 1.** Bottom Line Up Front. The recommendation, decision needed, or one-sentence summary.
3. **Pyramid structure.** BLUF, then 3 supporting points, then evidence under each. No prose ramps.
4. **The Ask.** Last line names what the executive is being asked to do: approve, decide, attend, fund, escalate. If there is no ask, this is a FYI, not an exec brief.

## The Structure

```markdown
# [Title — 6 words max]

**To**: [Name, Role]
**From**: [Name]
**Date**: 2026-04-19
**Re**: [What this is about — one phrase]

## BLUF
[One sentence. The recommendation, decision, or single most important fact.]

## Why This Matters
[Two sentences. Stakes for the business. What changes if we act / don't act.]

## What's True
1. **[Supporting point 1]** — [one-sentence evidence]
2. **[Supporting point 2]** — [one-sentence evidence]
3. **[Supporting point 3]** — [one-sentence evidence]

## What I Recommend
[One paragraph. The recommended action, the single most important reason, and the cost of doing it.]

## Risks
- [Risk + mitigation, one line]
- [Risk + mitigation, one line]

## The Ask
[One sentence. Explicit, named action by named person by named date.]

## Where to Look for More
- [Link to source doc]
- [Link to RAID log / decision memo]
```

## How It Works

1. **Find the BLUF.** Read the source 2–3 times if needed. The BLUF is the one thing the executive must know if they read nothing else. If you cannot identify it in one sentence, the source is not yet decision-ready and needs more thinking before a brief.
2. **Find the 3 supporting points** that prove the BLUF. Use MECE. If you have 5, you're not yet sure which 3 matter.
3. **Match each point to evidence** the executive can scan, not interpret.
4. **State stakes.** "Why this matters" is the bridge; without it, the executive doesn't know whether to read past line 2.
5. **Write the recommendation as a stance, not a summary.** "We should X because Y" — not "the team has been considering X."
6. **State the Ask explicitly.** "Approve $X by Friday." "Sign by EOW." "Attend Monday's review." "Decide between A and B."
7. **Cut.** If it's over one page, cut. The contract is one page; everything else is appendix.

## Examples

### Good BLUF

> Recommend pausing the Japan launch to Q4 to absorb the regulatory delay; doing so costs $1.2M and avoids a $9M downside scenario.

(Names the recommendation, the cost, and the alternative cost in one sentence.)

### Bad BLUF

> The Japan launch program has experienced several developments over the last two weeks that we should discuss.

(Buries the lede. Tells the executive nothing actionable.)

### Good "Why This Matters"

> A regulatory delay closes the Q3 launch window. Holding the original date risks a $9M penalty and a reputational hit; pausing costs $1.2M in idle inventory and slips Japan revenue by one quarter.

### Bad "Why This Matters"

> This is a complex situation with many stakeholders affected. Multiple options are being considered.

### Good "Ask"

> Sign the attached Option-B authorization by Friday Apr 24, 17:00 JST, or flag concerns in #program-japan-launch.

### Bad "Ask"

> Please review and provide thoughts at your convenience.

(Not an ask; it's a passive notice. Executives won't act on it.)

## Reviewer Checklist

- [ ] Brief fits on one page (~300–400 words).
- [ ] BLUF is on line 1 (after metadata).
- [ ] BLUF is one sentence, action-led, not context-led.
- [ ] "Why This Matters" quantifies stakes.
- [ ] Exactly 3 supporting points, each with one-line evidence.
- [ ] Recommendation is a stance, not a summary.
- [ ] Risks include mitigations, not just the risk.
- [ ] The Ask is explicit, named, dated.
- [ ] No buried lede anywhere — every section opens with the conclusion.

## Common Failure Modes

| Failure | Repair |
|---|---|
| BLUF is context, not conclusion | Move conclusion to the top; context becomes "Why This Matters." |
| 7 supporting points | MECE-collapse to 3. If you can't, you don't know what's actually load-bearing. |
| No ask | If there's no ask, it's a FYI; reframe as such or close the open question first. |
| Two pages | Cut. The contract is one page. |
| Hedging in the BLUF ("we may want to consider…") | Take a stance or don't write the brief. |

## Source

- Barbara Minto, *The Pyramid Principle*, on opening with the answer.
- BLUF (Bottom Line Up Front) from US military staff-writing tradition; see Kabay, *Writing for the Military*, and the Army Regulation 25-50 standard.
- Amazon's six-pager and PR-FAQ traditions on decision-ready prose.
- Andy Grove, *High Output Management*, on the cost of executive attention.
