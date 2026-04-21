# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-04-19 — Initial Release

### Added
- 12 PM skills: `mece-decomposition`, `pyramid-principle`, `scr-narrative`, `raid-log`, `stakeholder-mapping`, `project-charter`, `dmaic-structuring`, `decision-memo`, `post-mortem-facilitation`, `chief-of-staff-brief`, `executive-summary-brief`, `risk-triage`.
- 4 agents: `chief-of-staff-brief`, `executive-summary`, `risk-triage`, `stakeholder-mapper`.
- 8 slash commands: `/charter`, `/raid-update`, `/exec-brief`, `/decision-memo`, `/post-mortem`, `/stakeholder-map`, `/pyramid`, `/mece`.
- 7 always-on rules covering Pyramid-first, MECE compliance, named methods, multi-option decision memos, blameless post-mortems, TBD-over-fabrication, and one-page exec briefs.
- 3 contexts: `pm-mode`, `executive-mode`, `crisis-mode`.
- 3 JSON schemas for RAID rows, decision-memo frontmatter, and post-mortem templates.
- Python helpers: `raid_log_cli.py` and `decision_journal.py`.
- `install.sh` and `install.ps1` installers.
- Worked examples under `examples/`.
- Plugin manifest (`.claude-plugin/plugin.json`) and marketplace entry.
