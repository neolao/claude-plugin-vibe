---
name: docs-derives-features-from-the-code-without-changelog
description: "/vibe:docs on a project that has managed README sections but no CHANGELOG.md at all (the state /vibe:init hands it on a repo that never kept one): the features section must still be filled, from what the code and the manifest let the user do, without creating a changelog to read and without leaving the placeholder. Requires --allow-tools Bash Write Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, sources]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
