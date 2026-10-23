---
name: publish-answers-the-docs-question-in-its-place
description: >-
  vibe:publish must not end its turn on the question vibe:docs raises for a
  README without managed sections: it answers in its place (no section is
  managed, the README stays as it is), and the release reaches the remote.
  Requires --allow-tools Bash,Write,Edit to run.
tags: [publish, e2e, unattended]
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
