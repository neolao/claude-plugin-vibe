---
name: workspace-init-stops-inside-a-code-repo
description: >-
  vibe:workspace-init run from a subdirectory of a code repo must stop with the "run from the workspace root" message and create nothing, instead of taking that subdirectory for a workspace root. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [workspace-init, location]
runs: 3
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

You are at the root of a workspace folder (it is not itself a git repo) that
holds two sibling repos, `orders-api/` and `orders-sdk/`. No hub repo exists
anywhere in it.

The user ran the command from `orders-api/src`, inside the `orders-api` repo.
First change into that directory with the Bash tool (`cd orders-api/src`), and
stay there. Then invoke the `vibe:workspace-init` skill (Skill tool,
`skill: "vibe:workspace-init"`) with no argument.

Nobody is available to reply during this run, so never end your turn on a
question: if the skill needs an answer, use the ones below and carry on to the
end. Hub directory name: `roadmap`. Git remote: none. Status of a repo that
needs one: `planned`. Role of a repo that needs one: `Shared TypeScript
client`. If a `vibe:clarify` sub-flow starts probing with rounds of questions,
answer `yes` to close it out quickly.

Once the skill has finished (or otherwise concluded), run
`printf 'porcelain-lines|%s\n' "$(git -C "$(git rev-parse --show-toplevel)" status --porcelain | wc -l | tr -d ' ')"`
with the Bash tool and include its raw output in your final message. Then
report, in short plain sentences, what the skill did and what it said.
