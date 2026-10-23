---
name: workspace-init-leaves-hub-items-and-adrs-alone
description: >-
  vibe:workspace-init on a refresh must leave the hub's existing backlog item and ADR untouched and add no placeholder next to them, while registering the new sibling. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, refresh, commit, precision]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds three git repos: `orders-api/`, `orders-web/` and `roadmap/`, the last
one being the workspace's hub repo, which already holds a backlog item and
an ADR.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Removing or archiving a repo: `no, keep it`. Status of a repo that needs
one: `planned`. Role of a repo that needs one: `Storefront web app`. If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes`
to close it out quickly.

Once the skill has finished (or otherwise concluded), run
`git -C roadmap ls-files .vibe` with the Bash tool and include its raw
output in your final message. Then report, in short plain sentences, what
the skill did.
