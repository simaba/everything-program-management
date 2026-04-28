# Public Release Checklist

Use this checklist before making the repository public or before publishing a release.

## 1. Confidentiality and privacy scan

Confirm the repository does not contain:

- employer-specific confidential information
- customer, employee, candidate, or recruiter personal data
- internal project names that should not be public
- private meeting notes or unpublished business decisions
- credentials, tokens, API keys, or secrets
- salary, visa, immigration, or offer details
- proprietary templates copied from an employer

Suggested local scan:

```bash
git grep -n -i "confidential\|internal only\|do not share\|password\|api_key\|secret\|token\|salary\|offer\|visa\|passport\|recruiter\|email"
```

## 2. Example safety

All examples should be:

- generic
- fictional
- free of real company names unless intentionally cited as public examples
- free of real people, private email addresses, and internal project data
- safe to reuse as public templates

## 3. Claim accuracy

Confirm the README only claims what is actually shipped.

- If a command is documented, it should run.
- If a schema is listed, an example should exist.
- If CI is mentioned, the workflow should exist.
- If a template is listed, the file should be present.
- If a feature is planned but not shipped, it belongs under "Next maturity step."

## 4. Repository health

Before public release, verify:

- [ ] `LICENSE` exists
- [ ] `README.md` explains status and scope
- [ ] `docs/QUICKSTART.md` gives a first-use path
- [ ] CI passes
- [ ] examples are generic and validated where possible
- [ ] package metadata is present if code exists
- [ ] no generated artifacts or local cache files are committed

## 5. Positioning

This repository should be positioned as:

> a reusable program-management harness for structured artifacts, templates, skills, and lightweight validation utilities.

It should not be positioned as:

- a replacement for a project-management system of record
- legal, HR, financial, or compliance advice
- a guarantee of project success
- a complete PM methodology certification program

## 6. Final release note

Before publishing, add or update a short release note summarizing:

- what is included today
- what is intentionally out of scope
- what should be improved next
