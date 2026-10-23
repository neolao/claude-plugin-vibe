---
name: docs-asks-before-managing-a-hand-written-readme
description: "Precision side of docs-leaves-a-missing-marker-pair-absent: /vibe:docs on a README with no marker pair at all. The absent-pair rule must not fire here — the skill lists the sections it could manage and asks which to add, inserts nothing on its own, and leaves the hand-written README byte-for-byte as it was. Requires --allow-tools Bash Write Edit to run (the skill may write docs/ files)."
tags: [docs, markers, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:docs` skill (Skill tool, `skill: "vibe:docs"`) with no arguments, on the project in this workspace.

If the skill asks you a question, do not answer it: stop there and report the question as it was asked.

Otherwise, once it finishes, report exactly what it changed.
