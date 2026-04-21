---
name: raid-log
description: >-
  Maintain a RAID log — Risks, Assumptions, Issues, Dependencies —
  with strict schema, owner/date discipline, and risk scoring
  (probability × impact). Adds rows, promotes assumptions that fail
  to risks, closes items with resolution notes, and generates
  this-week summaries. Schema-validated against schemas/raid-row.json.
  TRIGGER when: user says "RAID", "risk register", "add this risk",
  "what's at risk", "track this dependency", "log an assumption", or
  wants a structured program-risk artifact.
  DO NOT TRIGGER when: the user wants a free-form risk discussion
  (use risk-triage) or a single-issue deep dive (use decision-memo).
origin: community
---

# RAID Log

Maintain a structured log of **Risks**, **Assumptions**, **Issues**, and **Dependencies** for a program, with enough discipline that the log is actually useful six months in.

## When to Use

- Kickoff of any program that will run longer than one month.
- Weekly or bi-weekly maintenance during execution.
- Before any steering committee update.
- When inheriting an existing program with no risk artifact.

**Do not use** for single-issue deep-dives (those belong in a decision memo) or for post-facto blame allocation (see `post-mortem-facilitation`).

## The Model

Four categories, each with precise definitions:

| Category | Definition | Key field |
|---|---|---|
| **Risk** | A future event that *might* happen and, if it does, affects the program. | Probability × Impact |
| **Assumption** | A condition we believe to be true and are planning around, but haven't confirmed. | Validation plan |
| **Issue** | An event that *has happened* and is affecting the program now. | Owner + fix plan |
| **Dependency** | An input we need from someone else, without which we can't proceed. | Provider + need-by date |

The most common mistake is conflating these — especially risks with issues. A risk is future; an issue is present. Once a risk occurs, it becomes an issue and is closed as a risk.

## Row Schema

Each row validates against `schemas/raid-row.json`:

```yaml
id: RAID-0042                    # sequential, immutable once assigned
type: risk | assumption | issue | dependency
title: "One-line summary"        # ≤ 80 chars
description: "Full context"      # prose, 1-3 sentences
category: scope | schedule | cost | quality | resource | external
owner: name@domain.com           # single human, not a team
opened: 2026-04-19               # YYYY-MM-DD
due: 2026-05-15 | null           # review date or need-by date
status: open | monitoring | closed
# Risk-only fields:
probability: 1-5                 # 1=remote, 5=near-certain
impact: 1-5                      # 1=minor, 5=program-threatening
score: probability * impact      # computed, not input
mitigation: "What we're doing about it"
trigger: "What would signal this is about to happen"
# Assumption-only fields:
validation_plan: "How we'll confirm or disprove"
# Issue-only fields:
fix_plan: "What we're doing now"
eta: 2026-05-01
# Dependency-only fields:
provider: name@domain.com | team-name
blocks: [RAID-0012, RAID-0021]   # what this dependency blocks
```

## How It Works

### Adding a row

1. **Classify.** Risk, assumption, issue, or dependency? Use the definitions above strictly.
2. **Write the title first** — 80 characters, the gist. If you can't compress it, the item isn't clear in your own head yet.
3. **Write owner and date.** Owner is a single human. "The team" is not an owner.
4. **For risks**: score probability and impact (1–5 each). Score = P × I. Risks scoring ≥ 16 go to the top of the weekly review.
5. **For assumptions**: write the validation plan. If you can't, the assumption is really a hope.
6. **For issues**: write the fix plan and ETA.
7. **For dependencies**: write the provider and blocks list.

### Weekly review

1. **Promote/demote.** Assumptions that failed become risks. Risks that occurred become issues. Issues that closed become closed.
2. **Re-score risks.** Probability changes as the program progresses.
3. **Close aged items.** Anything open > 60 days with no owner update: force-review, either close with "no action" or reassign.
4. **Archive closed rows.** Don't delete — move to `archive/` so the history survives.

### This-week summary (for exec brief)

Produce a three-line summary:
- **Top 3 risks by score** — title, owner, score, mitigation one-liner.
- **New issues this week** — count + titles.
- **Dependencies due in next 14 days** — count + provider.

## Examples

### Good rows

```yaml
- id: RAID-0017
  type: risk
  title: "Tier-1 supplier may miss May 15 parts deadline"
  description: "Supplier reported yield issues on two SKUs. Alternate source
    exists but adds 4 weeks lead time."
  category: schedule
  owner: priya@example.com
  opened: 2026-04-02
  due: 2026-05-15
  status: monitoring
  probability: 3
  impact: 5
  score: 15
  mitigation: "Weekly yield review; alternate supplier on standby contract."
  trigger: "Yield remains below 70% after May 1 review."

- id: RAID-0018
  type: assumption
  title: "Regulatory approval arrives before Aug 1"
  description: "Planning assumes EU AI Act conformity assessment completes by
    July, enabling Aug launch. No formal commitment from notified body yet."
  category: external
  owner: marcus@example.com
  opened: 2026-04-10
  due: 2026-06-15
  status: open
  validation_plan: "Notified body provides written ETA by June 15 review."

- id: RAID-0019
  type: issue
  title: "Translation bug in APAC onboarding flow"
  description: "Simplified Chinese strings incorrectly rendered during wave 1
    pilot, contaminating activation data."
  category: quality
  owner: chen@example.com
  opened: 2026-04-15
  due: null
  status: open
  fix_plan: "Fix merged and deploying to staging April 17; re-run APAC pilot."
  eta: 2026-04-22

- id: RAID-0020
  type: dependency
  title: "Security review from IT for new vendor onboarding"
  description: "New vendor must pass IT security review before production
    access. Review queue currently 3 weeks."
  category: external
  owner: sima@example.com
  opened: 2026-04-12
  due: 2026-05-10
  status: open
  provider: it-security@example.com
  blocks: [RAID-0012]
```

### Bad row — conflated risk/issue

```yaml
- title: "The vendor is late"      # This is an issue, not a risk
  type: risk
```
Fix: change type to `issue`, add `fix_plan` and `eta`.

### Bad row — no owner

```yaml
- owner: "Program team"            # Not a human
```
Fix: assign to one person accountable for the item.

## Reviewer Checklist

- [ ] Every row has a single human owner.
- [ ] Risks have probability, impact, and score.
- [ ] Assumptions have a validation plan.
- [ ] Issues have a fix plan and ETA.
- [ ] Dependencies have a provider and a `blocks` list.
- [ ] No row has been open > 60 days without an owner update.
- [ ] Risks ≥ 16 are called out in the weekly summary.
- [ ] Closed rows are archived, not deleted.

## Anti-patterns

| Anti-pattern | Why it's bad | Repair |
|---|---|---|
| "Generic risk" rows (e.g., "Schedule slippage") | Not actionable; owner can't do anything specific | Rewrite as a named, concrete event with a trigger |
| Team as owner | No one is accountable | Assign to the single person who would make the call |
| All risks scored 3×3 = 9 | Real program has a distribution | Re-score honestly; some are 2×2, some are 4×5 |
| Log of 200 rows, never pruned | Unreadable; no one uses it | Archive closed items, cap active log at ~40 rows |
| Issues recorded as "ongoing" with no ETA | Never closes | Every issue gets a hard ETA or becomes a program change |

## Source

- PMI *PMBOK Guide*, Risk Management knowledge area.
- UK Association for Project Management, *APM Body of Knowledge*, chapter on RAID logs.
- Internal program-management playbooks at large consultancies.
- Complementary JSON schema: `schemas/raid-row.json`.
