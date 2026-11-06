---
name: expert-cli-dx-additive-flag-needs-no-transition
description: >-
  Precision side of the compatibility bullet: an existing list command
  gains one optional filter flag and a `--json` output switch, with its
  default output, order and existing flags left exactly as they are, while
  other teams' scripts call it nightly. The expert must not demand a
  deprecation period, an alias, a version bump or a migration of the
  scripts for an additive change — it states that the unchanged invocation
  prints what it did, and keeps the rest of its lists on the new flag and
  the new output.
tags: [expert-cli-dx, precision, compatibility]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
`myctl backups list` has been in our CLI for three years. It prints a table
with the columns NAME, STATUS and AGE, oldest backup first, and takes
`--older-than <days>`. The deploy scripts of two other teams run it every
night and `awk` the second column to find failed backups. We're adding an
optional `--status <value>` flag so the on-call engineer can list only the
failed backups, and a `--json` flag that prints the same backups as a JSON
array instead of the table. Without the new flags the command prints exactly
what it prints today: same columns, same order, same `--older-than`.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
