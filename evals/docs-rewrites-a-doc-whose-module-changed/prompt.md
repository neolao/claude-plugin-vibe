---
name: docs-rewrites-a-doc-whose-module-changed
description: "/vibe:docs with no argument on a repository where docs/architecture.md was committed with the 1.3.0 release and a later commit added an export module and command: the incremental rule must find that commit after the doc's own and rewrite the doc so it covers the export module, keeping the banner. Requires --allow-tools Bash Write Edit to run (the skill reads git and writes README.md and docs/ files)."
tags: [docs, incremental]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
