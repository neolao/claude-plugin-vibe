---
name: workspace-init-bootstraps-hub-and-registers-siblings
description: vibe:workspace-init must bootstrap a new hub repo from a bare workspace root holding two sibling repos, auto-classifying the one with .vibe/backlog/ as active and asking about the one without, then commit only the hub's own files (requires --allow-tools to run — Bash, Write, Edit)
tags: [workspace-init, bootstrap]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion]
---

You are at the root of a workspace folder (it is not itself a git repo) that
holds two sibling repos, `orders-api/` and `orders-sdk/`. No hub repo exists
yet anywhere in this workspace.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with the argument `roadmap` as the hub directory name.

If asked for a new sibling's status and role (`orders-sdk` has no `.vibe/`
yet, so it should be asked about rather than auto-classified), answer
`planned` with a one-line role of your choosing. If asked for the
workspace's purpose or vision, answer in one or two plain sentences. If a
`vibe:clarify` sub-flow starts probing with further rounds of questions,
answer `yes` to close it out quickly rather than exploring every branch.

Once the skill finishes, report back what it did.
