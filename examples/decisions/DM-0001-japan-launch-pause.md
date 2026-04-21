---
id: DM-0001
title: "Should we pause the Japan launch given the NavTime contract stall?"
decider: david@example.com
co_deciders:
  - akira@example.com
  - marcus@example.com
due: 2026-05-10
status: in_review
decided: null
decision: null
reversibility: two_way
tags: [voxos-china, japan, partner, schedule]
links:
  charter: examples/charters/charter-japan-launch-2026.md
  related_raid: examples/raid/raid-log-voxos-china.md
  source_doc: https://example.com/internal/japan-launch-status-2026-04-19
---

## Question

Should we pause the Japan voice-assistant launch (slip from MY27 to MY28) until the NavTime contract is resolved, or proceed on the current timeline with a contingent launch path?

## Context

The Japan launch (charter `charter-japan-launch-2026.md`) requires three partner integrations: NavTime, Radiko, Music.jp. Radiko and Music.jp are signed. NavTime has been stalled for two weeks (RAID-0003) on a data-egress clause that, as drafted, would block on-vehicle caching of nav results — which breaks the offline-routing user story. Two cycles of legal back-and-forth have not closed. Akira's read is that NavTime will move, but not before mid-June; that puts integration testing into the last 8 weeks before software-freeze, with no slack for the inevitable surprises.

## Criteria

1. **Schedule risk** — probability we miss the 2026-09-15 software-freeze cutoff and slip to MY28.
2. **Partner-relationship cost** — durable cost to the NavTime relationship and to our credibility with the other two partners.
3. **Market exposure** — months without Japan voice while two competitors ship.
4. **Sunk cost** — investment to date that becomes wasted on a slip.
5. **Reversibility** — how easily we can change course later if conditions change.

## Options

### Option A: Hold the line on current timeline, all three partners

- Schedule risk: 55% probability of missing freeze (Akira's estimate, May 1).
- Partner cost: Low if we ship; very high if we slip (NavTime sees us as unable to deliver).
- Market exposure: 0 months if we ship; 12 if we slip.
- Sunk cost: ¥110M partner licensing fully spent; ¥38M localization 70% spent.
- Reversibility: Two-way — we can always slip later, but the slip cost grows weekly.

### Option B: Proceed on timeline; cut NavTime from MY27 scope; ship with native maps + Radiko + Music.jp only

- Schedule risk: 15% probability of missing freeze (NavTime integration was the long pole).
- Partner cost: NavTime damaged — they invested in the integration too. Recoverable if we commit publicly to MY28 inclusion.
- Market exposure: 0 months. Native maps is a known weaker product but covers the use case.
- Sunk cost: ~¥40M of NavTime-specific integration work shelved (30% recoverable for MY28).
- Reversibility: Two-way — we can re-add NavTime in MY28 OTA.

### Option C: Pause to MY28; resolve NavTime properly; relaunch with all three partners

- Schedule risk: 0% (we are choosing the slip).
- Partner cost: Radiko and Music.jp damaged (they sized teams for our timeline). Mitigatable but real.
- Market exposure: 12 months. Two competitors will have a year of head start in JP.
- Sunk cost: ¥182M largely written down for MY27; partial credit toward MY28.
- Reversibility: One-way at the program level — once we tell the market we're not shipping in MY27, we don't get that window back. Two-way at the contract level.

## Ruled Out

- **Option D: Hold timeline; substitute a different nav partner.** Evaluated MapFan and ZENRIN. Both require ≥ 16 weeks of integration; impossible inside the freeze window.
- **Option E: Build native nav from scratch for JP.** Timeline-infeasible (≥ 9 months). Also outside our charter scope.

## Recommendation

**Option B** — proceed on timeline with native maps + Radiko + Music.jp; defer NavTime to MY28 OTA.

The single most important reason: Option B is the only path that ships in MY27 *and* keeps the schedule risk below 20%. Option A's 55% slip probability is unacceptable for a non-negotiable cutoff; we would in effect be choosing Option C with extra burned cost.

Native maps is a real product downgrade, but a known one — we can communicate it honestly, set expectations for MY28 NavTime via OTA, and use the year to negotiate the data-egress clause from a position of "we're already shipping" rather than "we need you to close this for us to ship."

## Consequences

- **If A** (hold the line, all three): 55% chance of missing freeze. If we miss, NavTime relationship is worse than if we'd cut them now (we wasted their time too). Sunk cost ¥182M for MY27 + carry of MY28 work.
- **If B** (cut NavTime, ship MY27): 15% slip risk. NavTime relationship takes a hit but is recoverable with a public MY28 commitment. ~¥40M of NavTime-specific work shelved. Native maps becomes a known gap that competitor reviews will exploit. Ramp-down conversation with NavTime needs to be handled by Akira, not legal.
- **If C** (pause to MY28): 12-month market exposure. Two competitors will have ~12 months of feedback-loop advantage on JP voice. Likely costs us ~10pt of MY28 attach rate based on the China comp.

## Asks

- **David**: sign by 2026-05-10 or flag a different option in `#program-voxos-japan`.
- **Akira**: by 2026-05-08, draft the NavTime ramp-down conversation script (deferral, not termination) for Sima's review.
- **Marcus**: confirm by 2026-05-08 that publicly disclosing the deferral has no securities-disclosure implications.
- **Sima**: if Option B is chosen, brief sponsor on the "native maps gap" press posture by 2026-05-15.

## Open Questions

- If we choose B and NavTime then closes the data-egress issue in June, is it worth re-opening the integration for MY27 OTA in November? (Owner: Akira; answer expected 2026-06-30 once contract resolves.)
- The 55% / 15% slip probabilities are Akira's individual estimate. Worth a second read from Hiroshi (engineering lead) before David signs. (Owner: Sima; by 2026-05-05.)

---

*This memo was drafted using the `decision-memo` skill. Frontmatter validates against `schemas/decision-memo-frontmatter.json`. Reversibility marked `two_way` per the `one-way vs two-way doors` rule. After decision, update `status` to `decided`, fill `decided` (date) and `decision` (chosen option), and the `decision_journal_review.py` script will surface this memo for 90-day retrospection on or after 2026-08-08