---
name: docs-does-not-invent-features-on-a-scaffold
description: "Precision side of docs-derives-features-from-the-code-without-changelog: /vibe:docs on a bare scaffold (manifest, an empty entry point, a placeholder test, no README, no CHANGELOG, no docs/) as /vibe:init leaves it. It must create the README with its four managed sections, say in the features section that there is nothing yet instead of inventing capabilities from the manifest description, create neither a changelog nor a docs/ folder, and index no documentation. Requires --allow-tools Bash Write Edit to run (the skill writes README.md)."
tags: [docs, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
