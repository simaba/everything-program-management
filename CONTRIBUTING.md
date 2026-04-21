# Contributing

Thanks for your interest. This repo has a high bar for new skills and a lower bar for examples and bug fixes.

## What's in scope

**Yes, please:**
- New skills that codify a *named* PM method with a citation (Minto, Six Sigma, Ishikawa, McKinsey-style frameworks, Reforge frameworks, Lenny-canon frameworks, etc.)
- New worked examples under `examples/` showing real artifacts produced by the skills
- New rules that catch common PM antipatterns (buried lede, single-option memo, etc.)
- Translations of skill descriptions into other languages
- Adapter patches for non-Claude harnesses (Codex, Cursor, Gemini)
- Schema additions or tightenings

**No, thanks:**
- Skills that codify "vibes" or unnamed frameworks
- Skills that compete with an existing skill without a clear differentiator
- Anything that requires a paid SaaS to function (this is a pure markdown plugin by design)
- Decks, infographics, "thought leadership" — write a Medium post, link it from `docs/`

## How to add a skill

1. Pick a method that isn't already covered. Run `ls skills/` to check.
2. Copy `examples/_skill-template/SKILL.md` to `skills/<your-skill-name>/SKILL.md`.
3. Fill in the frontmatter — `name`, `description` with `TRIGGER when:` and `DO NOT TRIGGER when:` clauses, `origin`.
4. Write the body. Required sections: `When to Use`, `How It Works`, `Examples`, `Reviewer Checklist`, `Source` (the citation).
5. Add at least one worked example to `examples/`.
6. Add the skill name to the table in `README.md`.
7. Open a PR with a one-line description.

## How to add an agent

1. Agents compose multiple skills. If your work fits one skill, write a skill, not an agent.
2. Copy the format of `agents/chief-of-staff-brief.md`.
3. The agent's frontmatter must declare its `tools` and a `model` (haiku for triage, sonnet for default, opus for synthesis).
4. The agent's body must explain *which skills it loads* and *in what order*.

## Style

- Match the voice in `SOUL.md`.
- Run markdownlint locally (`npx markdownlint-cli '**/*.md'`).
- Keep top-level files short. Long content goes under `docs/`.

## License

By contributing, you agree your contributions are licensed under the MIT license (`LICENSE`).
