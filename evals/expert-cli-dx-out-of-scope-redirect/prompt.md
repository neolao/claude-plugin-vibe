---
name: expert-cli-dx-out-of-scope-redirect
description: expert-cli-dx must decline or redirect a brief that is really about system-level shell/service integration, not CLI UX
tags: [expert-cli-dx, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
We need a bash installer script for our internal agent daemon: it creates a
dedicated system user with restricted permissions, writes a systemd unit file
so the daemon starts on boot and restarts on crash, and must behave correctly
whether run on a Debian server or a developer's macOS laptop (GNU vs BSD
coreutils differences). No new command-line flags or CLI output are involved.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its reply back verbatim.
