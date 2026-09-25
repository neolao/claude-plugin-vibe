---
name: init-regenerates-while-preserving-keep-sections
description: vibe:init must regenerate CLAUDE.md from the real pyproject.toml/src layout while preserving a hand-written <!-- keep --> section verbatim, and must invoke vibe:sync afterward (requires --allow-tools to run — Bash, Write, Edit)
tags: [init, regeneration]
runs: 3
max_turns: 50
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion]
---

This is an existing Python project at the root of your working directory: a
real `pyproject.toml`, a `src/acme_widgets/` package, a `tests/` directory,
and a `CLAUDE.md` left over from an earlier `/vibe:init` run.

Invoke the `vibe:init` skill (Skill tool, `skill: "vibe:init"`) to regenerate
this project's `CLAUDE.md`.

If asked what language generated content should be written in, answer
English. For any other `AskUserQuestion` prompt, answer with a reasonable
default and move on — the goal is to let the skill finish, not to explore
every option.

Once the skill finishes, report back what it did.
