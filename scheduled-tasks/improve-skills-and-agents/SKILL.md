---
name: improve-skills-and-agents
description: Improve the skills and agents of the vibe plugin
---

Goal: bring every skill and every agent to a perfect score (1.00) at the lowest cost, then harden its case suite to find new weaknesses in it.

Repository: ~/workspace/claude-plugin-vibe. Scope: the skills in `skills/` and the agents in `agents/`, with their cases under `evals/`. The repo's eval conventions are in the "Agent model evals" section of its `CLAUDE.md`: read it before you start, it is authoritative.
**One run of this task = a single target (one skill or one agent), with all its objectives chained.** Do not touch any other target during this run, even if you notice a problem in it: write it down in the history.md row.
Follow the steps with TaskCreate.

## Persist what you learn about running a case
When you find a problem or an improvement in how an eval case runs, persist it so the next runs do not have to rediscover it.
This covers how a case is launched or run, not the target's behavior: a missing command or flag, an environment variable to provide, a sandbox limit, a fixture that does not install, a pitfall when reading the trace, a step to take before or after the run.
- If it is knowledge, write it in the "Agent model evals" section of `CLAUDE.md`, or in `evals/docker/README.md` for anything about Docker, where the next run will read it. Do not write it only in history.md, and not in this task prompt (`scheduled-tasks/improve-skills-and-agents/SKILL.md`): never edit this task itself, evolving it is the user's job.
- If it is a defect in one of the repo's eval tools (`evals/tokens.py`, `evals/docker/run.sh`, a scaffold script), fix the tool.
This update is allowed even when it falls outside the target's scope. Commit it separately, before the target's commit, with a message that says what was learned and how you observed it.

## Effort (agents only)
An agent can set `effort:` in its frontmatter: `low`, `medium`, `high`, `xhigh`, `max`. haiku does not support effort: an agent on haiku has no `effort:` field. An agent without `effort:` inherits the session's effort, which is not controlled in an eval: the first time you tune an agent's effort, write the level explicitly. When you change an agent's model, restart from `effort: high` (remove the field if it moves to haiku).

## 0. Starting guard
`git status --porcelain` must be empty and `git pull --rebase` must succeed. Otherwise, stop without doing anything: someone is working in the repo, or a previous run has not finished.

## 1. Choosing the target
For each target, its first pending objective is the first one that applies:
1. one of its cases has no non-obsolete row in `evals/results/history.md` (search for `<case-name> |` without the leading pipe: an obsolete row has ⚠️ in the Case cell);
2. the latest non-obsolete row of one of its cases is below 1.00;
3. all its cases are at 1.00.
A target with a case whose latest row is marked `**Manual follow-up needed:**` is excluded: that case is in the user's hands.
Pick the target whose first pending objective has the lowest number. On a tie, pick the one whose most recent row is the oldest.

## 2. Working on the target, in this order
1. **Evaluate**: run each of its cases that has no non-obsolete row.
2. **Fix**: as long as one of its cases is below 1.00, apply section 4.
3. **Cut the cost**: once all its cases are at 1.00, try to reduce its consumption, by lowering its `effort:` or its `model:` one notch (agents only), and/or by trimming its prompt. Re-run all its cases. Keep the reduction only if they all stay at 1.00 **and** the cost is lower than the latest row of each case. Otherwise, revert; a row records the attempt.
4. **Harden**: add **a single** new case, more elaborate but relevant, meant to try to lower the score. Follow the case rules of `CLAUDE.md` (a fixture never names the defect it contains, one grader = one verifiable claim, the injected prompt reproduces the skill's contract word for word, a case must be able to reach 1.00). Run it. If it is below 1.00, apply section 4. The run then ends, even if the target passes this new case.

## 3. Running a case
A new or modified case is first validated with `--runs 1`. That validation run gets no row in history.md; only the full run that follows does.

Case without `Bash`, on the host, from the repo root — **the canonical command**, both lines together:
```bash
claude plugin eval . --case '<case-name>' --scaffold --judge-model sonnet \
  --ablation none --keep-temp --trust-plugin --no-publish \
  --output-dir evals/results/<case-name>
python3 evals/tokens.py evals/results/<case-name> --cleanup
```
Case that grants `Bash` (its `allowed_tools`, or the `--allow-tools` its definition calls for): read `evals/docker/README.md` first, then run `zsh -ic 'cd ~/workspace/claude-plugin-vibe && evals/docker/run.sh <case-name> --allow-tools <case tools>'`. The `zsh -ic` is required: the app does not pass `CLAUDE_CODE_OAUTH_TOKEN` to the commands it runs, only `~/.zshrc` provides it. The script adds the canonical flags itself and runs `tokens.py` in the same container. If `CLAUDE_CODE_OAUTH_TOKEN` is missing, never remove `Bash` from the case to run it on the host: document the blocker in the note and move on to the next objective.

Do not improvise another command, and never run a global `rm -rf /private/tmp/e-*`: `tokens.py --cleanup` deletes exactly the run's directories.
The judge is always sonnet: never change it, and never replay a case with another judge to get a score through.

## 4. Score below 1.00
Read the trace to find who is at fault:
- **the case** (grader aimed wrong, ambiguous fixture) → fix the case and apply the "A changed case retires its own history" rule at the top of history.md (⚠️ in the Case cell, note opened with `**Obsolete (YYYY-MM-DD):**`);
- **the target** (behavior that contradicts its own definition) → fix its prompt. For an agent, if a prompt fix is not enough, first raise its `effort:` one notch (`low` → `medium` → `high` → `xhigh` → `max`; with no `effort:` field, start at `xhigh`), and raise its `model:` one notch (haiku → sonnet → opus) only once `max` is reached, or from haiku, which has no effort.
Re-run after each fix. Keep a copy of each version tried (target and case) in the scratchpad, with its score.
**Giving up**:
- agent: when opus at `effort: max` still fails after a fix;
- skill (no `model:`): after 5 fixes without reaching 1.00.
When you give up, restore the target and the case to the version that got the best score, and commit that best result. Its row's note starts with `**Manual follow-up needed:**`, followed by your diagnosis; the commit message says so too. The run ends there, without moving on to the next objectives.

## 5. history.md
Use its columns (Date, Agent, Agent version, Case, Model, Score, Pass rate, Cost, Tokens in/out, Notes).
One row per full run, including the attempts below 1.00 (another model, another effort, a fix not kept), in the same commit as the final result. The Tokens column takes the `Tokens in/out` line from `tokens.py`; the note names the model and effort tested and what was tried. If `tokens.py` fails (missing trace, cost reconciliation failed), write no figure: put the error in the note.

## 6. Commit
Bump the target's `version:` if it was modified (prompt, or model or effort for an agent), following the `CLAUDE.md` rule (patch, minor or major). `git add` only the files you touched, commit with a message prefixed `test:` like the existing eval commits, then push to main. If the push is rejected, run `git pull --rebase` once, then stop and document it.
