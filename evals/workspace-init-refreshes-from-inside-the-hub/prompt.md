---
name: workspace-init-refreshes-from-inside-the-hub
description: >-
  vibe:workspace-init run from inside the hub repo must refresh the registry in place — register the new sibling, keep the existing row, commit with the refresh message — and write the workspace-root CLAUDE.md in the hub's parent folder. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, location, precision]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds three git repos: `orders-api/`, `orders-web/` and `roadmap/`, the last
one being the workspace's hub repo.

The user ran the command from inside the hub repo. First change into it with
the Bash tool (`cd roadmap`), and stay there. Then invoke the
`vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`) with
no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Removing or archiving a repo: `no, keep it`. Status of a repo that needs
one: `planned`. Role of a repo that needs one: `Storefront web app`. If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes`
to close it out quickly.

Once the skill finishes, report back what it did.
