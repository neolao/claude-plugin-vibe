---
name: report-issue
description: Captures a misbehaviour of a vibe skill or agent noticed in the current conversation — did not trigger when it should, triggered when it should not, or ran its protocol wrong (wrong step, skipped gate, unwanted write, wrong finding) — as a permanent regression eval case in the plugin's own repository, from any project where vibe is installed; load it when the user reports such a misbehaviour or asks to "note", "record", or "keep a trace of" it as a test/eval case, and again when the user confirms a case already proposed. Not for fixing the skill or agent on the spot, nor for bugs in the project's own code (/vibe:fix).
argument-hint: "[optional: what went wrong, in one sentence; empty infers it from the conversation]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:report-issue — Regression Eval From a Misbehaviour

Turn a misbehaviour of a vibe skill or agent, observed in the current conversation, into an eval case committed later in the plugin's repository — the bug is *recorded*, never fixed here. Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Identify the target

Infer from the conversation which vibe skill (`/vibe:<name>`) or agent (`vibe:review-*`, `vibe:expert-*`) is at fault. Ask through `AskUserQuestion` only when it is genuinely ambiguous — several plausible targets, or the behaviour may belong to no vibe skill at all; otherwise do not ask.

## Step 2 — Classify the case

- **Did not trigger when it should** → *trigger-positive* case: the skill must load on that request.
- **Triggered when nothing justified it** → *trigger-negative* case: the skill must not load on that request.
- **Triggered but ran its protocol wrong** → *execution* case: the prior state is rebuilt in the prompt and the protocol is named explicitly.
- **A review or expert agent** → a `<agent>-finds-<what>` case for a missed finding, `<agent>-no-false-positives` (or a sibling named like the existing ones) for a wrong finding, following the names already in `evals/`.

A doubt between two families is settled with the user at Step 7, never silently.

## Step 3 — Extract the context

- **Trigger cases:** the user's request as phrased in this conversation (verbatim or a faithful rewording), **never naming the skill** — the case tests whether its description alone loads it.
- **Execution cases:** the prior state needed to reach the exact point of the protocol where the bug appeared (files already written, answers already given, backlog or `.vibe/` state), and the protocol named explicitly in the prompt.
- **Agent cases:** the code that provoked the behaviour, reduced to a minimal fixture file. A fixture never names the defect it contains: its comments say where the code is called from and what it is for, never what is wrong, and clean code does not defend itself — no "not feature envy", no "no shared state". The prompt reproduces word for word the contract `skills/review/SKILL.md` really sends the agent.

## Step 4 — Resolve the plugin repository

```bash
jq -r '.extraKnownMarketplaces.vibe.source.path // empty' ~/.claude/settings.json
```
Empty → fallback:
```bash
jq -r '.vibe.source.path // .vibe.installLocation // empty' ~/.claude/plugins/known_marketplaces.json
```
A path under `~/.claude/plugins/cache/` is an install cache, not a development checkout: ask the user for the checkout path. Sanity-check the path (`ls`): it must hold `evals/` and `skills/`. No usable path, or the check fails → **never guess**: ask through `AskUserQuestion`. `${CLAUDE_PLUGIN_ROOT}` is not available in a Bash command — it only expands in the `command` fields of `hooks.json`/`.mcp.json`/`settings.json`.

## Step 5 — Read the conventions

Before writing anything, read the eval section of `<plugin_root>/CLAUDE.md` ("Agent model evals" — the source of truth) and [references/eval-checklist.md](references/eval-checklist.md) (the condensed checklist of known pitfalls). Then read one existing case of the same family in `<plugin_root>/evals/` and follow its shape.

## Step 6 — Write the case

Folder: `<plugin_root>/evals/<skill-or-agent>-<slug>/` — unnumbered, target name first: alphabetical order groups by target, and no `max + 1` to compute (two parallel sessions would collide).

- `prompt.md` — frontmatter `name`, `description` (one sentence: what must happen, plus the `--allow-tools` it needs), `tags` (the target's name, never `report-issue`), `runs: 3`, `max_turns`/`timeout_seconds` sized for the case (trigger-negative: small; a skill chaining sub-skills: 80 turns; a heavy agent: 600 s), `allowed_tools` covering what the target needs in the tested mode (`Skill` for a skill, `Agent` for an agent; `Bash`, `Write`, `Edit` only when the target uses them). Body: the prompt built at Step 3.
- `case.yaml` + `fixture.sh` + `fixtures/` — for an agent case or any case needing files: `context.add_dirs: [fixtures]` (never `[.]`) and `context.scaffold_script: fixture.sh`, which copies `fixtures/` into the run's workspace (`cp -r "$dir/fixtures" .`) — `add_dirs` grants a read permission, it copies nothing.
- `graders/*.md` — one file per verifiable claim, each encoding the **correct** behaviour, never the observed bug: the case stays red until the bug is fixed, then turns green. `tool_used` with `min: 0` / `max: 0` forbids an action; a `regex` on `target: trace` never uses `^`/`$` and must not be satisfied by the prompt or the `SKILL.md` the trace also contains; an `llm` grader asks for concrete elements (file names, lines, options), never an impression. The graders together must be able to reach 1.00.

## Step 7 — Show and confirm

Show the whole case (`prompt.md`, `case.yaml` and `fixture.sh` if any, every `graders/*.md`), then confirm through `AskUserQuestion`, at least two questions with 2–4 concrete options each, the recommended one first:
- the family (e.g. "Trigger-positive (recommended)" / "Execution" / "Other, specify");
- the folder name `<target>-<slug>` ("Keep as is" / "Rename").

Without `AskUserQuestion` (non-interactive session), the question goes in text, and the message asking it is **the last one** of the answer, in this order:
1. `Folder: <target>-<slug>`;
2. the full `prompt.md` in a code block, frontmatter included;
3. each `graders/*.md` (and `case.yaml`/`fixture.sh`) in full, in its own code block;
4. the questions — family, folder name, and one more when a close existing case was spotted.

Even if already shown above, the case is repeated in that message: never "the case above". A spotted duplicate does not exempt from showing the case. Nothing is written before this confirmation; a correction from the user adjusts the case first.

## Step 8 — Write and mark the history

Write the files in `<plugin_root>/evals/<target>-<slug>/`. If the new case changes an existing case (fixture, grader, weight), apply CLAUDE.md's obsolescence rule in `evals/results/history.md`: ⚠️ in the `Case` column of every row of that case and `**Obsolete (YYYY-MM-DD):** <what changed>` at the start of its note — never delete a row, never touch its figures. A brand-new case touches no history row.

## Step 9 — Close

As soon as the files are written, the answer **always** ends with these lines, nothing after them — even when the confirmation was already in the user's message. A free-form file recap does not replace them:
```
🚩 [Eval case created — evals/<name>/]
Run it: `claude plugin eval . --case '<name>' --runs 1` from `<plugin_root>` (a case granting Bash runs through `evals/docker/run.sh`).
```

## Guardrails

- Never a silent write: Step 7's confirmation is mandatory however clear the case looks.
- Never a guessed repository path: when the `jq` resolution fails, ask.
- This skill never runs `claude plugin eval` itself and never commits — it writes the files, closes with the `🚩` block, and stops.
- Graders encode the correct behaviour, never the observed bug — otherwise the case tests nothing.
- Case folders are never numbered: `<target>-<slug>`.
