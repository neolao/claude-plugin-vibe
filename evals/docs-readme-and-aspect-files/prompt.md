---
name: docs-readme-and-aspect-files
description: "/vibe:docs must rewrite only the managed README sections with real content derived from the manifest/CHANGELOG, leave hand-written README content byte-for-byte untouched, and create docs/architecture.md for a project with several identifiable modules. Requires --allow-tools Bash,Write,Edit to run (the skill writes README.md and docs/ files)."
tags: [docs, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

Once it finishes, report exactly what it changed.
