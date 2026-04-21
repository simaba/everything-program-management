---
program: voxos-china-2026
owner: priya@example.com
last_reviewed: 2026-04-19
rows:
  - id: RAID-0001
    type: Risk
    title: Software-freeze cutoff binds entire program timeline
    description: >-
      MY27 software freeze is 2026-09-15 and cannot be moved without
      slipping SOP. Any NLU production-readiness slip past late August
      forces a 6-month delay to MY28.
    severity: 5
    likelihood: 3
    score: 15
    owner: Hiroshi Tanaka
    due: 2026-08-25
    status: mitigating
    mitigation: >-
      Weekly readiness checkpoints starting 2026-06-01. Pre-freeze
      candidate build by 2026-08-10 to leave 5-week buffer. Fallback
      OTA-only path scoped (RAID-0007).
    trigger: >-
      Production-build acceptance test fails or critical bug found
      between 2026-08-25 and freeze date.
    last_updated: 2026-04-19
    tags: [voxos-china, schedule, p0]

  - id: RAID-0002
    type: Risk
    title: On-device NLU accuracy 0.7pt below target on China test set
    description: >-
      Current 700M-param on-device model scores 91.3% top-1 vs 92%
      target. Cloud-only path meets accuracy at 94.1% but misses the
      300ms latency target. Quantization-aware training in flight.
    severity: 4
    likelihood: 3
    score: 12
    owner: Chen Wei
    due: 2026-05-15
    status: mitigating
    mitigation: >-
      QAT pass on the production training set; expected to recover
      0.4-0.6pt. If gap persists, hybrid routing (DM-0001) closes it
      via cloud fallback for tail intents.
    trigger: QAT pass fails to close gap by 2026-05-15.
    last_updated: 2026-04-15
    tags: [voxos-china, ml, accuracy]

  - id: RAID-0003
    type: Issue
    title: NavTime contract stalled on data-egress terms
    description: >-
      NavTime legal pushing for a clause that would block us from
      caching nav results on-vehicle, which breaks the offline-routing
      story. In escalation since 2026-04-08.
    severity: 4
    likelihood: 5
    score: 20
    owner: Akira Yamamoto
    due: 2026-05-10
    status: open
    last_updated: 2026-04-18
    tags: [voxos-china, partner, legal]

  - id: RAID-0004
    type: Risk
    title: APPI opinion on always-listening wake-word not yet final
    description: >-
      Japanese privacy regulator (APPI) guidance on always-listening
      wake-word is being interpreted conservatively by external
      counsel. Risk that we have to add an explicit consent prompt at
      every ignition.
    severity: 3
    likelihood: 3
    score: 9
    owner: Marcus Holst
    due: 2026-05-15
    status: mitigating
    mitigation: >-
      Marcus drafting opinion by 2026-05-15. Backup UX (per-trip
      consent toast) prototyped by Maya in case we need it.
    last_updated: 2026-04-12
    tags: [japan, legal, appi]

  - id: RAID-0005
    type: Assumption
    title: Shared NLU training infrastructure has capacity through Q3
    description: >-
      We assume the Platform team's shared training cluster has
      capacity for our weekly fine-tunes through end of Q3. If a
      higher-priority program preempts, we slip.
    severity: 4
    likelihood: 2
    score: 8
    owner: Sima Bagheri
    due: 2026-05-01
    status: open
    assumption_test: >-
      Confirm with Platform team lead by 2026-05-01 that our quota
      is reserved through 2026-09-30. If declined, escalate to
      sponsor.
    last_updated: 2026-04-10
    tags: [voxos-china, infra, dependency]

  - id: RAID-0006
    type: Dependency
    title: Vehicle Engineering MY27 build manifest
    description: >-
      Our binary inclusion depends on the MY27 build manifest being
      finalized by 2026-08-15. Vehicle Engineering owns the manifest;
      we are one of nine teams contributing.
    severity: 5
    likelihood: 2
    score: 10
    owner: Hiroshi Tanaka
    due: 2026-08-15
    status: watch
    blocking:
      - VE-MANIFEST-MY27
    last_updated: 2026-04-19
    tags: [voxos-china, dependency, vehicle-eng]

  - id: RAID-0007
    type: Risk
    title: Fallback OTA-only path adds ~$1.40/vehicle distribution cost
    description: >-
      If we miss the software freeze, the fallback is to ship the
      voice assistant as an OTA update post-SOP. Distribution cost is
      higher (carrier data) and adoption is materially lower (opt-in
      install vs default-on).
    severity: 3
    likelihood: 2
    score: 6
    owner: Sima Bagheri
    due: 2026-09-30
    status: watch
    last_updated: 2026-04-19
    tags: [voxos-china, contingency, cost]

  - id: RAID-0008
    type: Issue
    title: P1 — partner sandbox environment unstable
    description: >-
      Music.jp sandbox has been intermittently down for ~30% of test
      runs over the past 10 days. Blocking integration test
      automation. Reported by Music.jp ticket #JPMC-1142.
    severity: 2
    likelihood: 5
    score: 10
    owner: Akira Yamamoto
    due: 2026-04-25
    status: mitigating
    mitigation: >-
      Music.jp engineering aware; ETA on stable sandbox 2026-04-25.
      Local mock in use for the next 5 working days.
    last_updated: 2026-04-19
    tags: [voxos-china, partner, integration]

  - id: RAID-0009
    type: Risk
    title: Translation review backlog growing
    description: >-
      JP translation review queue is at 412 strings, growing ~80/week
      vs 60/week throughput. Reviewer is part-time contractor.
    severity: 2
    likelihood: 4
    score: 8
    owner: Maya Rivera
    due: 2026-06-01
    status: open
    last_updated: 2026-04-17
    tags: [japan, localization]

  - id: RAID-0010
    type: Risk
    title: Wake-word false-accept rate elevated in highway noise
    description: >-
      Internal eval shows 1.4% false-accept on highway-noise corpus
      vs 0.3% target. Likely fixable with a noise-conditioning pass
      on the wake-word model.
    severity: 3
    likelihood: 3
    score: 9
    owner: Chen Wei
    due: 2026-06-15
    status: open
    last_updated: 2026-04-12
    tags: [voxos-china, ml, wake-word]
---

# RAID Log — VoxOS China + Japan 2026

This log tracks risks, assumptions, issues, and dependencies for the VoxOS China and Japan voice-assistant programs. Rows in the YAML frontmatter validate against `schemas/raid-row.json`.

## How to use this log

- Add or update rows via `python scripts/raid_cli.py --log examples/raid/raid-log-voxos-china.md add ...` (see script `--help`).
- Validate schema: `python scripts/raid_cli.py --log examples/raid/raid-log-voxos-china.md validate`.
- Triage view (Now / This Week / This Month / Watch): `python scripts/raid_cli.py --log examples/raid/raid-log-voxos-china.md triage`.

## Notes

- All rows have a named human owner (no "team" or "leadership"). This is enforced by the schema's `minLength: 2` and reviewed manually.
- "Last reviewed" at the top is the most recent re-triage pass. Do this weekly. If older than 14 days, treat the log as stale.
- The triage script bucketizes by `due` date relative to today: ≤ today+1 = NOW, ≤ today+7 = THIS WEEK, ≤ today+30 = THIS MONTH, otherwise WATCH.

## Linked artifacts

- Charter: `examples/charters/charter-japan-launch-2026.md`
- Open decision: `examples/decisions/DM-0001-japan-launch-pause.md`
- Methodology: `docs/METHODOLOGY.md` (RAID skill canon and re-triage cadence)
