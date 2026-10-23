---
name: docs-keeps-english-without-a-project-language
description: "Precision side of docs-writes-in-the-project-language: CLAUDE.md has no Project language section but says the team is French-speaking and the stored labels are French; the README is in English. The language rule must fall back to the README's own language — the managed sections and docs/architecture.md come out in English, banner verbatim. Requires --allow-tools Bash Write Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, language, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
