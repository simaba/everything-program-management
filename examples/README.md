# Examples

Worked examples of the artifacts this plugin produces. Use them as references when calling the corresponding skills.

| File | Skill | Schema |
|---|---|---|
| `charters/charter-japan-launch-2026.md` | `project-charter` | — |
| `raid/raid-log-voxos-china.md` | `raid-log` | `schemas/raid-row.json` |
| `decisions/DM-0001-japan-launch-pause.md` | `decision-memo` | `schemas/decision-memo-frontmatter.json` |

The three examples are deliberately cross-linked: the charter seeds risks into the RAID log, and the open RAID issue (RAID-0003) is the trigger for the decision memo. This shows how the artifacts compose in practice.

## Running the schema validators

```bash
python scripts/raid_cli.py --log examples/raid/raid-log-voxos-china.md validate
python scripts/raid_cli.py --log examples/raid/raid-log-voxos-china.md triage
python scripts/decision_journal_review.py --dir examples/decisions/
```

All three commands should succeed against the bundled examples. If you fork or adapt the examples, re-run `validate` to confirm the schema still hold