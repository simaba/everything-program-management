# Public Release Checklist

Use this checklist before changing repository visibility or creating a public release.

## Repository content

- [ ] Confirm every example is fictional, generic, or fully sanitized.
- [ ] Search all tracked files for employer, customer, supplier, project, product, colleague, and location names.
- [ ] Remove real RAID entries, decision memos, steering material, HR content, commercial terms, financial data, and internal escalation details.
- [ ] Confirm no prompts, agent instructions, templates, or screenshots expose non-public processes or systems.
- [ ] Confirm no personal data, credentials, API keys, tokens, or connector identifiers are present.

## GitHub surfaces

- [ ] Review default and non-default branches.
- [ ] Review full commit history before publicizing; remove or rewrite sensitive history before visibility changes where necessary.
- [ ] Review open and closed pull requests, issues, comments, review threads, releases, tags, wiki pages, and discussions.
- [ ] Review GitHub Actions logs, workflow artifacts, caches, and uploaded screenshots or attachments.
- [ ] Review repository description, topics, homepage, social preview image, and contributor metadata.

## Quality baseline

- [ ] README explains purpose, intended audience, quick start, maturity, and non-goals.
- [ ] `CHANGELOG.md` and the release notes accurately describe the publication snapshot.
- [ ] CI is green on the release commit.
- [ ] Example artifacts validate with `pmkit`.
- [ ] Links in public-facing documentation work.
- [ ] License, security policy, and contribution guidance are discoverable.

## Release decision

- [ ] Record the reviewed commit SHA and reviewer/date in the release notes or release description.
- [ ] Create the version tag and GitHub Release as a draft first.
- [ ] Check release notes and assets before publishing.
- [ ] Once published, correct mistakes in a new version rather than altering the published release artifact.

This checklist helps prepare a repository for public sharing; it does not replace legal, security, privacy, or employer-specific review.