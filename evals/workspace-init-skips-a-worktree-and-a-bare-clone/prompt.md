---
name: workspace-init-skips-a-worktree-and-a-bare-clone
description: >-
  vibe:workspace-init must register only real sibling repos — not a linked worktree, not a bare clone, not a plain folder — and name the skipped worktree and bare clone in its report. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, bootstrap, siblings]
runs: 3
max_turns: 80
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo). It
holds the `orders-api/` repo and a few other directories next to it. No hub
repo exists yet anywhere in this workspace.

Invoke the `vibe:workspace-init` skill (Skill tool, `skill: "vibe:workspace-init"`)
with the argument `roadmap` as the hub directory name.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Git remote for the hub: none. Status of a repo that needs one:
`planned`. Role of a repo that needs one: `Hotfix checkout`. Purpose of the
workspace, if asked: `Everything that lets a shop take orders online.` If a
`vibe:clarify` sub-flow starts probing with rounds of questions, answer `yes`
to close it out quickly.

Once the skill finishes, report back what it did, including what it said
about the directories it did not register.
