---
name: expert-linux-interactive-setup-keeps-prompts
description: >-
  Precision side of the unattended-run rule: a setup script developers run by
  hand from a terminal on their own laptop, which asks them what to install,
  is not a cron job — expert-linux must not forbid its questions, demand a
  non-interactive mode or a single-instance lock, or test it as if a
  scheduler launched it, while still confining root to the package-manager
  steps as its checklist requires.
tags: [expert-linux, precision, unattended]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-linux` sub-agent (Agent tool, `subagent_type: "vibe:expert-linux"`) with this brief plus the consultation request below.

Brief:

```
We're writing `setup-dev.sh`, a bash script a new developer runs by hand
from a terminal on their own Linux laptop on their first day, and again
whenever the README tells them to after a pull. It asks them which of the
project's services to install locally (the database, the message broker, or
both), installs the chosen ones with the distribution's package manager,
writes a local config file with the ports it picked, and prints what to do
next.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
