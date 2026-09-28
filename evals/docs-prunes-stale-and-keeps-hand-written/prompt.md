---
name: docs-prunes-stale-and-keeps-hand-written
description: "/vibe:docs on a project whose docs/ already exists: it must delete the generated doc whose aspect left the code, leave the hand-written doc and the non-Markdown assets untouched, rebuild the docs index from what docs/ really holds, and drop the removed capability from the README features. Requires --allow-tools Bash Write Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
