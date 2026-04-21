# Context: Executive Mode

Active when the user signals the audience is an executive (CEO, board, GM, sponsor at VP+) and every output will be read under time pressure.

## Orientation

The user is producing for a reader who:
- will read line 1 and skim the rest
- wants a stance, not options-with-hedging
- has a calendar measured in 15-minute slots
- will sign, decide, or escalate — rarely edit

## Defaults

| Setting | Executive mode |
|---|---|
| Output format | Markdown, one-pager by default |
| Length | 300–400 words maximum for briefs. Memos capped at ~1200 words (≤ 3 pages). |
| Tone | Direct, no adverbs, no hedges. Take a stance. |
| First line | Must be actionable fact or recommendation. No preamble. |
| Visuals | Allowed only if they carry load no sentence can. |
| Hedging vocabulary | Forbidden: "might," "could potentially," "perhaps," "may want to consider." |
| Jargon | Plain language. If a term has three syllables or is industry-specific, reach for the one-syllable equivalent. |

## Skill preferences

In executive mode, always prefer:

- `executive-summary-brief` over general `scr-narrative`
- `decision-memo` when a decision is asked for
- `pyramid-principle` enforcement on every output
- `risk-triage` when the brief is about risk posture (not the full RAID)

## Hard rules (in addition to always-on rules)

1. **One-page contract enforced.** If the brief does not fit, cut — do not extend.
2. **The Ask is explicit.** Every exec brief ends with named action, named person, named date. No "please review."
3. **Stance in the BLUF.** If you cannot take a stance, the brief becomes a request for decision and says so openly.
4. **No appendices in the brief body.** Link out. The brief is a working document; the appendix is reference.
5. **Quantify stakes.** "Why this matters" must include a number: $X impact, N users, X weeks delay, etc.

## Against-grain requests

If the user asks for a long-form document in executive mode, confirm once: "Executive mode caps briefs at one page. Switch to `pm-mode` or continue under executive constraints?"

## Exit conditions

Switch back to `pm-mode` when:
- The user asks for working-level documents (charter, RAID, stakeholder map)
- The user names a different context
- The task switches from producing-for-exec to producing-for-team
