---
name: fix
description: Fix a bug using TDD (reproduce first), then update CHANGELOG.md under [Unreleased] > Fixed
argument-hint: <bug description in natural language>
version: 2.1.0
model: claude-sonnet-5-5
---

# /vibe:fix — TDD Bug Fix

Fix the bug described in `$ARGUMENTS`: the user is the Product Owner only and never tests code manually.

**First read the shared implementation workflow** at `${CLAUDE_PLUGIN_ROOT}/skills/feature/workflow.md` (`workflow.md` in the `feature` skill's directory): standing commit rule, `--auto` mode and its verdict line, escalation log, usage report, backlog resolution, baseline check, need framing, expert consultation, implementation framing, plan presentation, task list, red/green (delegated to `vibe:task-implementer`)/runtime/refactor loop, internal review and its routing, CHANGELOG, docs, sync, commit, final checks, report, debrief. This file only defines what is specific to a bug fix. Prefix: `fix:`; entry: `fix`.

## Step 1 — Understand the bug

Resolve `$ARGUMENTS` (backlog reference or free-form report), then identify the observed behaviour, the expected behaviour, and where in the codebase the cause likely lies: `.vibe/index.md` and the relevant module file to locate the area, then the source files to find the root cause. Settle terminology as the workflow describes. A report too vague to reproduce deterministically is for the need framing to settle (observed behaviour, expected behaviour, how to trigger it), not a question of your own.

Then run the baseline check — a pre-existing failure that *is* the reported bug is not pre-existing — and frame the need.

## Step 2 — Plan

Expert consultation will often select no expert — that is expected; the implementation framing then mostly confirms the root cause and the test. Present the plan covering: the observed problem (user-visible), the likely cause in plain language ("the app doesn't check a field is filled in before continuing", not "missing null check"), what will change, how it will be verified (the scenario as a user action and expected result, plus how the fix is exercised for real at runtime), and the assumptions.

Task list: one group labelled `[Fix]` (`Red → green`, `Runtime smoke`, `Refactor + lint`), then the closing tasks.

## Steps 3–5 — Red, green, runtime, refactor

The first test reproduces the bug exactly: it fails on the current code, proving the bug exists, and describes the correct behaviour ("does not crash when input list is empty"). A test that passes before the fix does not reproduce the bug — the implementer revises it. The tautology check applies as "could a plausible-but-wrong fix still pass this?". The implementer's prompt names the observed and expected behaviour and the likely root cause from the plan, so the fix lands where the cause is, not at the caller. Then the minimum change that makes it pass without breaking existing tests; runtime verification replays the reported scenario plus a nearby one. Follow the workflow loop.

## Step 6 — Internal review

Follow the workflow's loop. Request handed to the reviewers: the need's decisions (observed, expected, trigger) and, for a backlog item, its acceptance criteria. A `review-correctness` finding at the wrong altitude (the caller patched while the shared helper is the cause) is an implementation finding that sends the fix back to its framing.

## Steps 7–9 — CHANGELOG, docs, sync, commit

CHANGELOG section: `### Fixed` ("Fixed crash when submitting an empty form", not "Fixed null check in handleSubmit()"). Docs condition: the fix changes a documented behaviour (most fixes do not). Commit with `fix:`.

## Step 10 — Report

Root cause (1 sentence); what changed (1 sentence); the test that now covers the bug; the runtime scenario replayed and its outcome; full suite status; lint status; the changelog entry; experts consulted, if any; then the workflow's pre-existing-failures line. The draft goes through the workflow's final checks before it reaches the user.
