---
name: workspace-init-refreshes-registry-and-keeps-human-edits
description: vibe:workspace-init must refresh an existing hub from the workspace root — keep the human status and role of an already-listed repo, auto-register a new sibling that has .vibe/backlog/, ask before dropping a listed repo that is gone, and commit with the refresh message, not the bootstrap one (requires --allow-tools — Bash, Write, Edit)
tags: [workspace-init, refresh]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds three git repos: `orders-api/`, `orders-web/` and `roadmap/`.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Removing a repo from the registry: `no, keep it`. Status of a repo that
needs one: `planned`. Role of a repo that needs one: `Storefront web app`. If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes` to
close it out quickly.

Once the skill finishes, report back what it did.
