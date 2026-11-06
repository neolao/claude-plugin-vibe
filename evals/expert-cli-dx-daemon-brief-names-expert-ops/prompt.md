---
name: expert-cli-dx-daemon-brief-names-expert-ops
description: >-
  Precision side of the operations routing: a daemon that is already
  launched by an unchanged `agentd run` command gains environment-based
  configuration, a health endpoint, a graceful SIGTERM shutdown, a
  Dockerfile and a restart policy — a brief full of process vocabulary
  that adds or changes no command, flag or CLI output. expert-cli-dx must
  decline in one line and name `expert-ops` by id, since the experts never
  see the roster, instead of filling the lists with deployment advice or
  pointing at `expert-linux`.
tags: [expert-cli-dx, precision, ops-routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our internal agent daemon is started with `agentd run`, which has worked the
same way for two years; its flags, its help and what it prints do not change
in this work. The daemon currently reads a hardcoded config file; we're
moving its settings to environment variables with a startup check that
names any missing one, adding an HTTP `/healthz` endpoint for the
orchestrator's liveness probe, making it finish in-flight work on SIGTERM
before exiting, and writing its Dockerfile and the restart policy of its
deployment so it comes back on its own after a crash. No new command-line
flags, no new CLI output.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
