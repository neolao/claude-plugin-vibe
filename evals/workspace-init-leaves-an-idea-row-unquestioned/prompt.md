---
name: workspace-init-leaves-an-idea-row-unquestioned
description: >-
  vibe:workspace-init must leave an idea row alone on a refresh — no removal or archiving question, no change — since an idea has no repo directory by definition. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, refresh, archived, precision]
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
end. A listed repo whose directory is gone, whether the question is to remove
or to archive it: `remove it`. Status of a repo that needs one: `planned`.
Role of a repo that needs one: `Shared TypeScript client`. If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes`
to close it out quickly.

Once the skill finishes, report back what it did.
