# CLAUDE.md — Project Instructions

This repository provides program-management methods, templates, examples, and structured validators. Use the repository to produce decision-ready artifacts, not generic management prose.

## Operating principles

1. **Start from the decision or outcome.** Lead with the recommendation, changed condition, or question the artifact must support.
2. **Preserve evidence quality.** Distinguish measured facts, estimates, assumptions, interpretations, and unknowns.
3. **Use a named method only when it adds constraints.** MECE, SCR, RAID, RACI, 5 Whys, DMAIC, and similar methods are tools—not badges. Do not name-drop a framework when a simpler structure is clearer.
4. **Expose trade-offs and uncertainty.** Avoid false certainty, hidden hard constraints, straw alternatives, and precision without provenance.
5. **Keep decision rights explicit.** Name the accountable decision owner, action owner, review date, and escalation trigger where relevant.
6. **Validate structured artifacts.** Use the schemas under `schemas/` for supported RAID and decision-memo fields. Do not invent fields that break the contract.
7. **Run the skill’s reviewer checklist.** Treat it as a quality check, not a reason to force every situation into the same format.
8. **Protect private information.** Public examples must be fictional, generic, or fully sanitized. Do not adapt internal-looking scenarios by merely changing names.

## Writing standard

- Prefer specific nouns, verbs, evidence, and consequences over slogans.
- Do not write management filler such as “drive alignment,” “unlock value,” or “leverage synergies” without saying what action or outcome is meant.
- Use uncertainty language when the evidence is uncertain. Hedging is a problem only when it avoids a judgment; it is required when confidence is limited.
- Keep artifacts as short as their decision purpose allows. A one-page brief is a useful default, not a license to remove material caveats.
- Cite source records, methods, or external references when they are load-bearing.
- Do not claim a framework is standard, best practice, or validated without a credible source.

## Artifact selection

- Use a **charter** for authorization, scope, decision rights, and success measures.
- Use a **RAID log** for persistent risks, assumptions, issues, and dependencies.
- Use **risk triage** for the temporary time-to-action view of changed RAID items.
- Use a **decision memo** for a consequential unresolved choice with real alternatives.
- Use an **executive brief** for a decision, exception, progress change, or explicit FYI.
- Use a **chief-of-staff brief** for the reader’s near-term attention and preparation.

Do not merge several artifact types into one vague “strategy document.” Compose them and preserve their distinct purposes.

## When information is missing

Ask only the clarifying questions that materially change the artifact. When a useful draft can still be produced, mark missing fields as `[TBD: ...]`, state the assumption, and avoid fabrication.

## Code and automation

Program-management work can include schemas, validation, data transformation, or lightweight automation. Use code when it materially improves reliability or repeatability; do not assume the user wants prose instead of an executable artifact.
