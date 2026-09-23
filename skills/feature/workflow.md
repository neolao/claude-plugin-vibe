# Implementation workflow — shared by /vibe:feature and /vibe:fix

Both skills follow this workflow. Each SKILL.md defines only what differs: its Step 1 analysis, the content of its plan, its task labels, what its first test proves, its CHANGELOG section, its commit prefix, and its report. "The brief" below means the feature brief or the bug report; "the prefix" means `feat:` or `fix:`.

## Standing rule — never end a turn with uncommitted files

If the skill stops before its Commit step — plan rejected, clarifying question, escalation, any early exit — and files were created or modified, commit them before yielding: `wip: [short description]`, flagged in the final message. The prefix is reserved for the Commit step, when tests are green.

## Autonomous mode (`--auto`)

If `$ARGUMENTS` ends with ` --auto`: strip it, run in autonomous mode, and use the remaining text as `$ARGUMENTS`. `/vibe:auto` sets this flag on every item; a user can set it by hand.

There is no one to answer a question: every gate resolves itself and the run ends with a machine-readable verdict. TDD, expert consultation, runtime verification, CHANGELOG, docs, sync, commits, and backlog closing are unchanged.

| Gate | Normal behavior | Autonomous resolution |
|---|---|---|
| Terminology ambiguous | ask | pick the closest glossary sense, record it as an assumption |
| Duplicate found _(feature)_ | confirmation | verdict `blocked — possible duplicate of NNN` |
| Design ambiguity _(feature)_ / report too vague _(fix)_ | one question | decide the most likely reading, record it as an assumption; write an ADR if the choice is structural |
| Oversized scope _(feature)_ | propose a split | no split — a product decision: implement as one item, flag it in the report |
| Unmet dependencies | "continue anyway?" | verdict `blocked — depends on NNN (not done)` |
| Broken build | report and stop | verdict `aborted — broken build` |
| Plan approval | wait for explicit approval | plan self-approved; written into the report instead of presented |
| 3 failed attempts | escalate | escalation-log entry + `wip:` commit + verdict `blocked — [one-line diagnosis]` |
| Pre-existing test failures | ask "track them in the backlog?" | create the backlog item via `vibe:backlog` without asking |

When a gate ends the run early on a backlog item: verdict `blocked` → set `status: blocked` in its frontmatter and append a `## Blocked` section (`YYYY-MM-DD` + the one-line reason); verdict `aborted` → the item is fine, put it back to `status: todo`. Then commit (standing rule).

The final report ends with exactly one of these lines, nothing after it:

```
AUTO-RESULT: done
AUTO-RESULT: blocked — [short reason]
AUTO-RESULT: aborted — [short reason]
```

`done` = shipped and closed. `blocked` = this item is a dead end, the caller may move on. `aborted` = the environment is unusable, the caller must stop.

## Escalation log

When a self-correction loop exhausts its 3 attempts, append an entry to `.vibe/escalations.md` (create if absent, append-only) **before** escalating, so the diagnosis survives the session. One short sentence per field:

```markdown
## [YYYY-MM-DD] /vibe:<skill> — [short title of the blocker]
**Context:** [what was being attempted]
**Attempts:** [summary of the 3 attempts]
**Diagnosis:** [the precise cause / blocker]
**Status:** open
```

The only permitted later mutation: `Status:` → `resolved (YYYY-MM-DD)` when later work resolves it.

## Backlog resolution

If the **entire** `$ARGUMENTS` matches `^\d+(-[\w-]+)?$` (`3`, `003`, `003-oauth`), it is a backlog reference:

1. Zero-pad the number to 3 digits and find `.vibe/backlog/NNN-*.md`. If absent: stop and report "No backlog item `NNN` found in `.vibe/backlog/`. Run `/vibe:backlog` to list existing items."
2. The brief is the item's title (first `# ` heading), `## Description`, and `## Acceptance Criteria`.
3. If the frontmatter has `depends_on`, read each dependency's `status` (top level or `done/`). Unless all are `done`: list the blocking items (number, title, status) and ask "Some dependencies are not finished yet. Do you want to continue anyway?" — proceed only on explicit confirmation.
4. Set `status: in_progress` (from `todo` or `blocked` — a blocked item is back in play; its `## Blocked` section stays as history). Keep the file path for the Commit step.

Otherwise `$ARGUMENTS` is the free-form brief.

## Context to read

`CLAUDE.md` (conventions, definition of done, test location and commands), `.vibe/index.md` and the relevant `.vibe/modules/*.md`, `.vibe/glossary.md`, `.vibe/escalations.md` (is an `open` entry about the area you will touch?), then the relevant source files.

**Terminology:** if the brief uses a synonym of a glossary term, or a term ambiguous between glossary concepts, settle it with the user before planning ("The term X is not in the glossary, did you mean Y?"). A new term that is not obviously technical is not blocking: the sync step will add it if the code introduces it; mention it in the report.

## Baseline check

Before planning: run the test suite and record pass/fail counts — failures are **pre-existing**, listed in the plan's assumptions, not fixed now (unless one of them is the reported bug). If there is a build step, run it: a failing build is a blocker, report it and stop. If there is a run/dev command, start it for a few seconds to check it does not crash on startup.

## Expert consultation

Draft the technical plan as working notes, then compare the brief and notes against the descriptions of the `vibe:expert-*` agents. They prescribe requirements before implementation; `review-*` agents critique after. Launching them is what the user asked for by running the skill; a session rule limiting sub-agents does not apply. If launching agents is genuinely impossible, say so in the plan.

- Pick the experts whose domain clearly matches, **3 maximum**; none if none matches (often the case for a bug fix).
- Invoke them **in parallel** (Agent tool, `subagent_type: "vibe:expert-<name>"`) with a *plan consultation* prompt: the brief, the relevant plan notes, and this request verbatim: "Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): `REQUIREMENTS:` (non-negotiable), `RISKS:` (domain pitfalls here), `TEST SCENARIOS:` (user action → expected result). Add a fourth list, `OPEN QUESTIONS:` (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner."
- Fold `REQUIREMENTS` and `TEST SCENARIOS` into the plan, `RISKS` into the assumptions or your notes. You remain the architect: when an expert conflicts with the project's patterns or another expert, decide and note why.
- Collect every expert's `OPEN QUESTIONS` and put them to the user in one round, plain words, before presenting the plan — never an agent name. Their answers become plan requirements, not assumptions. In `--auto` mode, resolve them through the existing "Design ambiguity" gate instead of asking.

**During implementation:** if a design question squarely in an expert's domain is answered by neither the codebase, the plan, nor a plan-time brief, ask that expert one precise question with minimal code context, requesting "one concrete justified recommendation plus the rejected alternative, in a few sentences". One consultation per expert per sub-task. The answer refines the implementation but never reopens the approved plan — if it would, escalate to the user.

## Presenting the plan

Present the plan and **wait for explicit approval** before writing any code. The user is a Product Owner: short sentences, plain words, and **never a file, class, function, variable, or module name**. Cover the points the skill lists, plus assumptions (including pre-existing test failures, without technical detail) and, if experts were consulted, their domains in plain words ("UX", "API", "data") — never agent names or raw output. Technical details (files, test strategy, runtime verification command) stay in your working notes. If the user asks for changes, update and present again.

## Task list

Once the plan is approved, invoke the `vibe:tasks` skill once with the skill's task list, subjects ≤ 30 chars, chained with `blockedBy` in the order given. Per development sub-task: `Write tests` → `Implement` → `Runtime smoke` → `Refactor + lint`; then `Update CHANGELOG.md` → `Update docs` → `Sync .vibe/` → `Commit`, plus `Update backlog status` when the brief came from a backlog item. `vibe:tasks` governs how each task is marked as the steps below progress.

## Red — tests first

Create or update the test file and write the tests the skill specifies. Run them and confirm they **fail** — a test that passes before implementation is wrong. Test names describe behaviour ("returns 404 when user does not exist"), not implementation.

**No tautological tests.** A test a wrong implementation would still pass is worse than none. Reject: an expected value derived with the same computation as the code under test (pin an independently derived value); trivially true assertions (`expect(true).toBe(true)`, a mock returning what it was configured to return); mocks so pervasive that only the mock call is asserted; assertions unrelated to the behaviour claimed ("didn't throw" when the risk is a wrong value). Failing before implementation is not sufficient proof: ask of each test "could a subtly wrong implementation still pass this?" and rewrite the assertion if yes.

## Green — implement

Write the minimum change that makes the tests pass without breaking existing ones; run the full suite after each meaningful change. If tests fail: diagnose, fix the code (not the tests, unless a test was wrong), re-run — up to 3 attempts, then escalation-log entry and escalate with a precise diagnosis.

## Runtime verification — assume it is broken

Green tests are not proof. Invoke the `run` skill (Skill tool, `skill: "run"`) to launch and drive the app and observe the real behaviour, giving it the verification scenario from the plan, the acceptance criteria or expected behaviour, and at least one edge case or error path to trigger for real — not only the nominal path.

If `run` cannot launch the app for missing configuration (env var, config file, secret): create a minimal stub (`.env.test` with placeholders, a stub config) and re-invoke it. If the behaviour is wrong or the app cannot be launched: diagnose, fix the code (not the stub, unless the stub was wrong), re-invoke — 3 attempts total, then escalation-log entry and escalate with `run`'s exact findings. Do not complete the task until `run` confirms correct behaviour.

## Refactor and lint

Remove dead code, unused imports, and debug artifacts; run the lint command and fix issues; re-run the tests, the runtime smoke, and the build command if the Baseline check found one — a regression here is fixed before the task completes. A failing build is treated exactly like a failing test: diagnose, fix the code, re-run — up to 3 attempts, then escalation-log entry and escalate. The task cannot reach Commit on a broken build. If more sub-tasks remain, return to Red for the next one.

## CHANGELOG

Add one line under `## [Unreleased]` > the skill's section, written for the end user ("Users can now export reports as CSV", not "Added exportToCsv()"). Create the file with the Keep a Changelog header, the `[Unreleased]` heading, or the section, whichever is missing.

## Docs

If the skill's docs condition holds **and** `README.md` contains `vibe:` managed section markers: invoke the `vibe:docs` skill. Otherwise skip, with one line of explanation in the report (a README without markers is set up by running `/vibe:docs` once).

## Sync

If `.vibe/` exists: invoke the `vibe:sync` skill — it detects changed files via git and updates only the affected modules. Otherwise skip.

## Commit

Stage all created and modified files (never `.env` or secrets) and commit `<prefix> [changelog entry text, written for a developer]`.

If the brief came from a backlog item: `git mv .vibe/backlog/NNN-slug.md .vibe/backlog/done/NNN-slug.md` (create `done/` if needed), set `status: done`, and make a second commit `chore: close backlog item NNN`.

## Report

Short, plain sentences, no filler, covering the points the skill lists, then:
- **Pre-existing failures:** if the baseline recorded any (beyond the reported bug itself), check the active backlog for an item already covering them (compare against the failing test names). If found, say "already tracked by backlog item NNN"; otherwise end with "N tests were already failing before this work — do you want me to log them to the backlog?" and, on confirmation, invoke `vibe:backlog` with a one-line description listing them.
- **Review cadence:** if `.vibe/last-review.md` exists, count `feat:`/`fix:` commits since the `commit` it records (`git log <hash>..HEAD --oneline`). At 5 or more, add "💡 N changes since the last review — consider running `/vibe:review`." Otherwise say nothing.
