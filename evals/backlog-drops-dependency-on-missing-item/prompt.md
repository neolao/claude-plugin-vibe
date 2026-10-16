---
name: backlog-drops-dependency-on-missing-item
description: >-
  vibe:backlog adds one item whose description names "after 007" while the
  backlog only holds 001 and 002: it must create 003 with no depends_on on
  007, name the dropped reference in its report, and commit once with the
  single-item message.
tags: [backlog, add, dependencies]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with this argument, verbatim:

```
Let users export the current report as a PDF file, after 007
```

Do not look up or correct the reference yourself before invoking the skill — let the skill handle it. If it asks anything, answer that you have nothing to add, without ending your turn (nobody else will reply), and let it proceed.

Once it finishes, report back: the file it created, that file's frontmatter verbatim, the commit it made, and every sentence of its report about dependencies.
