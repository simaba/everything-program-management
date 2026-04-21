---
name: project-charter
description: >-
  Generate a project charter — a one- to two-page document that
  answers: what, why, who, by when, with what, and how will we know
  it worked. Includes scope/non-scope, success criteria, high-level
  milestones, and initial RAID seed. Produces charter.md plus a seed
  RAID log row for the initial top risk.
  TRIGGER when: user asks to "write a charter", "kick off a project",
  "project brief", "PID", or describes a new initiative that needs
  scoping.
  DO NOT TRIGGER when: the project already has a charter (use
  executive-summary-brief for updates) or the scope is a single
  decision (use decision-memo).
origin: community
---

# Project Charter

Produce a one- to two-page charter that answers six questions in order: **what**, **why**, **who**, **by when**, **with what**, **how we'll know**. Nothing more, nothing less.

## When to Use

- New program kickoff.
- Re-scoping an existing program whose original charter is stale.
- Proposing a new workstream to a steering committee.
- Handing a program between PMs.

**Do not use** for single-deliverable tasks (use a task ticket) or ongoing operational work (use an operating-model doc).

## The Six Questions

A good charter answers:

| Question | Section | Length |
|---|---|---|
| **What** are we doing? | Objective and scope | 2–3 sentences |
| **Why** now? | Business rationale | 1 paragraph |
| **Who** owns it? | Sponsor, PM, working team | Named list |
| **By when?** | Timeline with milestones | 3–6 milestones |
| **With what?** | Budget, resources, dependencies | Summary line + link to detail |
| **How will we know** it worked? | Success criteria | 3–5 measurable criteria |

Plus two structural elements:
- **Non-scope** — things people might assume are in scope but aren't. This prevents the #1 charter failure mode: unstated exclusions that bite you later.
- **Initial top risk** — seeded into the RAID log.

## How It Works

1. **Draft the objective** in one sentence. If you can't, the scope isn't clear yet; stop and clarify with the sponsor.
2. **Draft the "why now"** in one paragraph. Why is this the right use of the team's time versus other options?
3. **Name the sponsor, PM, and core team.** Single humans.
4. **Draft 3–6 milestones** with dates. Dates are ranges ("late Q3") only if you truly cannot commit.
5. **Summarize budget and resources.** Headcount, cash, key dependencies. Link to detailed model if it exists.
6. **Draft 3–5 success criteria** that are measurable and time-bound. "Increase NPS" fails; "NPS ≥ 45 by end of Q3, measured by in-product survey n ≥ 500" passes.
7. **Draft non-scope.** Three to five items. Think adversarially: what might someone assume is in scope that isn't?
8. **Seed the top risk** into the RAID log as RAID-0001.
9. **Review against the Reviewer Checklist.**
10. **Circulate to sponsor for sign-off.** Do not start execution without a signed charter.

## Template

```markdown
# Project Charter: [Project Name]

**Status**: Draft | In Review | Signed
**Version**: 0.1
**Last updated**: 2026-04-19
**Sponsor**: Name (Role)
**Program Manager**: Name
**Target sign-off date**: 2026-05-01

---

## Objective

[One to three sentences. Active voice. What we will do and for whom.]

## Why Now

[One paragraph. What changed in the environment, what opportunity or threat this addresses, and why this quarter/year is the right time.]

## Scope

In scope:
- [Specific, concrete inclusion]
- [Specific, concrete inclusion]
- [Specific, concrete inclusion]

Non-scope (explicitly excluded):
- [Inclusion someone might assume]
- [Inclusion someone might assume]

## Team

| Role | Name | Allocation |
|---|---|---|
| Sponsor | Name (Role) | 10% |
| Program Manager | Name | 100% |
| Engineering Lead | Name | 50% |
| Design Lead | Name | 25% |
| [Other] | Name | % |

## Timeline

| Milestone | Target | Description |
|---|---|---|
| M1 — Kickoff | 2026-05-01 | Charter signed, team assembled |
| M2 — Discovery complete | 2026-06-01 | Requirements, constraints, dependency map |
| M3 — Alpha | 2026-07-15 | Internal-only version; N users |
| M4 — Beta | 2026-09-01 | External beta; N users, N regions |
| M5 — GA | 2026-11-01 | Public launch |
| M6 — Post-launch review | 2026-12-15 | Outcomes vs success criteria |

## Budget & Resources

- Budget: $[X] for [period], covering [categories]
- Headcount: [N] FTE-equivalents for [period]
- Key dependencies: [list; link to full dependency map]

## Success Criteria

We will know this project succeeded if, within 90 days of GA:

1. [Measurable criterion with target and measurement method]
2. [Measurable criterion with target and measurement method]
3. [Measurable criterion with target and measurement method]

Each criterion must be: (a) measurable, (b) time-bound, (c) tied to a metric the team can reasonably influence.

## Risks (Initial)

Top risk: [one-line description]. Seeded as RAID-0001 in the risk log.

## Sign-off

- Sponsor: _________________________ Date: _______
- Program Manager: ___________________ Date: _______
- Key stakeholder 1: _________________ Date: _______
```

## Examples

### Good objective

> Build and launch an EU-market conformity assessment workflow that lets our automotive AI teams self-serve their AI Act compliance documentation before the Feb 2027 enforcement date.

### Bad objective

> Drive AI governance excellence across the organization.

(Unmeasurable, unbounded, no target user.)

### Good success criterion

> By 2026-12-15, at least 80% of in-scope AI features have a complete conformity assessment package (all 7 required sections, audited sample n ≥ 20), with zero external audit findings classified "major."

### Bad success criterion

> Improve AI governance maturity.

### Good non-scope line

> Not in scope: AI features deployed only in non-EU markets. Those are covered by `governance-emea-v2` separately.

(Prevents the common mistake of a reader assuming a bigger scope.)

## Reviewer Checklist

- [ ] Objective is one to three sentences.
- [ ] "Why now" answers what changed, not just what we want.
- [ ] Sponsor is a named human, not a title.
- [ ] PM is a named human with ≥ 50% allocation.
- [ ] At least 3 milestones with specific dates.
- [ ] Non-scope has at least 3 items.
- [ ] All success criteria are measurable and time-bound.
- [ ] At least one risk is seeded into the RAID log.
- [ ] Charter is ≤ 2 pages.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Objective is 5 sentences with a "will" per clause | Pick the core outcome. Put the rest in scope bullets. |
| No non-scope section | Write one. Think adversarially about unstated assumptions. |
| Success criteria are "ship X" | Ship is an output, not an outcome. What changes because we shipped? |
| Timeline has 15 milestones | Collapse to 3–6. If you genuinely have 15, you have a program-of-programs; each sub-program gets its own charter. |
| Sponsor not identified | Don't start. Get a sponsor first. |

## Source

- PMI *PMBOK Guide*, Project Charter.
- UK APM *Body of Knowledge*, Project Initiation Document (PID) format.
- Amazon's PR/FAQ (press-release–first) format — structurally similar but outcome-led; see `docs/METHODOLOGY.md` for comparison.
