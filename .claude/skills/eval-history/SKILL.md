---
name: eval-history
description: Rebuilds or updates the evolution chart of a skill or agent of this plugin (evals/history/) by replaying the current eval case on its past versions. Use for "show the evolution of <skill/agent>", "redo the chart", "update the history", or after an eval case was modified (outdated points).
---

# eval-history

Argument: `<skill|agent> [case] [--refresh]`. Details and limits: `CLAUDE.md`, section "Evolution history".

1. Case: with no argument, list the `evals/<x>-*` cases (skill or agent name as prefix) and ask which ones via `AskUserQuestion`. A case that grants `Bash` runs in Docker on the commit's worktree: it needs `CLAUDE_CODE_OAUTH_TOKEN` (see `evals/docker/README.md`, `zsh -ic`).
2. Estimate: `sh evals/history/collect.sh <x> <case> --dry-run [--refresh]`. Each point costs about $0.4-4 (3 runs + judge). Show the number of points and the estimated cost, and ask for confirmation (`AskUserQuestion`) before any real run.
3. Run: the same command without `--dry-run`, in the background (several minutes per point).
4. Open `evals/history/index.html`, summarize the evolution (version → score) and mention the outdated points if any remain.
5. Do not commit; `timeline.json`, `cases.json` and `index.html` are for the user to commit.
