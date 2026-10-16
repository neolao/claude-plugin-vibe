# Eval case checklist

Condensed from the "Agent model evals" section of the plugin's `CLAUDE.md`, which stays the source of truth: when the two diverge, `CLAUDE.md` wins — reread it, it may have moved on since this file was written.

## Layout

- Folder `evals/<target>-<slug>/`, never numbered. One case per scenario. Everything that defines it is committed normally; `evals/results/` is regenerated and gitignored, except `evals/results/history.md`.
- `case.yaml`: `context.add_dirs` names **only the case's fixture folders** (`add_dirs: [fixtures]`) — `[.]` is refused by the CLI and every run fails at $0. It declares a read permission, it copies nothing.
- A fixture needs a `context.scaffold_script` (e.g. `fixture.sh`) that copies `fixtures/` into the run's empty workspace; it runs only with `--scaffold`. A scaffold writes nothing outside the workspace (a shared `../origin.git` survives cleanup and collides between runs).
- A fixture never names the defect it contains: comments say where the code is called from and what it is for, never what is wrong — and clean code does not defend itself. The only exception is a justification that is part of the evaluated domain and that the agent's definition tells it to accept.
- The prompt injected into an agent reproduces word for word what `skills/review/SKILL.md` really sends it (contract, exclusion list, dynamic-verification flag).
- A fixture's stand-in tool (`./bin/gh`) must be pointed at by the prompt (e.g. "the repo's `CLAUDE.md` explains how commands run in the sandbox"), or the agent reports the tool as missing.

## `prompt.md` frontmatter

- `tags`: the target's name, never `report-issue`.
- `allowed_tools` covers the `tools:` the agent needs **in the tested mode** (`review-tests`, `review-dependencies`, `review-web-security` declare `Bash`); the static mode of `review-web-security` is the exception. `Read`/`Grep`/`Glob`/`Agent` come from the case; `--allow-tools` only takes gated tools (`Bash`, `Write`, `Edit`, `WebFetch`, `mcp__*`), space-separated.
- Never add `AskUserQuestion` just because the skill uses it: it is never offered in the sandbox, adding it changes nothing. A question is graded as text in `last_message` followed by a stop; what follows the user's answer is tested by an execution case whose prompt already contains that answer.
- `max_turns` fits the skill's nested skills: 80 for a skill that chains sub-skills; a collapse on the *last* step's graders with "Reached maximum number of turns" is a turn limit, not a regression.
- `timeout_seconds` fits the agent's `effort:`: 600 s for a heavy case; a timed-out run scores ~0.1 everywhere and gives no token figure.
- A case granting `Bash` runs in Docker (`evals/docker/run.sh <case-glob> [flags]`, needs `CLAUDE_CODE_OAUTH_TOKEN`), never on the host; cases without `Bash` run on the host.
- The sandbox has no network: a registry audit fails or returns "0 vulnerabilities" without checking; such a case measures how the agent handles an audit that could not run. No `pytest` either: Python fixtures run with `python3 -m unittest`. A background server does not outlive its Bash call: launch and probe in the same call.

## Graders

- One grader = one verifiable claim. Recall side: one grader per category, each with its own anchor in the code. Precision side: one grader per neutralised pattern, never a catch-all.
- Graders encode the correct behaviour, never the observed bug; together they must be able to reach 1.00 — two mutually exclusive graders (path A / path B) cap the score: one grader that tolerates both and checks the agent announces the one it took.
- `file_exists` only for a file the run **creates**; on a file already in the fixture it fails even when the agent edited it. Check a pre-existing file with an `llm` grader on `focus: { source: file, path: … }` or a regex on its content. `file_exists` sees only the run's cwd, never `$HOME` nor the plugin repo: anything outside the cwd is checked with `tool_used` + `input_match` on the path.
- An `llm` `criteria` never copies code containing `${…}` (template literal): describe the expected content in words.
- `tool_order` whose `after` is a command already run at baseline compares with the first occurrence and always fails: count occurrences with `tool_used` + `min: 2`. `tool_used` with `min: 0` / `max: 0` forbids an action. An agent reads the small files of a fixture while exploring: a narrative grader accepts both the anticipated and the failed path.
- A red step (test failed first) is graded from the tool calls (`tool_order` test edit → source edit, `tool_used` on the test command with `min: 3`), not from the final report.
- `regex` on `target: trace`: never `^`/`$`; the trace is JSON inside JSON, so tolerate 0 to 3 backslashes before a quote and test the pattern against a stored `traces/*.jsonl` before running. The trace also holds the prompt and the `SKILL.md` returned by the `Skill` tool: a pattern satisfied by either measures nothing. A `regex` on a status glyph tolerates markdown emphasis (`✓ **Pushed:**`).
- A skill that asks a question is hard to grade in one turn: a prompt asking for the question as a message of its own, then "yes" without ending the turn, works with a fixed template question; a grader judging order says that only the assistant's own text events before the first write count.
- A judge refusal (`grader threw`, `judge call failed: … safeguards`) is not a score; the same safeguard can hit the relaying top-level session ("I'm not able to continue reproducing that report verbatim"): grade such content from the trace, log the row with the error, do not change the judge.
- Past a certain trace length the `llm` judge only sees its start and end: a criterion on a mid-trace event is more reliable on a short run.

## After writing

- Changing an existing case outdates its own history rows: ⚠️ in the `Case` column and `**Obsolete (YYYY-MM-DD):** <what changed>` at the start of the note, in the same commit; never delete a row or touch its figures.
- Validate a new or modified case with `--runs 1` before running it at full scale; `--ablation none` halves the price once no baseline comparison is needed. Running an eval costs real tokens: it is a manual action, never triggered by a skill.
