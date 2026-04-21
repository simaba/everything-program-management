# Project Charter: Japan Voice-Assistant Market Launch (2026)

**Status**: In Review
**Version**: 0.3
**Last updated**: 2026-04-19
**Sponsor**: David Liang (VP, International Product)
**Program Manager**: Sima Bagheri
**Target sign-off date**: 2026-05-01

---

## Objective

Launch the VoxOS in-vehicle voice assistant in the Japan market for model-year 2027 vehicles, with full Japanese-language NLU, on-device wake-word, and integration with three local navigation and media partners (NavTime, Radiko, Music.jp).

## Why Now

Japan is the second-largest market by unit volume for the VoxOS-equipped fleet (projected 220k vehicles in 2027). Two competitors shipped Japanese voice in 2025; we are the only premium OEM in segment without it. The MY27 software-freeze deadline is 2026-09-15, which makes this the last opportunity to ship for that production cycle without a costly OTA-only path post-SOP. The Japanese-language NLU model finished pre-training in March and is at parity with the EN baseline on the limited internal eval set.

## Scope

In scope:
- Japanese-language NLU and TTS for the in-cabin voice assistant.
- On-device wake-word ("Hey Vox") tuned for JP acoustic environment.
- Integration with NavTime (navigation), Radiko (radio), Music.jp (streaming).
- Privacy and consent UX in Japanese, compliant with APPI.
- A/B-tested rollout to 10% of the MY27 JP fleet at SOP, ramping to 100% over 8 weeks.

Non-scope (explicitly excluded):
- China market — covered by the parallel `voxos-china-2026` program.
- Korean and Mandarin support — out of scope for this charter; planned for MY28.
- Third-party app-store integrations beyond the three named partners.
- Steering-wheel hardware changes — using the existing PTT button.
- Changes to the cluster display or HUD voice-feedback UI.

## Team

| Role | Name | Allocation |
|---|---|---|
| Sponsor | David Liang (VP, International Product) | 10% |
| Program Manager | Sima Bagheri | 100% |
| Engineering Lead | Hiroshi Tanaka | 75% |
| NLU Model Lead | Chen Wei | 50% |
| Partner Integration Lead | Akira Yamamoto | 80% |
| Design Lead | Maya Rivera | 40% |
| QA Lead | Kenji Sato | 60% |
| Legal / APPI | Marcus Holst | 15% |

## Timeline

| Milestone | Target | Description |
|---|---|---|
| M1 — Charter signed, team confirmed | 2026-05-01 | This document signed; resource commits in place. |
| M2 — Partner contracts signed | 2026-06-15 | NavTime, Radiko, Music.jp commercial + technical agreements. |
| M3 — Internal alpha (50 vehicles, JP test fleet) | 2026-07-15 | All three integrations live on test fleet; intent accuracy ≥ 90%. |
| M4 — Closed beta (200 vehicles, JP press + employees) | 2026-08-20 | Production code path; APPI consent UX final. |
| M5 — Software-freeze cutoff | 2026-09-15 | Final binary into the MY27 production image. |
| M6 — SOP + 10% rollout | 2026-11-03 | Production vehicles begin shipping with feature flagged on for 10%. |
| M7 — 100% rollout | 2026-12-29 | Feature on by default for all MY27 JP vehicles. |
| M8 — 90-day post-launch review | 2027-03-30 | Outcomes vs success criteria; lessons into MY28 plan. |

## Budget & Resources

- Budget: ¥182M for the period 2026-04 → 2027-03, covering partner licensing (¥110M), localization (¥38M), QA fleet ops (¥22M), contingency (¥12M).
- Headcount: 4.2 FTE-equivalents, drawn from the existing VoxOS Voice team (no net new hires).
- Key dependencies: shared NLU training infrastructure (owned by Platform team), MY27 software-freeze date (owned by Vehicle Engineering), APPI legal opinion on always-listening wake-word (owned by Legal). See `examples/raid/raid-log-voxos-china.md` style log for live tracking.

## Success Criteria

We will know this project succeeded if, within 90 days of 100% rollout (by 2027-03-30):

1. **Adoption**: ≥ 60% of MY27 JP vehicles have triggered the voice assistant at least 5 times, measured via in-product telemetry on opted-in fleet (n ≥ 50k).
2. **Accuracy**: Top-1 intent accuracy ≥ 92% on the production JP test set (n ≥ 5,000 utterances), audited monthly.
3. **Latency**: p95 end-to-end response time ≤ 300ms for on-device intents and ≤ 800ms for cloud-routed intents.
4. **Quality / safety**: Zero P0 voice-related incidents post-SOP; ≤ 3 P1 incidents resolved within SLA.
5. **Partner health**: All three partner integrations (NavTime, Radiko, Music.jp) at ≥ 99.5% monthly availability as measured by joint SLA dashboards.

Each criterion is measurable, time-bound, and tied to a metric the team can influence. Adoption is the only criterion with a market-facing dependency; the other four are within the team's direct control.

## Risks (Initial)

Top risk: **Software-freeze cutoff (2026-09-15) is non-negotiable; any slip in NLU production-readiness (currently tracking yellow) forces a 6-month delay to MY28.**

Seeded as RAID-0001 in `examples/raid/raid-log-voxos-china.md` (see RAID-0002 for the equivalent JP risk row pattern).

Two follow-on risks already identified and seeded:

- RAID-0003: NavTime contract negotiation has stalled on data-egress terms (see decision memo `examples/decisions/DM-0001-japan-launch-pause.md`).
- RAID-0004: APPI legal opinion on always-listening wake-word not yet finalized; Marcus committed to a draft by 2026-05-15.

## Sign-off

- Sponsor (David Liang): _________________________ Date: _______
- Program Manager (Sima Bagheri): _________________ Date: _______
- Engineering Lead (Hiroshi Tanaka): _____________ Date: _______
- Legal (Marcus Holst): __________________________ Date: _______

---

*This charter was drafted using the `project-charter` skill. It composes with `raid-log` (initial risks seeded) and `stakeholder-mapping` (sponsor + co-deciders identified). For updates after sign-off, use `executive-summary-brief` not a new charte