---
name: fix
description: Fix a bug using TDD (reproduce first), then update CHANGELOG.md under [Unreleased] > Fixed
argument-hint: <bug description in natural language>
---

# /vibe:fix — TDD Bug Fix

Fix the bug described in `$ARGUMENTS` following the vibe coding workflow: the user is the Product Owner only and never tests code manually.

## Standing rule — never end a turn with uncommitted files

If this skill stops before its own Step 8 — plan rejected, clarifying question, escalation, or any other early exit — and files were created or modified, commit them before yielding control: `fix:` for a complete, coherent unit of work (a reproducing test plus its fix); otherwise `wip: [short description]`, flagged in your final message.

## Escalation log — record every dead end

_Entry format kept identical to `skills/feature/SKILL.md` and `skills/review/SKILL.md` — canonical shape documented in `.vibe/models.md` ("Escalation entry"); update all three together._

Whenever a self-correction loop in this skill exhausts its 3 attempts and escalates to the user (Step 4, Step 4b), append an entry to `.vibe/escalations.md` (create the file if absent) **before** escalating — the standing rule above then commits it with the `wip:` commit, so the diagnosis survives the session:

```markdown
## [YYYY-MM-DD] /vibe:fix — [short title of the blocker]
**Context:** [what was being attempted]
**Attempts:** [summary of the 3 attempts]
**Diagnosis:** [the precise cause / blocker]
**Status:** open
```

The file is append-only. The only permitted mutation: when later work resolves an `open` entry, change its `Status:` to `resolved (YYYY-MM-DD)`.

## Step 1 — Understand the bug

### Backlog resolution

_Kept identical to `skills/feature/SKILL.md`'s Backlog resolution — update both together._

Before treating `$ARGUMENTS` as a free-form description, check whether it is a reference to a backlog item (e.g. a bug filed via `/vibe:backlog`, often from a `/vibe:review` finding).

A backlog reference matches one of these patterns (the **entire** `$ARGUMENTS` must match — not just a prefix):
- A pure number: `3`, `003`, `42`
- A number followed by an optional slug: `003-login-crash`, `3-login-crash`

Detection rule: `$ARGUMENTS` matches `^\d+(-[\w-]+)?$`.

**If `$ARGUMENTS` is a backlog reference:**

1. Extract the numeric part and normalize it to 3 digits with zero-padding (e.g. `3` → `003`).
2. Search `.vibe/backlog/` for a file whose name starts with that 3-digit prefix: `003-*.md`.
   - If the directory does not exist or no matching file is found: stop and report "No backlog item `NNN` found in `.vibe/backlog/`. Run `/vibe:backlog` to list existing items."
3. Read the file:
   - Extract the title (first `# ` heading).
   - Extract the full `## Description` section.
   - Extract the `## Acceptance Criteria` section.
   - Extract the optional `depends_on` list from the frontmatter.
4. **Dependency check:** if `depends_on` is non-empty, for each dependency number find the file `NNN-*.md` in `.vibe/backlog/` (top level or `done/`) and read its `status`.
   - If ALL dependencies have `status: done`: continue normally.
   - If ANY dependency is NOT done: display a warning listing each blocking item (number, title, status). Then ask the user: "Certaines dépendances ne sont pas encore terminées. Voulez-vous continuer quand même ?" — do not proceed until the user explicitly confirms.
5. Update the frontmatter in the file: replace `status: todo` with `status: in_progress`.
6. Store the resolved backlog file path (e.g. `.vibe/backlog/003-login-crash.md`) — it will be needed at Step 8.

Use the extracted title + description + acceptance criteria as the bug report for all subsequent steps, in place of the raw `$ARGUMENTS` string.

**If `$ARGUMENTS` does not match a backlog reference:** proceed normally — treat `$ARGUMENTS` as the free-form bug description.

---

Read `$ARGUMENTS` carefully. Identify:
- What is the observed (broken) behavior?
- What is the expected (correct) behavior?
- Where in the codebase is the issue likely located?

Read, in order:
- `.vibe/index.md` if it exists — to identify which module the bug likely belongs to
- The relevant `.vibe/modules/[name].md` for that area
- `.vibe/glossary.md` if it exists — to check terminology
- `.vibe/escalations.md` if it exists — past dead ends; check whether an `open` entry concerns this bug or the area it touches
- The actual source files to locate the root cause

### Terminology check

Compare the terms used in `$ARGUMENTS` against `.vibe/glossary.md`:
- If a term is a synonym or near-synonym of a glossary term: correct the user before proceeding — "The term X is not in the glossary, did you mean Y?"
- If a term is ambiguous: ask for clarification

Do not proceed with the fix until terminology is aligned.

If the bug description is too vague to reproduce deterministically, ask ONE clarifying question before proceeding.

## Step 1b — Baseline check

Before planning anything, establish the current state of the project.

1. Run the test suite (from manifest): record how many tests pass and how many fail.
   - If tests fail: note the failures as **pre-existing** — do not fix them now (unless one of them IS the reported bug), but list them in Step 2 under the assumptions.
2. If the project has a build step (compiled language, bundler, etc.): run the build command.
   - If the build fails: this is a blocker — report it to the user before proceeding. Do not plan over a broken build.
3. If the project has a run/dev command (server, CLI, script): attempt a quick start to verify it doesn't crash immediately.
   - Run the command, wait 3–5 seconds, then stop it. If it crashes on startup: report the error. If it starts: note that the baseline is healthy.

Record the baseline results — they will be referenced in Step 2 and Step 9.

## Step 2 — Plan (must be validated before proceeding)

Present the fix plan to the user and **wait for explicit approval** before writing any code.

The user is a Product Owner, not a developer: present the plan in plain, non-technical language. **Never mention file names, class/function/method/variable names, or other implementation details.**

The plan must cover, in a few short sentences:
- **Le problème observé** — what's broken, from a user-visible perspective
- **La cause probable** — why it happens, in plain language (e.g. "l'appli ne vérifie pas qu'un champ est rempli avant de continuer" rather than "missing null check")
- **Ce qui va changer** — what will be fixed, described functionally
- **Comment on va vérifier que c'est corrigé** — the scenario that will be tested, phrased as a user action and the expected result, plus a plain description of how the fix will be exercised for real at runtime (e.g. "on va relancer l'appli et rejouer le scénario qui plantait")
- **Hypothèses** — any assumption made because the report was ambiguous, in plain language; mention if pre-existing test failures were found (Step 1b) without technical detail

Keep the technical analysis (exact root cause in code terms, files/modules to touch, technical test strategy) in your own working notes — it guides the fix but is not part of what you show the user.

Do not write a single line of code until the user approves the plan. If the user requests changes, update and re-present.

## Step 2b — Create task list

Once the plan is approved and before writing any code, invoke the `vibe:tasks` skill (Skill tool) to create the full task list below. **Keep subject names short (≤ 30 chars)** — they appear in the status line. `vibe:tasks` creates the tasks via `TaskCreate`, or falls back to a scratchpad checklist if that tool is unavailable — either way, its instructions then govern how every later "Mark the task ... completed" instruction in this skill is carried out.

Pass these tasks as `$ARGUMENTS`, in order, chained with `blockedBy`:

```
[Fix] Write failing test   ← no dependency
[Fix] Implement            ← blockedBy "[Fix] Write failing test"
[Fix] Runtime smoke        ← blockedBy "[Fix] Implement"
[Fix] Refactor + lint      ← blockedBy "[Fix] Runtime smoke"
Update CHANGELOG.md        ← blockedBy "[Fix] Refactor + lint"
Update docs                ← blockedBy "Update CHANGELOG.md"
Sync .vibe/                ← blockedBy "Update docs"
Commit                     ← blockedBy "Sync .vibe/"
```

If the bug was loaded from a backlog file (detected in Step 1), append one additional task, blocked by "Commit":

```
Update backlog status  ← blockedBy "Commit"
```

All tasks are created upfront. Do not start coding until the full list is created.

## Step 3 — Reproduce in a test first (red)

Mark the `[Fix] Write failing test` task `in_progress` with TaskUpdate.

Before touching any implementation:

1. Write a failing test that captures exactly the bug:
   - The test must **fail** with the current code (proving the bug exists)
   - The test must describe the expected correct behavior
   - Place it in the appropriate existing test file, or create one if needed
2. Run the test command (from manifest) and confirm the new test **fails**
   - If it passes without any fix, the test does not reproduce the bug — revise it

Test name must describe the bug scenario:
- ✅ `"does not crash when input list is empty"`
- ❌ `"bug fix test"`

### Avoid tautological tests

A test that cannot fail for a wrong fix is worse than no test — it gives false confidence while masking the bug behind a green suite. Before considering the test valid, check it does not fall into one of these patterns:
- **Self-referential assertion**: the expected value is derived using the same computation as the code under test, so a wrong fix would still satisfy it. Pin an exact, independently-derived expected value instead.
- **Trivially true assertion**: `expect(true).toBe(true)`, asserting a mock returns exactly what it was just configured to return, asserting an object equals itself.
- **Mock over-configuration**: mocking so much of the dependency chain that the assertion only checks the mock was called, never that the real logic now produces the correct result.
- **No-op coverage**: the test exercises the buggy code path but asserts something unrelated to the actual bug (e.g. asserting the function didn't throw, when the bug was a wrong output value).

Confirming the test fails before the fix (point 2 above) is necessary but **not sufficient** — a test can fail for the right reason today and still be tautological once "fixed" with the wrong change. Self-check: **could a plausible-but-wrong fix still make this test pass?** If yes, rewrite the assertion before moving on.

Mark the task `completed`, then mark the `[Fix] Implement` task `in_progress`.

## Step 4 — Fix the bug (green)

Write the minimum change to make the failing test pass without breaking existing tests.

Run the full test suite after each meaningful change. All tests must remain green — if existing tests break, the fix has a regression; address it before continuing.

### Self-correction loop

If tests fail after the fix:
- Diagnose the failure
- Fix the code
- Re-run the full test suite
- Repeat up to 3 times before escalating to the user with a precise diagnosis (append the entry to the escalation log first — see "Escalation log" above)

Mark the task `completed`, then mark the `[Fix] Runtime smoke` task `in_progress`.

## Step 4b — Runtime verification (assume it's broken)

Tests are green — that is not proof the bug is actually gone. Adopt a skeptical posture: assume it is still broken until you have personally observed the correct behavior, for real, the way a suspicious QA engineer would. Do not replay the exact reported scenario once and declare victory.

**Invoke the `run` skill** (Skill tool, `skill: "run"`) to launch and drive the app, exercising the change end-to-end and observing its real behavior. Give it as context:
- the verification scenario from the Step 2 plan
- the bug's expected (correct) behavior from Step 1
- at least one edge case or nearby scenario to drive for real, in addition to the exact scenario that triggered the bug — not just asserted in a test, actually triggered and observed

### Interpret the result

**If `run` confirms the behavior matches the expected (correct) behavior:** mark the `[Fix] Runtime smoke` task `completed`, then mark the `[Fix] Refactor + lint` task `in_progress`.

**If `run` reports it could not launch the app due to missing configuration** (missing env var, config file, secret): identify exactly what is missing from its output, create a minimal stub — a `.env.test` with placeholder values, or a stub config file — sufficient to allow the scenario to run, and re-invoke `run`.

**Self-correction loop:**
- If the bug still manifests, `run` reports a new error, or it cannot get the app launched at all: diagnose, fix the code (not the stub, unless the stub was wrong), re-invoke `run`.
- Repeat up to **3 attempts** total.
- If it still fails after that: append the entry to the escalation log (see "Escalation log" above), then stop and escalate to the user with `run`'s exact findings and what was tried.

Do not mark the task `completed` until `run` confirms the scenario behaves correctly.

## Step 5 — Clean up

With all tests green:
- Remove any debug artifacts introduced during investigation (console.log, print, dbg!, etc.)
- Run the lint command (from manifest) and fix any issues
- Re-run tests to confirm still green
- Re-run the runtime smoke test from Step 4b to confirm the cleanup did not break runtime behavior. If it fails, treat it as a regression: fix before marking the task completed.

Mark the task `completed`.

## Step 6 — Update CHANGELOG.md

Mark the `Update CHANGELOG.md` task `in_progress`.

Add an entry under `## [Unreleased]` > `### Fixed`:

```markdown
- [one-line human-readable description of what was fixed, from a user perspective]
```

Rules:
- Write for the end user ("Fixed crash when submitting an empty form" not "Fixed null check in handleSubmit()")
- If `CHANGELOG.md` does not exist, create it with the Keep a Changelog header and the entry
- If `## [Unreleased]` does not exist, add it at the top below the header
- If `### Fixed` does not exist under [Unreleased], add it

Mark the task `completed`.

## Step 6b — Update docs

Mark the `Update docs` task `in_progress`.

Most fixes do NOT touch documentation. Only if the fix changes a behavior that is documented — e.g. a command described in the README `usage` section behaved incorrectly — AND `README.md` contains `vibe:` managed section markers: **invoke the `vibe:docs` skill** using the Skill tool (`skill: "vibe:docs"`) to refresh the impacted sections. The modified files will be part of the commit in Step 8.

Otherwise: skip with a one-line explanation in the report.

Mark the task `completed`.

## Step 7 — Sync .vibe/

Mark the `Sync .vibe/` task `in_progress`.

If the `.vibe/` directory exists: **invoke the `vibe:sync` skill** using the Skill tool (`skill: "vibe:sync"`) — it will detect changed files via git and update only the affected modules.

If `.vibe/` does not exist: skip — the user can run `/vibe:sync` to generate it.

Mark the task `completed`.

## Step 8 — Commit

Mark the `Commit` task `in_progress`.

Stage all modified and created files (exclude `.env`, secrets) and commit:
- Message format: `fix: [changelog entry text, written for a developer]`

Mark the task `completed`.

If the bug was loaded from a backlog file:
- Mark the "Update backlog status" task `in_progress`.
- Create `.vibe/backlog/done/` if it does not exist.
- Move the backlog file: `git mv .vibe/backlog/NNN-slug.md .vibe/backlog/done/NNN-slug.md`
- In the moved file, replace `status: in_progress` with `status: done` in the frontmatter.
- Stage all changes and create a second commit: `chore: close backlog item NNN`
- Mark the "Update backlog status" task `completed`.

## Step 9 — Report to user

Summarize concisely:
- Root cause of the bug (1 sentence)
- What was changed to fix it (1 sentence)
- The test name that now covers this bug
- Runtime smoke test result: the scenario replayed and its outcome
- Full test suite status: X tests passing (mention pre-existing failures from Step 1b, if any)
- Lint status
- The changelog entry that was added

### Pre-existing failures follow-up

If Step 1b recorded pre-existing test failures (beyond the one that IS the reported bug):
1. Check the active backlog items (`.vibe/backlog/*.md`) for one that already covers these failures — compare titles and descriptions against the failing test names.
2. If a matching item exists: mention it in the report ("already tracked by backlog item NNN").
3. Otherwise: end the report by asking the user — "N tests étaient déjà en échec avant ce travail — veux-tu que je les enregistre au backlog ?". If the user confirms, invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with a one-line description listing the failing tests.

### Review cadence hint

If `.vibe/last-review.md` exists: count the `feat:`/`fix:` commits made since the `commit` hash it records (e.g. `git log <hash>..HEAD --oneline`, keeping only `feat:`/`fix:` messages). If the count is **5 or more**, append one line to the report: "💡 N changements depuis le dernier review — pense à lancer `/vibe:review`." If the marker does not exist or the count is below 5: say nothing.
