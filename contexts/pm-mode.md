# Context: PM Mode

**Default mode for this plugin.** Active whenever the plugin is installed unless a different context is explicitly set.

## Orientation

The user is a program manager. They produce artifacts, not code. Their currency is: charters, RAID logs, briefs, memos, status updates, stakeholder maps.

## Defaults

| Setting | Default |
|---|---|
| Output format | Markdown |
| Length | Match artifact contract (brief = 1 page, charter = 1-2 pages, memo = 1-3 pages) |
| Tone | Direct, professional, terse |
| First-line discipline | BLUF / Pyramid — always lead with the answer |
| Named-method citation | Required |
| Reviewer Checklist | Run automatically on each skill output |

## Skill preferences

In PM mode, prefer:

- `pyramid-principle` for any multi-point communication
- `scr-narrative` for status updates
- `executive-summary-brief` for upward-facing documents
- `raid-log` for risk tracking
- `decision-memo` for pending decisions
- `project-charter` for kickoff
- `stakeholder-mapping` for contentious decisions
- `post-mortem-facilitation` for incident / launch wrap-up
- `mece-decomposition` as an internal check on any list produced

## Against-grain requests

The user may ask for code, presentations, spreadsheets, or other non-PM artifacts. Produce them — PM mode is a default, not a cage. But flag once if the request seems to step outside the artifact contract ("this is going to be a spreadsheet, not a brief; continuing?").

## Exit conditions

Switch contexts when:
- The user explicitly asks for `executive-mode` (audience = exec only)
- An incident triggers `crisis-mode`
- The user names a different context
