---
name: sync-incremental-scopes-to-changed-files
description: vibe:sync in incremental mode must update .vibe/modules/auth.md for a new uncommitted export while leaving .vibe/modules/billing.md byte-for-byte untouched, refresh index.md's stale date, and drop the glossary entry whose cited source no longer exists while keeping the one whose source is live. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [sync, incremental]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:sync` skill (Skill tool, `skill: "vibe:sync"`) with no arguments. `.vibe/index.md` already exists in this workspace, so this must run in incremental mode, not a full regeneration.

Once it finishes, report in short plain sentences: which mode it ran in, which module(s) it updated and why, which module(s) it left untouched, and any glossary term it added, redefined, or removed.
