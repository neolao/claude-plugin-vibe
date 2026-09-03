---
name: fix
description: Fix a bug using TDD (reproduce first), then update CHANGELOG.md under [Unreleased] > Fixed
argument-hint: <bug description in natural language>
---

# /vibe:fix — TDD Bug Fix

Fix the bug described in `$ARGUMENTS`: the user is the Product Owner only and never tests code manually.

**First read the shared implementation workflow** at `${CLAUDE_PLUGIN_ROOT}/skills/feature/workflow.md` (`workflow.md` in the `feature` skill's directory): standing commit rule, `--auto` mode and its verdict line, escalation log, backlog resolution, baseline check, expert consultation, plan presentation, task list, red/green/runtime/refactor loop, CHANGELOG, docs, sync, commit, report. This file only defines what is specific to a bug fix. Prefix: `fix:`.

## Step 1 — Understand the bug

Resolve `$ARGUMENTS` (backlog reference — often a bug filed from a `/vibe:review` finding — or free-form report), then identify the observed behaviour, the expected behaviour, and where in the codebase the cause likely lies: `.vibe/index.md` and the relevant module file to locate the area, then the source files to find the root cause. Settle terminology as the workflow describes. If the report is too vague to reproduce deterministically, ask one clarifying question.

Then run the baseline check — a pre-existing failure that *is* the reported bug is not pre-existing.

## Step 2 — Plan

Expert consultation will often select no expert — that is expected. Present the plan covering: the observed problem (user-visible), the likely cause in plain language ("the app doesn't check a field is filled in before continuing", not "missing null check"), what will change, how it will be verified (the scenario as a user action and expected result, plus how the fix is exercised for real at runtime), and the assumptions.

Task list: one group labelled `[Fix]` (`Write failing test`, `Implement`, `Runtime smoke`, `Refactor + lint`), then the closing tasks.

## Steps 3–5 — Red, green, runtime, refactor

The first test reproduces the bug exactly: it fails on the current code, proving the bug exists, and describes the correct behaviour ("does not crash when input list is empty"). A test that passes before the fix does not reproduce the bug — revise it. The tautology check applies as "could a plausible-but-wrong fix still pass this?". Then the minimum change that makes it pass without breaking existing tests; runtime verification replays the reported scenario plus a nearby one. Follow the workflow loop.

## Steps 6–8 — CHANGELOG, docs, sync, commit

CHANGELOG section: `### Fixed` ("Fixed crash when submitting an empty form", not "Fixed null check in handleSubmit()"). Docs condition: the fix changes a documented behaviour (most fixes do not). Commit with `fix:`.

## Step 9 — Report

Root cause (1 sentence); what changed (1 sentence); the test that now covers the bug; the runtime scenario replayed and its outcome; full suite status; lint status; the changelog entry; experts consulted, if any; then the workflow's pre-existing-failures and review-cadence lines.
