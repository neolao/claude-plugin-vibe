---
name: expert-linux-in-scope-advice
description: expert-linux must surface XDG-path, SIGTERM/child-cleanup, and GNU-vs-BSD portability requirements for a cross-platform bash daemon
tags: [expert-linux, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-linux` sub-agent (Agent tool, `subagent_type: "vibe:expert-linux"`) with this brief plus the consultation request below.

Brief:

```
We're writing a bash script that runs as a long-lived background daemon: it
watches a directory for new files, spawns a child process per file to convert
it, writes results into a cache file under the user's home directory, and
must run unmodified on both our Linux build servers and developers' macOS
laptops. It needs to be started from a supervisor and stopped cleanly when
the machine shuts down or the supervisor restarts it.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its reply back verbatim.
