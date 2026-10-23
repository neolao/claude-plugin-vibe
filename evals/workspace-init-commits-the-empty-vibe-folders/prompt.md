---
name: workspace-init-commits-the-empty-vibe-folders
description: >-
  vibe:workspace-init's bootstrap commit must carry the hub's empty .vibe/backlog/ and .vibe/decisions/ folders (a .gitkeep in each) and leave nothing of the run unstaged. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, bootstrap, commit]
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
the workspace, if asked: `Everything that lets a shop take orders online.`
If a `vibe:clarify` sub-flow starts probing with rounds of questions, answer
`yes` to close it out quickly.

Once the skill has finished (or otherwise concluded), run
`git -C roadmap ls-files .vibe` and
`printf 'porcelain-lines|%s\n' "$(git -C roadmap status --porcelain | wc -l | tr -d ' ')"`
with the Bash tool and include their raw output in your final message. Then
report, in short plain sentences, what the skill did.
