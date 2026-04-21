# RULES.md — Index

The rules under `rules/common/` are loaded automatically by the harness on every session. They are *constraints*, not preferences. Listed here for transparency.

| Rule | What it enforces |
|---|---|
| `pyramid-first.md` | Every artifact opens with the answer. No buried lede. |
| `mece-before-lists.md` | Bullet lists must pass MECE check (mutually exclusive, collectively exhaustive). |
| `cite-the-method.md` | Named methods (Minto, SCR, MECE, DMAIC, Ishikawa) must be cited when used. |
| `no-single-option-memo.md` | Decision memos require ≥2 options or explicit single-option justification. |
| `blameless-post-mortems.md` | Post-mortems forbid blame language and individual attribution. |
| `tbd-over-fabrication.md` | Unknown values get `[TBD: <what>]` placeholders, never fabricated data. |
| `exec-brief-one-page.md` | Exec briefs default to one page unless the user explicitly requests longer. |

To disable a rule for a specific session, the user can prefix their request with `--rule-off=<name>`. To disable globally, comment out the corresponding line in `manifests/install-modules.json`.
