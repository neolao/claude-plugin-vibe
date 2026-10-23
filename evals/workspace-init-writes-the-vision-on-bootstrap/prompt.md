---
name: workspace-init-writes-the-vision-on-bootstrap
description: >-
  vibe:workspace-init must write the workspace vision gathered at bootstrap under the hub CLAUDE.md's Role section, in the project's language. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, bootstrap, vision, precision]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo) that
holds two sibling repos, `orders-api/` and `orders-web/`. No hub repo exists
yet anywhere in this workspace.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with the argument `roadmap` as the hub directory name.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Git remote for the hub: none. Status of a repo that needs one:
`planned`. Role of a repo that needs one: `Storefront web app`. Purpose of
the workspace, when asked: `These repos together let a florist take orders
online and deliver them the same day — the API owns the orders and the
storefront sells them.` If a `vibe:clarify` sub-flow starts probing with
rounds of questions, answer `yes` to close it out quickly, and confirm its
summary when it asks.

Once the skill finishes, report back what it did.
