---
name: publish-refreshes-a-managed-readme-on-release
description: >-
  vibe:publish on a README with managed sections must let the release's docs
  refresh rewrite them — nothing is declined, nothing asked — and push the
  release. Requires --allow-tools Bash,Write,Edit to run.
tags: [publish, e2e, unattended, precision]
runs: 3
max_turns: 60
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is.

If the skill asks you a question, do not answer it: stop there and report the
question as it was asked.

Otherwise, once it finishes, run `git ls-remote --tags origin` and report its
exact output in your final message, together with `vibe:publish`'s own report.
