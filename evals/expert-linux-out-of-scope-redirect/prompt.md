---
name: expert-linux-out-of-scope-redirect
description: expert-linux must decline or redirect a brief that is really about CLI flag/help/output design, not shell scripting or system integration
tags: [expert-linux, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-linux` sub-agent (Agent tool, `subagent_type: "vibe:expert-linux"`) with this brief plus the consultation request below.

Brief:

```
We're designing the command-line interface for a new `myctl export` command:
which flags it should accept (short and long forms), what its `--help` output
should look like, whether it needs a `--json` mode for scripting, and what
exit code it should return for each failure case. No shell script or system
service is involved — this is a single Go binary's argument parsing and
output design.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
