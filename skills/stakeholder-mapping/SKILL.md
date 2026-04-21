---
name: stakeholder-mapping
description: >-
  Build a stakeholder map for a program or decision — power/interest
  grid (Mendelow), RACI for specific deliverables, and an influence
  path showing who needs to be convinced in what order. Also flags
  hostile stakeholders, missing advocates, and "RACI pollution"
  (everyone is Consulted).
  TRIGGER when: user asks "who needs to know", "stakeholder map",
  "RACI", "power interest grid", "who should I talk to first", or is
  facing a contentious decision that needs sequencing.
  DO NOT TRIGGER when: user just wants a distribution list (use a
  team roster) or wants to draft a message (use chief-of-staff-brief).
origin: community
---

# Stakeholder Mapping

Produce a structured map of the humans around a program: who they are, how much power and interest they have, what role they play on specific deliverables, and in what order you should engage them.

## When to Use

- Kickoff of any cross-functional program.
- Before a contentious decision where approval ordering matters.
- When inheriting a program and needing to know who's actually in play.
- When a decision has stalled — usually because a power-high, interest-high stakeholder was missed.

**Do not use** for routine distribution-list maintenance or when "stakeholder" just means "attendee."

## Three Artifacts

### 1. Power / Interest Grid (Mendelow, 1991)

Plot each stakeholder on two axes. Four quadrants, four strategies:

```
          HIGH POWER
             │
  Keep       │       Manage
  Satisfied  │       Closely
     (A)     │         (B)
 ────────────┼──────────────── HIGH INTEREST →
             │
  Monitor    │       Keep
             │       Informed
     (D)     │         (C)
             │
         LOW POWER
```

- **(A) Keep Satisfied** — High power, low interest. Don't burn their time, but if they turn against the program, they kill it. Quarterly updates, no surprises.
- **(B) Manage Closely** — High power, high interest. Primary sponsors and blockers. Regular 1:1s, early sight of material.
- **(C) Keep Informed** — Low power, high interest. Teams affected by the program. Transparency and regular updates; their goodwill compounds.
- **(D) Monitor** — Low power, low interest. Awareness-only. A standing email DL is sufficient.

### 2. RACI Matrix (for specific deliverables)

For each major deliverable, each stakeholder gets exactly one of:

- **R** (Responsible) — does the work
- **A** (Accountable) — signs off, one-per-deliverable
- **C** (Consulted) — input before the work is done
- **I** (Informed) — told after the work is done

Three hard rules:
1. **Exactly one A per row.** If there are two, it's not decided yet.
2. **R and A can be the same person** for small items. For large items, keep separate.
3. **Cap C at 3** per row unless you can justify why four opinions are needed. "RACI pollution" — everyone marked C — is a failure mode.

### 3. Influence Path (for a specific decision)

Order the stakeholders you need to convince, with a one-line reason:

```
1. Priya (VP Eng) — shapes the technical feasibility view; if she's skeptical, nothing else matters
2. Maria (CFO) — once Priya is soft-yes, Maria needs the cost picture
3. David (CEO) — only asks him to sign after Priya and Maria are aligned
4. Regional heads — inform after the decision, work the rollout
```

This prevents the anti-pattern of asking for a decision at a forum where one key stakeholder is going to torpedo it because they weren't prepped.

## How It Works

1. **Brainstorm the list.** Every person or role touched by the program. Don't filter yet.
2. **For each, assign power and interest** on a 1–5 scale each. Power = ability to affect the program (approve budget, block a dependency, veto a decision). Interest = how much they care about the outcome.
3. **Plot on the grid.** Which quadrant?
4. **Identify missing advocates.** In quadrant B (manage closely), do you have at least one strong advocate? If not, flag as a risk.
5. **Identify hostile high-power stakeholders.** Anyone in A or B who is currently negative? Flag and plan.
6. **Build RACI** for each major deliverable — only for ones with real handoffs.
7. **For any active decision, build the influence path.**

## Examples

### Power / Interest output

```
| Stakeholder | Role | Power | Interest | Quadrant | Strategy |
|---|---|---|---|---|---|
| Priya | VP Eng | 5 | 5 | Manage Closely | Weekly 1:1; draft review before dist |
| Maria | CFO | 5 | 3 | Keep Satisfied | Monthly update; no budget surprises |
| David | CEO | 5 | 2 | Keep Satisfied | Quarterly; one-pager only |
| Marcus | Legal | 3 | 4 | Keep Informed | Bi-weekly; early draft of regulated content |
| Chen | Eng Lead APAC | 3 | 5 | Keep Informed | Weekly update; field ops detail |
| Support leads (x3) | Ops | 2 | 3 | Monitor | Standing email; no standing meeting |
```

### RACI for a specific deliverable

```
Deliverable: EU AI Act conformity assessment submission

| Task | Priya | Marcus | Sima | Maria |
|---|---|---|---|---|
| Technical documentation | A, R | C |  |  |
| Legal review | C | A, R |  |  |
| Program coordination | I | C | A, R |  |
| Budget sign-off |  | I | C | A |
| Exec communication |  | I | R | C |
```

Rows check: each has exactly one A. Cs are limited. No RACI pollution.

### Influence Path for a hard decision

> **Decision**: Should we pause Japan launch given the regulatory delay?
>
> 1. **Kenji (Country Lead Japan)** — owns the P&L; if he argues for pause, everyone else will follow
> 2. **Priya (VP Eng)** — second opinion on whether we can deliver on the revised timeline
> 3. **Marcus (Legal)** — confirms regulatory risk is material, not just procedural
> 4. **Maria (CFO)** — confirms financial impact is absorbable
> 5. **David (CEO)** — signs once the above four are aligned; only then
> 6. **Regional teams + press team** — informed after, rollout
>
> **Forums**: Take Kenji 1:1 this week. Priya + Marcus in a prep session next week. Maria in one-on-one with pre-read. David in exec staff meeting with written recommendation.

## Reviewer Checklist

- [ ] Every high-power stakeholder is on the grid with a strategy.
- [ ] At least one advocate exists in "Manage Closely" for major initiatives.
- [ ] Every hostile high-power stakeholder has a plan.
- [ ] Each RACI row has exactly one A.
- [ ] No RACI row has more than 3 Cs without explicit justification.
- [ ] Influence path is ordered, with a reason per step.
- [ ] "Monitor" quadrant is not loaded with people who actually belong in "Keep Informed."

## Common Failure Modes

| Failure | Repair |
|---|---|
| All stakeholders rated Power 5 | Recalibrate; not everyone can veto. |
| "Team" or "leadership" as a stakeholder | Decompose to named humans. |
| RACI with multiple As per row | Decide, or acknowledge the decision isn't clear yet. |
| RACI where everyone is C | Cap C at 3; justify each. |
| No influence path for contentious decisions | Build one before the next forum; otherwise the decision will stall. |

## Source

- A. Mendelow, "Stakeholder mapping", Proceedings 2nd International Conference on Information Systems, 1991 (power/interest grid).
- PMI *PMBOK*, Stakeholder Management.
- R. Freeman, *Strategic Management: A Stakeholder Approach* (1984) — foundational text.
- RACI as standardized in BABOK and PMI PMBOK.
