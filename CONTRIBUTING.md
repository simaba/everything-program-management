# Contributing

Thanks for your interest in improving this repository.

`everything-program-management` is a reusable toolkit for structured program-management artifacts. Good contributions should make the repo more useful, more reusable, and more trustworthy for real PM workflows.

## What belongs here

Contributions are especially welcome when they add:

- reusable PM templates
- worked examples with generic, public-safe content
- clearer skill or agent instructions
- schema improvements for structured PM artifacts
- small validation utilities for existing schemas and examples
- tests and CI improvements
- documentation that makes the repo easier to adopt

## What does not belong here

Please avoid contributions that are primarily:

- personal career notes or job-search material better suited to another repo
- company-specific internal templates copied from private work contexts
- essay-only content presented as if it were operational tooling
- vague frameworks without a clear PM use case
- duplicated assets that overlap with an existing template, skill, or command without a clear differentiator

## Contribution principles

Optimize for:

- **reusability**: public-safe and easy to adapt
- **clarity**: outputs should be structured and decision-oriented
- **traceability**: owners, dates, assumptions, and open risks should be visible
- **honest maturity**: do not describe planned capabilities as shipped capabilities

## How to contribute

### 1. Open an issue first

Before opening a pull request, describe:

- what you want to add or change
- why it improves the repository
- which existing folder it best fits into
- whether it introduces a new template, example, schema, command, skill, or utility

### 2. Keep examples public-safe

All contributed examples should be:

- generic or fictional
- free of confidential employer or customer information
- free of real personal data
- safe to reuse in a public template context

### 3. Match the repository structure

Use the current structure intentionally:

- `templates/` for reusable artifact shapes
- `examples/` for filled public-safe examples
- `skills/` for method guidance
- `agents/` for role-based orchestration
- `commands/` for direct entry prompts
- `schemas/` for structured artifact validation
- `src/pmkit/` for lightweight utility code
- `docs/` for guidance and adoption notes

### 4. If you add a new skill

A good skill should:

- solve a recognizable PM problem
- explain when to use it and when not to use it
- provide a reviewer checklist or quality bar
- align to the repository’s practical PM focus
- include or reference at least one worked example when possible

### 5. If you add code or schemas

Please also:

- add or update tests where practical
- keep the implementation lightweight and readable
- avoid introducing unnecessary third-party dependencies
- ensure examples validate if the repo claims they do

## Pull request checklist

Before submitting a PR, verify:

- [ ] the change fits the repository purpose
- [ ] README claims still match what is actually shipped
- [ ] examples are generic and public-safe
- [ ] new files are placed in the correct folder
- [ ] tests pass if code or schemas changed
- [ ] the contribution does not duplicate an existing artifact without a clear reason

## License

By contributing, you agree that your contributions will be licensed under the MIT license in this repository.
