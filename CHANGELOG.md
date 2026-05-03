# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning where practical. Until the first stable release, minor versions may include structural changes to templates, schemas, examples, and utility behavior.

## [0.1.0] — Foundation release

### Added

- Repository entry layer with `AGENTS.md`, `CLAUDE.md`, and `docs/QUICKSTART.md`.
- Core program-management skills for chartering, executive briefing, stakeholder mapping, decision memos, RAID management, and chief-of-staff style briefing.
- Specialist agents for executive summarization, risk triage, and daily PM briefing.
- Reusable command prompts for common PM workflows.
- Markdown templates and worked examples for practical PM artifacts.
- JSON schemas for structured RAID rows and decision-memo frontmatter.
- `pmkit` Python utility package for validating supported structured artifacts.
- Example data under `examples/data/` for validated RAID and decision-memo workflows.
- Regression tests for schema validation and CLI behavior.
- CI workflow that runs tests and validates bundled examples across supported Python versions.
- Public-release checklist for sanitization and release-readiness review.
- Repository-specific security and contribution policies.

### Notes

This is a foundation release, not a finished PM operating system. The repo is intended as a reusable artifact-generation and validation layer beside existing tools such as Jira, Asana, Excel, Confluence, or similar systems of record.

### Next

- Add richer worked examples for stakeholder maps and decision memos.
- Add one additional structured schema for a charter or executive brief.
- Add optional CSV import/export helpers for RAID data.
- Add simple formatting helpers for validated artifacts.
