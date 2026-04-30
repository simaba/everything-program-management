# Security Policy

## Supported versions

This repository is primarily a program-management toolkit made of markdown assets, examples, schemas, and a lightweight Python utility package (`pmkit`).

Security attention is focused on:

- the latest `main` branch
- the packaged Python utility under `src/pmkit`
- GitHub Actions workflow files
- example artifacts and schemas that could be reused by downstream users

Older snapshots and forks may not receive fixes.

## Security scope

The main executable surface in this repository is limited to:

1. the `pmkit` Python package and CLI
2. GitHub Actions workflows
3. JSON Schema validation paths and example artifacts used in tests or CI

Most repository content is markdown guidance, templates, examples, commands, skills, and agents. Those files do not execute code by themselves, but they still matter from a trust and safety perspective because unsafe instructions or misleading defaults can be copied into downstream workflows.

## What to verify before reuse

Before using this repository in your own environment:

- review the Python utility code under `src/pmkit`
- review GitHub workflow files before enabling them in forks
- confirm public examples are safe for your context before adapting them
- pin to a reviewed commit if you vendor or mirror the repository internally

## Reporting a vulnerability

If you discover a security issue or safety-relevant problem, please do **not** disclose exploit details publicly.

Preferred options:

1. Use GitHub Private Vulnerability Reporting if it is available for the repository.
2. If private reporting is not available, open a minimal issue titled `[SECURITY] Private reporting request` without exploit details, or contact **bagherisima@gmail.com** with a concise summary and a request for a private channel.

Please include, where possible:

- affected file or component
- impact summary
- reproduction guidance shared privately
- suggested mitigation, if known

## Response targets

These are targets, not guarantees:

- acknowledgment within 7 days
- initial assessment within 14 days
- mitigation or fix timing based on severity and practicality

## Disclosure approach

Confirmed issues should be handled through coordinated disclosure. Public discussion should happen only after a fix, mitigation, or risk note is ready.
