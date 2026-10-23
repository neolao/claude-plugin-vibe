---
name: docs-leaves-an-up-to-date-doc-unchanged
description: "Precision side of docs-rewrites-a-doc-whose-module-changed: docs/architecture.md was committed after the last change to the code it describes and nothing changed since, so a run with no argument must leave the file byte-for-byte as it is, write nothing to it, and report it unchanged. Requires --allow-tools Bash Write Edit to run (the skill reads git and writes README.md and docs/ files)."
tags: [docs, incremental, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
