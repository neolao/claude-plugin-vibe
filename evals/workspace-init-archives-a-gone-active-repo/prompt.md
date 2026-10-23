---
name: workspace-init-archives-a-gone-active-repo
description: >-
  vibe:workspace-init must offer to archive an active repo whose directory is gone, and write the archived status in its row when the user chooses it, instead of removing the row or leaving it active. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, refresh, archived]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds two git repos: `orders-api/` and `roadmap/`, the latter being the
workspace's hub repo.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. A listed repo whose directory is gone: `archive it`. Status of a repo
that needs one: `planned`. Role of a repo that needs one: `Nightly invoice
batch job`. If a `vibe:clarify` sub-flow starts probing with rounds of
questions, answer `yes` to close it out quickly.

Once the skill finishes, report back what it did.
