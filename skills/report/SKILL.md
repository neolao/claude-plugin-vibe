---
name: report
description: "Usage report of a vibe workflow: counts, while the work runs, the bricks called, the loop rounds, the findings, the questions asked to the user and the fixes, then writes these statistics to `.vibe/reports/` in the project at the end. Invoked by `vibe:feature` and `vibe:fix` through their shared workflow, at the start of the work and at the end. Never triggered by a user request."
argument-hint: "init <entry> <model> <backlog: yes|no> | write"
user-invocable: false
version: 1.1.0
model: claude-sonnet-5-5
---

# vibe:report — Usage Report

## Golden rule
The report holds statistics only. Never code, a file path, a ticket, a backlog item title or free text: it must be shareable with the plugin's maintainers without exposing anything of the project.

## The script
Every operation goes through `scripts/report.sh`. Its absolute path is the "Base directory for this skill" line shown at the top of this skill, followed by `/scripts/report.sh`. Always run it with `sh`, writing in full in every call the path of the script and the path of the counters: never a shell variable (`R=… ; C=…`), which an allow rule `Bash(sh */skills/report/scripts/report.sh:*)` would not recognize. Several events counted at once are chained with `&&`, each call with its two paths written in full. The counters live in `<scratchpad>/report.tsv` (the scratchpad your system prompt indicates).

```
sh <base>/scripts/report.sh <counters> init <entry> <model> <yes|no>
sh <base>/scripts/report.sh <counters> incr <key> [n]
sh <base>/scripts/report.sh <counters> brick <name>
sh <base>/scripts/report.sh <counters> show
sh <base>/scripts/report.sh <counters> write <project root>
```

The script refuses an unknown entry or counter, a model id or brick name outside lowercase letters, digits and dashes (exit 1, `refused: …`); it exits 2 when it cannot write. A brick name is otherwise free: spell it exactly as the agent or skill is named (`task-implementer`, `review-naming`), a typo would make a new line in the report. A refusal signals an error on your side: never work around it by editing the counters by hand. Without Bash, or if the call fails, skip the report and say so in one line: the work itself does not depend on it.

`init` overwrites a counters file left by a run that stopped early; `write` removes the counters once the report is on disk. One `init`, one `write` per run.

## At the start: `init`
The workflow calls `init` before its first step, with its entry (`feature` or `fix`), the full model id of the session, and `yes` when the brief came from a backlog item, `no` otherwise.

## During the work: `incr` and `brick`
Each event is counted when it happens, not reconstructed at the end: the session is long and context gets lost.

| Event | Call |
|---|---|
| A brick is called (agent or skill) | `brick <name>`, without the `vibe:` prefix |
| A loop round starts (a return to a framing) | `incr rounds` |
| A question is asked to the user | `incr questions` (one per question, even when grouped in one call) |
| The review agents raise findings | `incr findings.raised <n>` |
| The classifier drops some, merges some | `incr findings.dropped <n>`, `incr findings.merged <n>` |
| Kept findings, per level | `incr findings.high <n>`, `incr findings.medium <n>`, `incr findings.low <n>` |
| A finding sends the loop back to the need, to the implementation | `incr returns.need`, `incr returns.implementation` |
| A finding is corrected (one per finding, in a correction round) | `incr fixes` |
| A self-correction loop exhausts its attempts | `incr escalations` |

## At the end: `write`
At every end of the run — the report, an escalation, an early stop:
1. `write <project root>`: the script creates `.vibe/reports/<timestamp>-<entry>.md`, prints its path and removes the counters. The directory carries its own `.gitignore`, so a report never enters the project's history.
2. Close with one line: `📊 Report — <path>`, followed by: "Local only. Share it with the plugin's maintainers if you want it to feed the evals." In `--auto`, both lines come before the `AUTO-RESULT:` line, which stays last.
