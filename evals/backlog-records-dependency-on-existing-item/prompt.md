---
name: backlog-records-dependency-on-existing-item
description: >-
  vibe:backlog adds one item whose description names "after 002" on a
  backlog holding 001 and 002: it must create 003 with `depends_on: [002]`
  and commit once with the single-item message.
tags: [backlog, add, dependencies]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with this argument, verbatim:

```
Let users export the current report as a PDF file, after 002
```

Do not resolve the reference yourself before invoking the skill — let the skill handle it. If it asks anything, answer that you have nothing to add, without ending your turn (nobody else will reply), and let it proceed.

Once it finishes, report back: the file it created, that file's frontmatter verbatim, and the commit it made.
