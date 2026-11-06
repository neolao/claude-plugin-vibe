---
name: expert-cli-dx-changed-default-keeps-existing-scripts
description: >-
  Recall of the compatibility bullet of expert-cli-dx on changes that
  remove nothing: an existing list command gets a column inserted in the
  table that deploy scripts `awk`, its default order flipped to newest
  first, and its `--older-than` flag moved from plain days to a `7d`/`12h`
  form that makes the plain number an error — while the scripts that call
  it today are owned by other teams. The expert must require that those
  scripts' unchanged invocations keep getting what they got (the old
  columns and order, plain days still accepted) or a transition with a
  deprecation warning, instead of treating a default change and a flag
  re-interpretation as plain changes.
tags: [expert-cli-dx, recall, compatibility]
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
`--older-than <days>` as a plain number of days. The deploy scripts of two
other teams run it every night, `awk` the second column to find failed
backups, and call it with `--older-than 30`. We now also record the backup's
size, so we want a SIZE column between NAME and STATUS, we want the newest
backup first since that is what people look for, and we want `--older-than`
to accept `7d` and `12h`; a bare number would no longer be meaningful, so
`--older-than 30` would become an error. We don't control when the other
teams update their scripts.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
