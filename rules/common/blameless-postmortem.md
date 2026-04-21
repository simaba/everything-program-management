# Rule: Blameless Post-Mortem

**Always load when post-mortem skill is active.**

Post-mortems are blameless. Personal names do not appear in failure contexts. The system failed, not the person.

## Rule

In any post-mortem the harness produces:

1. **Names do not appear next to failures.** "The deploy was triggered" — not "Name triggered the deploy."
2. **System framing is required.** If a single individual could have prevented the incident, the system let them. Document the system gap, not the individual.
3. **Names do appear** in "what worked" contexts (who detected, who responded, who shipped the fix). Crediting good work is mandatory.
4. **Action items are about systems**, not behavior change. "Train people to be more careful" is rejected; "require schema-migration warnings to block deploys until manually ack'd" is acceptable.

This is non-negotiable. It is not a stylistic preference; it is the entire reason post-mortems produce learning rather than political fiction.

## Why

Without blamelessness:
- People hide near-misses.
- People stop reporting what they were thinking during the event.
- Latent issues never surface.
- The post-mortem becomes a document about who was unlucky.

With blamelessness, the post-mortem produces transferable lessons. That is the only thing it's for.

## Application

The harness must, before publishing a post-mortem:

1. Scan for personal names in failure contexts. Rewrite each in system terms.
2. Scan action items for behavior-change language ("train", "be more careful", "remember to"). Rewrite as system controls.
3. Verify the timeline records what was *observable* (timestamps, log entries, alerts), not what was *judged* in retrospect about anyone's actions.

## Counter-examples the harness should reject

- "Sara missed the warning."
  → "The deploy pipeline did not surface the warning at a level requiring acknowledgment."
- "The on-call should have escalated sooner."
  → "Escalation criteria were not encoded in the runbook; the on-call relied on judgment."
- "Action item: Be more careful with schema migrations."
  → "Action item: Require schema-migration warnings to block the deploy until ack'd."

## When a name unavoidably must appear in a failure context

Rare. Real cases: a leadership decision that materially changed the program direction, named in a contributing factor. Even then, the framing is about the decision and its system context, not the person.

## Source

- John Allspaw (Etsy), "Blameless PostMortems and a Just Culture," 2012.
- Sidney Dekker, *The Field Guide to Understanding Human Error*.
- Google SRE book, post-mortem chapter.
- NTSB-style aviation accident investigations.
