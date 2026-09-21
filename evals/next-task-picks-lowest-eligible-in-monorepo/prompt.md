---
name: next-task-picks-lowest-eligible-in-monorepo
description: >
  next-task must classify a clearly-worded defect backlog item as a fix (not
  a feature), hand off to vibe:fix, then surface vibe:publish's push failure
  (no Git remote configured) as a reported blocker rather than a silent
  success or a hang. Runs a real, trivial vibe:fix cycle — the most
  expensive case in this eval batch by design. Requires
  `--allow-tools Bash,Write,Edit` to run.
tags: [next-task, defect-classification, publish-blocker]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

You are in a mono-repo (no workspace hub, just this repo's own `.vibe/backlog/`) with a single eligible backlog item, `001`.

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with `001` as `$ARGUMENTS` — this is the forced-pick form, so it reads that item directly instead of scanning/scoring candidates.

Let it run to completion. It is expected to:
1. Read backlog item `001` and classify it — its title and description use defect vocabulary ("crash"), so it should be treated as a fix, not a feature.
2. Hand off to `vibe:fix 001` with its normal gates, which should find and fix the one-line off-by-one bug in `calculator.py` so `test_calculator.py::test_average_of_three_numbers` passes.
3. Invoke `vibe:publish` to push the result. This repo's Git remote is not configured on purpose — the push is expected to fail with a Git error (e.g. "no configured push destination"). This is the correct, intended outcome for this case: report it as a blocker, do not try to work around it (do not add a remote, do not force-push, do not silently treat it as success).

Once `vibe:next-task`'s final report comes back, report it back verbatim.
