---
name: init-merges-stacks-and-honors-keep-on-template-section
description: vibe:init must regenerate CLAUDE.md for a two-stack repo (Python API at the root, TypeScript front end in web/) — covering both stacks' test commands, re-deciding stale review-agent rows from the real code, and keeping a hand-written <!-- keep --> section even when it sits on a heading the template also defines (requires --allow-tools to run — Bash, Write, Edit)
tags: [init, regeneration, multi-stack]
runs: 3
max_turns: 60
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion]
---

This is an existing project at the root of your working directory: a Python
service (`pyproject.toml`, `src/shop_api/`, `tests/`), a TypeScript front end
in `web/` with its own `package.json`, and a `CLAUDE.md` left over from an
earlier `/vibe:init` run.

Invoke the `vibe:init` skill (Skill tool, `skill: "vibe:init"`) to regenerate
this project's `CLAUDE.md`.

If asked what language generated content should be written in, answer
English. If asked whether a locally-run instance should be probed for web
security, answer no. For any other `AskUserQuestion` prompt, answer with a
reasonable default and move on — the goal is to let the skill finish, not to
explore every option.

Once the skill finishes, report back what it did.
