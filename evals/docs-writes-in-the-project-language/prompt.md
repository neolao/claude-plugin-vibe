---
name: docs-writes-in-the-project-language
description: "/vibe:docs on a project whose CLAUDE.md names French under its Project language section (the README is already in French, the CHANGELOG and the code comments in English): the README managed sections and the docs/ files it writes must be in French, while the generated-file banner, the marker comments and the CLI commands stay verbatim. Requires --allow-tools Bash Write Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, language]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
