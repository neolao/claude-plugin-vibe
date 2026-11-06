---
name: expert-cli-dx-convention-does-not-excuse-exit-zero-on-failure
description: >-
  Precision side of the convention rule: the CLI's six existing commands
  exit 0 whatever happens and print `ERROR: ...` on stdout, and the brief
  adds an export command that CI pipes into a file. "Reuse the existing
  conventions" must not become "copy the existing defect": expert-cli-dx
  must still require the new command to exit non-zero on failure and keep
  its errors off the piped stdout, and must not make re-wiring the six
  existing commands' exit codes — which would abort the `set -e` wrapper
  scripts that read their ERROR line — a requirement of this change.
tags: [expert-cli-dx, precision, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our internal CLI `inv` has six commands (`inv sync`, `inv check`, `inv tag`
and three others) with ordinary `--long` flags. All six always exit 0: when
something goes wrong they print a line starting with `ERROR:` on stdout and
stop. The ops team's wrapper scripts, written by another team, run the
commands under `set -e` and read that `ERROR:` line themselves to decide what
to do. We're adding `inv export --since <date>`, which prints the inventory
changes since a date as CSV; the nightly CI job will pipe its output into a
file that the finance tool imports the next morning. Nothing else in the CLI
changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
