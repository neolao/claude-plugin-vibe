---
name: docs-leaves-a-missing-marker-pair-absent
description: "/vibe:docs on a README that carries three of the four marker pairs (no docs-index pair) while docs/ holds a generated file worth indexing: it must rewrite the three sections present, report the documentation index as absent, and never insert the missing pair — not at the end of the file, not anywhere — nor ask the question meant for a fully hand-written README. Requires --allow-tools Bash Write Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, markers]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
