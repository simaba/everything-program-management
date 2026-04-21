---
name: risk-triage
description: >-
  Re-score and prioritize risks in a RAID log against current evidence
  and recommend owner actions. Produces a triaged list with each risk
  classified as Now / This Week / This Month / Watch, plus the single
  next action per risk and the named owner. Built for weekly risk-review
  forums.
  TRIGGER when: user says "triage these risks", "what's red", "weekly
  risk review", "re-score the RAID", "what's at risk this week", or
  asks for prioritization across an existing risk set.
  DO NOT TRIGGER when: user wants to add a new risk (use raid-log) or
  classify a single risk in isolation (use raid-log directly).
origin: community
---

# Risk Triage

Take a RAID log (or any list of risks) and produce a triaged, action-ready view: which risks demand action **now**, which **this week**, which **this month**, and which are **watch-only**. Each risk gets one next action and one named owner. No pages of analysis — the output is a ranked working set.

## When to Use

- Weekly risk review meeting prep.
- After a state change (incident, schedule slip, dependency break) that invalidates yesterday's prioritization.
- Inheriting a RAID log and needing to know what's actually live.
- Before an exec brief — the brief should reflect the triaged view, not the raw log.

**Do not use** for:
- Adding a single new risk → use `raid-log`.
- Building the log in the first place → use `raid-log`.
- Decision-grade tradeoff analysis on one risk → use `decision-memo`.

## The Four Buckets

```
NOW         — needs action in the next 24 hours; un-triaged it will damage the program
THIS WEEK   — needs decision or escalation by end of this week
THIS MONTH  — being managed; check at next monthly review
WATCH       — known but not currently consuming bandwidth; re-check at next quarterly
```

The buckets are **time-to-action**, not severity × likelihood. A SEV-1 risk fully mitigated this morning is "watch"; a SEV-3 risk that just changed state is "now."

## Scoring

For each risk, ask three questions in order:

1. **What changed since the last triage?** State changes drive the bucket. If nothing changed, the bucket from last week is the default unless a deadline forced a move.
2. **What's the time-to-action?** When does the next decision or owner action need to happen? That sets the bucket.
3. **Who owns the next action?** One named human. "The team" is not an answer.

Severity × likelihood is informational, not the bucket criterion. A high-severity risk with no actionable lever this week is correctly "watch." A low-severity risk blocking a Friday decision is correctly "now."

## The Output

```markdown
# Risk Triage — [date]

**Source RAID log**: [link]
**Triaged by**: [name]
**Window**: 2026-04-19 → 2026-04-26

## NOW (next 24h)
| RAID | Title | What changed | Next action | Owner | Due |
|---|---|---|---|---|---|
| RAID-0014 | China data-residency exposure | Legal flagged new draft of PIPL guidance | Draft response position | Marcus | Apr 20 |

## THIS WEEK
| RAID | Title | What changed | Next action | Owner | Due |
|---|---|---|---|---|---|
| RAID-0021 | EV cabin noise miscls | QAT pilot result expected May 15 | Schedule pilot review | Chen | Apr 24 |

## THIS MONTH
| RAID | Title | Status | Owner | Next checkpoint |
|---|---|---|---|---|
| RAID-0011 | Vendor SLA renegotiation | In progress; draft term sheet circulated | Maria | May 5 |

## WATCH
| RAID | Title | Why it's watch | Re-check at |
|---|---|---|---|
| RAID-0008 | Long-tail PII in support tickets | No new incidents in 60 days | Quarterly |

## Removed from active set
- [RAID-id] [title] — [reason: closed / accepted / transferred to <owner>]
```

## How It Works

1. **Pull the RAID log.** Filter to open items. Closed items go to the "removed" list with one line each.
2. **For each open item, identify state changes** since the last triage. New evidence, missed milestone, decision made, owner change.
3. **Bucket by time-to-action.** Default: same bucket as last triage. Move only on state change or deadline pressure.
4. **For each item moved up** (e.g., This Week → Now), name what triggered the move.
5. **For each item with no next action**, either (a) name one or (b) move to Watch / close it. "No action" with active status is the most common log-rot symptom.
6. **Cap NOW at 5 items.** If you have more, you're in crisis mode (see `contexts/crisis-mode.md`); triage isn't the right tool.
7. **Cap THIS WEEK at 10 items.** Same logic — beyond 10, the team can't actually act on all of them.

## Composition With Other Skills

- **`raid-log`** is the source. Triage does not modify the log; it produces a derived view.
- **`stakeholder-mapping`** decides who needs the triage output. NOW items often demand a Manage-Closely stakeholder be looped in same-day.
- **`decision-memo`** is what NOW or THIS WEEK risks often graduate into — when the next action is "decide between X and Y."
- **`executive-summary-brief`** is the upward-facing view; risk-triage is the working view.

## Examples

### Good "what changed" line

> Vendor confirmed they cannot meet the May 1 cutover; this risk moves from "this month" to "now" because the slip invalidates our Q2 plan.

### Bad "what changed" line

> Risk is still elevated.

(Not a state change; just a status. Belongs in the RAID log, not in triage output.)

### Good NOW item

> RAID-0014. Legal flagged a new PIPL guidance draft yesterday afternoon that could classify our hybrid voice path as in-scope for data localization. Next action: Marcus drafts our position memo by tomorrow EOD; if classified in-scope, this changes the architecture decision currently in DM-0014.

### Bad NOW item

> RAID-0014. Data residency is a major risk. Need to address.

(No state change, no action, no owner, no date. Cannot be acted on.)

## Reviewer Checklist

- [ ] Every NOW item names what changed since the last triage.
- [ ] Every NOW and THIS WEEK item has a single named owner (not a team).
- [ ] Every NOW and THIS WEEK item has a specific next action and a date.
- [ ] NOW bucket has ≤ 5 items.
- [ ] THIS WEEK bucket has ≤ 10 items.
- [ ] Items in WATCH have an explicit re-check date.
- [ ] Items removed from the active set have a reason.

## Common Failure Modes

| Failure | Repair |
|---|---|
| 15 items in NOW | You're in a crisis, not a triage. Switch to `crisis-mode` and reduce span. |
| Every item moved up since last week | Either a real state change wave (incident) or risk inflation. Ask: what concretely changed in the world? |
| Owner = "the team" | Force a single name. If no one will own it, it should be in WATCH or closed. |
| WATCH bucket is 80% of items | Probably correct — most risks are not actionable this week. Don't artificially promote. |
| No state-change column | Triage becomes a list copy. The state-change column is the value. |

## Source

- PMI *PMBOK*, Risk Management chapter on monitoring and re-prioritization.
- ISO 31000, Risk Management — Guidelines, on the iterative re-assessment principle.
- Lean Coffee / weekly-stand-up patterns adapted for risk forums.
- Andy Grove, *High Output Management*, on management by exception (only re-touch what changed).
