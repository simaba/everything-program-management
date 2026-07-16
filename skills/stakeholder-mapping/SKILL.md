---
name: stakeholder-mapping
description: >-
  Build a stakeholder analysis for a program or decision using power,
  interest, impact, legitimacy, and decision-role lenses. Produces an
  engagement plan, a deliverable-specific responsibility matrix, and a
  transparent decision path without treating stakeholder management as persuasion theater.
  TRIGGER when: the user needs to identify affected groups, decision rights,
  consultation order, or communication responsibilities.
  DO NOT TRIGGER when: the user only needs a distribution list or a message draft.
origin: community
---

# Stakeholder Mapping

A stakeholder map should improve decision quality and participation, not merely identify whom to “win over.” It should show:

- who can authorize, block, shape, implement, or be materially affected;
- what information each party needs and when;
- where representation or user voice is missing;
- which decisions require consultation, consent, notice, or formal approval;
- how disagreement will be surfaced rather than hidden.

## Use three complementary views

### 1. Stakeholder analysis

Power and interest are useful but incomplete. Add impact and legitimacy so low-power affected groups do not disappear from the analysis.

| Dimension | Question |
|---|---|
| **Decision authority** | Can this stakeholder approve, veto, fund, or stop the work? |
| **Operational influence** | Can they materially shape delivery, adoption, or quality? |
| **Interest** | How closely do they follow the outcome? |
| **Impact** | How strongly are they affected if the program succeeds or fails? |
| **Legitimacy / standing** | Do they have a formal, legal, ethical, or representative claim to participation? |
| **Current position** | supportive, conditional, undecided, concerned, opposed, unknown |
| **Evidence need** | What information would let them evaluate the proposal responsibly? |

Use a power/interest grid only as a communication-frequency aid. It should not override impact, rights, or required consultation.

### 2. Responsibility matrix

Use RACI or a similar model only for a specific deliverable or decision. A program-wide RACI with dozens of rows and columns usually creates false clarity.

- **Responsible:** performs the work.
- **Accountable:** owns the result or decision; normally one per row.
- **Consulted:** provides input before completion.
- **Informed:** receives the result or decision.

Add other roles when the situation demands them—for example **Approver**, **Reviewer**, **Control owner**, or **Affected representative**—rather than forcing every responsibility into RACI.

### 3. Decision path

Sequence the work needed to make a legitimate decision:

1. gather evidence and affected-user input;
2. resolve technical and operational feasibility questions;
3. complete required control reviews;
4. expose unresolved trade-offs to the decider;
5. record the decision and communicate consequences.

This is not a covert influence plan. Material objections, dissent, and affected-group concerns should remain visible in the decision record.

## Worked example: fictional library metadata pilot

All names, organizations, systems, and dates below are invented.

### Stakeholder analysis

| Stakeholder | Authority | Impact | Current position | Evidence need | Engagement |
|---|---|---:|---|---|---|
| Executive sponsor | Approves pilot scope and funding | Medium | Conditional support | cost, schedule, residual risk | Decision memo at two stage gates |
| Library operations lead | Owns catalog operations | High | Supportive | recovery process, training effort | Weekly working review |
| Data protection reviewer | Can block restricted-data flows | High | Undecided | data-flow diagram, deletion test, contract terms | Early control review; written disposition |
| Accessibility reviewer | Can withhold readiness recommendation | High | Concerned | keyboard, screen-reader, language results | Test-plan review before pilot |
| Archive staff representatives | No formal approval authority | High | Mixed | workload change, error-handling path | Two structured workshops; record dissent |
| Managed-service provider | Delivers external processing | Medium | Supportive | interface decisions, test schedule | Technical checkpoints; no internal decision role |
| Pilot users | No budget authority | High | Unknown | usability, correction path, support model | Representative research and feedback sessions |

### Responsibility matrix for pilot-readiness decision

| Deliverable | Product owner | Platform lead | Operations lead | Privacy reviewer | Accessibility reviewer | Sponsor |
|---|---|---|---|---|---|---|
| Pilot scope | R | C | C | C | C | A |
| Data-flow and deletion evidence | C | R | I | A | I | I |
| Operational recovery plan | C | C | A/R | I | I | I |
| Accessibility test report | C | C | C | I | A/R | I |
| Final pilot recommendation | R | C | C | C | C | A |

### Decision path

1. **Archive staff and pilot users:** validate workflow impact and correction needs.
2. **Platform and operations leads:** close feasibility and recovery questions.
3. **Privacy and accessibility reviewers:** issue written control dispositions.
4. **Product owner:** assemble options, residual risks, and recommendation.
5. **Executive sponsor:** decide pilot scope and conditions.
6. **All affected groups:** receive the decision, rationale, and escalation path.

## How to use the map

1. Start from decisions and affected outcomes, not an organization chart.
2. Identify people or groups with authority, operational influence, impact, or legitimate standing.
3. Record the current position as evidence, not assumption. Use `unknown` when you have not asked.
4. Define what each stakeholder needs to make a responsible contribution.
5. Use a responsibility matrix only where handoffs or approvals are genuinely ambiguous.
6. Design consultation before the decision deadline; avoid asking for input after the answer is effectively fixed.
7. Preserve material dissent in the decision record.
8. Revisit the map when scope, evidence, leadership, or affected populations change.

## Reviewer checklist

- [ ] The map includes materially affected groups, not only powerful approvers.
- [ ] Formal authority and informal influence are distinguished.
- [ ] Current positions are based on evidence or marked unknown.
- [ ] Required consultation, approval, and notice are separated.
- [ ] Responsibility matrices are deliverable-specific and have a clear accountable role.
- [ ] The decision path includes evidence and control review, not only executive pre-alignment.
- [ ] Material objections and dissent remain visible.
- [ ] Engagement frequency is proportional to decision need, not status hierarchy alone.

## Common failure modes

| Failure | Repair |
|---|---|
| Only senior leaders appear | Add affected users, operators, reviewers, and representatives with legitimate standing. |
| “Manage closely” becomes manipulation | Define the evidence, decision role, and transparent engagement needed. |
| Position is guessed from reputation | Ask, document, or mark unknown. |
| RACI contains multiple accountable parties | Split the deliverable or identify the actual decision owner. |
| Everyone is consulted on everything | Tie consultation to a specific decision or artifact. |
| Engagement begins after the preferred option is fixed | Move consultation earlier and record how input changes the option set. |

## Sources

- R. Edward Freeman, *Strategic Management: A Stakeholder Approach*.
- Mitchell, Agle, and Wood, “Toward a Theory of Stakeholder Identification and Salience,” for power, legitimacy, and urgency.
- PMI stakeholder-management guidance.
- Mendelow-style power/interest mapping, used here as one lens rather than a complete model.
