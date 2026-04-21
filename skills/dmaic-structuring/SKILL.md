---
name: dmaic-structuring
description: >-
  Structure a process-improvement project using DMAIC (Define,
  Measure, Analyze, Improve, Control) — the Six Sigma project
  framework. Produces a DMAIC plan with phase deliverables, gate
  criteria, and tooling recommendations per phase. Applies when the
  work is "a process isn't performing; fix it", not "build something
  new" or "make a decision".
  TRIGGER when: user says "DMAIC", "Six Sigma", "process improvement",
  "reduce defects in X", "cycle time", or describes a process with a
  persistent, measurable problem.
  DO NOT TRIGGER when: the work is building a new capability (use
  project-charter) or resolving a single incident (use
  post-mortem-facilitation).
origin: community
---

# DMAIC Structuring

Structure a process-improvement project using the five DMAIC phases — **Define, Measure, Analyze, Improve, Control** — with explicit gate criteria between each.

## When to Use

- An existing process has a persistent, measurable problem (defects, cycle time, cost, quality variation).
- The process has been "fixed" before but keeps regressing.
- You need a framework that a quality team, ops team, or Lean Six Sigma practitioner will recognize.

**Do not use** for:
- **New capability builds** → use `project-charter`.
- **One-off incident response** → use `post-mortem-facilitation`.
- **Strategic decisions** → use `decision-memo`.

## The Five Phases

From the Motorola / GE Six Sigma canon. Each phase has a question, deliverables, and a gate.

### D — Define

**Question**: What is the problem, and why does it matter?

**Deliverables**:
- Problem statement (one paragraph, time-bound, quantified)
- Business case (what's the cost of the current state?)
- Project charter (reuse `project-charter` skill)
- Scope boundaries (in/out, including which process steps)
- Stakeholder map (reuse `stakeholder-mapping` skill)

**Gate criterion**: Sponsor signs the problem statement and charter.

### M — Measure

**Question**: How is the process performing today, and can we measure it reliably?

**Deliverables**:
- Process map (SIPOC: Suppliers–Inputs–Process–Outputs–Customers)
- Measurement system analysis (MSA) — can we trust the data?
- Baseline performance: mean, standard deviation, capability (Cp, Cpk)
- Sample size justification

**Gate criterion**: Baseline performance is measured with documented MSA showing the measurement system is adequate (typically Gage R&R < 30%).

### A — Analyze

**Question**: What are the root causes of the gap between current and target performance?

**Deliverables**:
- Root cause analysis using one or more of:
  - **Ishikawa / fishbone diagram** — categorical brainstorm (6Ms: Method, Machine, Material, Measurement, Mother Nature, Manpower)
  - **5 Whys** — sequential drill-down
  - **Pareto analysis** — 80/20 of defect contributors
  - **Hypothesis testing** — statistical test that a candidate cause is significant
- Prioritized root cause list with evidence

**Gate criterion**: Top 3 root causes are identified with statistical or documented evidence (not opinion).

### I — Improve

**Question**: What changes will address the root causes, and will they work?

**Deliverables**:
- Candidate solutions (brainstormed, then filtered by impact × feasibility)
- Pilot design (small-scale test with pre-registered success criterion)
- Pilot results
- Full-rollout plan with rollback criteria

**Gate criterion**: Pilot shows statistically significant improvement against the target metric.

### C — Control

**Question**: How do we make sure the improvement sticks?

**Deliverables**:
- Control plan (which metrics we monitor, at what frequency, with what alerts)
- Standard operating procedure (SOP) updated
- Training plan for affected team
- Handover to process owner

**Gate criterion**: Process owner accepts the control plan; first 30 days of monitoring confirm performance holds.

## How It Works

1. **Classify the problem**. Is this truly a process problem? If yes, DMAIC fits. If no, pick a different skill.
2. **Set the target state**. The charter must specify current and target performance with numbers.
3. **Produce the D deliverables**. Review with sponsor; wait for sign-off before Measure.
4. **Produce the M deliverables**. Pay special attention to MSA — most DMAIC failures trace to bad measurement.
5. **Produce the A deliverables**. Use Ishikawa for a broad sweep, then Pareto + hypothesis tests to filter.
6. **Produce the I deliverables**. Always pilot before full rollout.
7. **Produce the C deliverables**. A DMAIC project isn't done at go-live; it's done after 30+ days of stable monitoring.

## Example

### Define

> **Problem**: In-cabin voice assistant intent misclassification rate rose from 8% to 14% over Q1 in the VoxOS China fleet, increasing support ticket volume by 22% and customer-reported dissatisfaction in the same period. Target: return to 8% by end of Q3, with 95% confidence bound below 10%.
>
> **Scope**: Voice intent pipeline from wake-word detection through intent classifier output. Excluded: dialog manager, TTS, third-party apps.

### Measure

> **Baseline**: 14.2% misclassification on a rolling 14-day window, n = 38K utterances. Cp = 0.41 (process is incapable). MSA: manual re-labeling inter-rater agreement κ = 0.82 — adequate.

### Analyze

> Ishikawa surfaced 22 candidate causes. Pareto on misclassified utterances showed:
> - 41% — domain-new slang terms (post-training drift)
> - 22% — acoustic variation in EV cabin noise profile
> - 15% — multilingual code-switching within utterance
> - 12% — user-specific pronunciations
> - 10% — long tail
>
> Top-3 root causes have >78% combined contribution. Hypothesis-tested at p < 0.01.

### Improve

> Candidate solutions ranked by impact × feasibility. Pilot: retrain classifier on 3-month sliding window of real traffic, plus synthetic cabin-noise augmentation. Pre-registered success: ≥ 4-pt reduction in misclassification rate on held-out set with p < 0.05.
>
> Pilot result: 8.9% misclassification, p = 0.003. Proceed to full rollout with staged deployment.

### Control

> Monitoring: weekly misclassification rate dashboard, alerted at > 10%. Retraining cadence: monthly. SOP updated. Process owner: ML Ops team lead. First 30-day check: 9.1% average, stable.

## Reviewer Checklist

- [ ] Problem statement is quantified with current and target values.
- [ ] Gate criteria are explicit and met before moving to next phase.
- [ ] Measurement system analysis is documented (MSA).
- [ ] Root causes have evidence — statistical, not opinion.
- [ ] Improvement is piloted before full rollout.
- [ ] Pilot has a pre-registered success criterion.
- [ ] Control plan has a named process owner.
- [ ] 30-day post-implementation check is scheduled.

## Common Failure Modes

| Failure | Repair |
|---|---|
| Skipping Measure to rush to Improve | Slow down. Bad data makes A and I worthless. |
| MSA shows > 30% Gage R&R but teams improve anyway | Fix measurement first. You can't improve what you can't reliably measure. |
| Ishikawa with 60 causes, no prioritization | Apply Pareto. Filter to top 3–5. |
| Rollout without a pilot | Reject. DMAIC requires empirical evidence before scaling. |
| No handover to process owner | Project will regress. Force a named owner and a 30-day check-in. |

## Source

- Mikel Harry and Richard Schroeder, *Six Sigma: The Breakthrough Management Strategy*, chapter on DMAIC.
- Motorola Six Sigma training materials (DMAIC as standard project form).
- George, *Lean Six Sigma for Service* — DMAIC applied outside manufacturing.
- Kaoru Ishikawa, *Guide to Quality Control* — fishbone / 6Ms origin.
