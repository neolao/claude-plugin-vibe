---
name: sync-incremental-adds-new-zone-and-keeps-glossary-clean
description: vibe:sync in incremental mode must document a brand-new uncommitted source zone (module, model, index line, domain glossary term) without promoting implementation plumbing to a glossary term, and leave the untouched billing module unchanged. Requires --allow-tools Bash,Write,Edit.
tags: [sync, incremental]
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:sync` skill (Skill tool, `skill: "vibe:sync"`) with no arguments. `.vibe/index.md` already exists in this workspace, so this must run in incremental mode, not a full regeneration.

Once it finishes, report in short plain sentences: which mode it ran in, which module(s) it created or updated, which it left untouched, and any glossary term it added, redefined, or removed.
