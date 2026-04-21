# Security

## What this plugin can and cannot do

This is a **markdown-only** plugin. It does not execute code on install. The only executable surface is:

1. `install.sh` / `install.ps1` — copies files into your Claude config directory. Read it before running.
2. `scripts/raid_log_cli.py` and `scripts/decision_journal.py` — small Python helpers you opt into running. They read/write local markdown files only and make no network calls.

The skills, agents, commands, and rules are all instructions to Claude. They don't ship executable code that runs on your machine.

## What you should still verify

- Pin to a reviewed commit when vendoring (`git checkout <full-sha>`).
- Read any new skill before merging — a malicious skill could instruct the model to do harmful things.
- The Python helpers run with your user permissions. Read them.

## Reporting a vulnerability

If you find a way that this plugin could be abused — for example, a skill that could lead the model to exfiltrate data or perform destructive actions — email **bagherisima@gmail.com** with:

- A description of the issue
- Steps to reproduce
- Suggested mitigation (if any)

I'll acknowledge within 7 days and aim to ship a fix or mitigation within 30 days for high-severity issues.

Please do **not** file public GitHub issues for security reports.
