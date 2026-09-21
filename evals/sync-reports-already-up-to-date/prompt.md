---
name: sync-reports-already-up-to-date
description: vibe:sync must take Step 1's "already up to date" branch — nothing changed since index.md's date and the tree is clean — and stop without rewriting index.md, the module doc, or the glossary
tags: [sync, incremental, no-op]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:sync` skill (Skill tool, `skill: "vibe:sync"`) with no arguments. `.vibe/index.md` already exists in this workspace, so this must run in incremental mode, not a full regeneration.

Once it finishes, report in short plain sentences what it did and whether it changed anything.
