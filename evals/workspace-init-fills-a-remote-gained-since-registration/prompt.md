---
name: workspace-init-fills-a-remote-gained-since-registration
description: >-
  vibe:workspace-init must fill a `—` Remote cell from the repo's origin gained since registration, and change nothing else in the registry — status, role, the other row, the naming convention. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, refresh, human-edits, precision]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds three git repos: `orders-api/`, `orders-web/` and `roadmap/`, the last
one being the workspace's hub repo.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Removing or archiving a repo: `no, keep it`. Status of a repo that needs
one: `planned`. Role of a repo that needs one: `Storefront web app`. If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes`
to close it out quickly.

Once the skill finishes, report back what it did.
