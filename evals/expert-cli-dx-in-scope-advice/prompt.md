---
name: expert-cli-dx-in-scope-advice
description: expert-cli-dx must surface destructive-op confirmation, stdout/stderr piping discipline, and exit-code requirements for a new CLI subcommand
tags: [expert-cli-dx, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our existing CLI tool `myctl` already has `myctl status` and `myctl backup`, both
using standard single/double-dash flags. We're adding a new subcommand,
`myctl prune-logs <dir> --older-than <days>`, that deletes log files older than
the given number of days from a directory and prints how many files were
deleted. Teams want to run it unattended from cron jobs, and also want to pipe
the list of deleted file paths into other tools for auditing.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
