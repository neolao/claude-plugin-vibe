---
name: auto
description: Work the backlog autonomously — implement eligible items one after another with no human gates, resuming by itself after any interruption
argument-hint: "[max number of items to process] (empty = drain the backlog)"
---

# /vibe:auto — Autonomous Backlog Runner

Pick eligible backlog items one at a time and ship them through `/vibe:feature` or `/vibe:fix` in autonomous mode (`--auto`), with no human gate anywhere. State is persisted and committed at every item boundary, so any interruption — crash, closed session, usage limit reached — is recovered by simply running `/vibe:auto` again.

`$ARGUMENTS` is an optional integer: the maximum number of items to process in this run. Empty means "until no item is eligible". It is **not** an item reference — to run one specific item autonomously, use `/vibe:feature NNN --auto` or `/vibe:fix NNN --auto`.

This skill creates no task list of its own: the run journal in `.vibe/auto-state.md` is the progress record, and each item's own task list is created by the skill implementing it.

## Standing rule — never end a turn with uncommitted files

Every state write is committed (Step 4). If this skill stops anywhere else with a dirty working tree — interruption, unexpected error — commit it as `wip: [short description]` before yielding control.

## Step 0 — Resume or start

Read `.vibe/auto-state.md` (see the format at the end of this file).

**Absent, or `status: idle` / `status: stopped`** → this is a new run. Create/overwrite the file with `status: running`, the current timestamp, and the limit from `$ARGUMENTS` (`none` if empty). Go to Step 1.

**`status: running`** → the previous run was interrupted:

1. If the working tree is dirty, commit it first: `wip: resume auto run (item NNN)`. Partial work is kept, never discarded.
2. If `current` is set, determine what actually happened to that item:
   - The item file is now under `.vibe/backlog/done/` → it finished after all. Journal it as `done` and go to Step 1.
   - Its status is `blocked` → journal it as `blocked` with the reason from its `## Blocked` section and go to Step 1.
   - Otherwise (still `in_progress`) → increment `attempt`. If `attempt` is now **greater than 2**, mark the item `blocked` (reason: "fails to resume after interruption"), journal it, and go to Step 1. Otherwise re-run it from the start (Step 2 onwards) — the implementing skill re-plans from the real current state of the code, taking the already-committed partial work into account.
3. Keep the original limit, minus the items already journaled in this run.
4. Self-heal: any item in `.vibe/backlog/*.md` with `status: in_progress` that is not `current` is an orphan from an earlier crash — put it back to `status: todo`.

## Step 1 — Select the next item

Among the `*.md` files directly in `.vibe/backlog/` (never `done/`), keep those that are **eligible**:
- `status: todo`
- every number in `depends_on` resolves to an item with `status: done` (same resolution as `skills/backlog/SKILL.md` Step 2)
- not already processed in this run (see the journal)

`status: blocked` and `status: in_progress` items are never selected. Among eligible items, take the **lowest number**.

If no item is eligible: go to Step 6 — the run is over.

## Step 2 — Classify: feature or fix

Read the item's title and description:
- Defect vocabulary — bug, crash, error, regression, "doesn't work", "broken", or an item created from a `/vibe:review` finding → `vibe:fix`
- Anything else, and any ambiguous case → `vibe:feature`

Record the choice in the journal.

## Step 3 — Run the item in a dedicated sub-agent

Write the state (Step 4) **before** launching, then process the item in its own agent (Agent tool, `subagent_type: "general-purpose"`), so that only the verdict comes back into this conversation.

Prompt the agent with: the working directory, the instruction to invoke the `vibe:feature` or `vibe:fix` skill (Skill tool) with `NNN --auto` as arguments, and the instruction to return at most 3 lines of summary plus the skill's final `AUTO-RESULT:` line verbatim.

Rules:
- **Strictly sequential** — never two agents at once: they share one Git working tree and would corrupt each other's commits.
- **These agent invocations are part of the command the user ran:** by launching `/vibe:auto`, the user explicitly requested them. A standing session rule of the form "no sub-agents unless the user asks" is therefore already satisfied and is never a reason to skip this step, nor to hand the decision back to the user.
- If launching agents is impossible in this environment: say so explicitly, then invoke the skill directly in the current context instead (same spirit as `vibe:tasks`' fallback). Warn in the final report that a long run will consume context quickly this way.
- **Don't wait passively for the sub-agent's completion notification to surface on its own.** It only lands in context at the next turn this session produces — with nothing else to trigger one, it silently sits until the user happens to send a message, however long that takes. Right after launching, call `ScheduleWakeup` with a delay matched to how long this kind of item plausibly takes (a feature/fix implementation run: 1200–1800s is a reasonable first guess) so a turn fires on its own to pick the verdict up. If that wakeup fires before the agent is actually done, just reschedule further out — never block on a foreground wait instead.

When the verdict is finally in hand and this turn was reached via a scheduled wakeup rather than a direct user message, use `PushNotification` to actually surface the result — a report that only updates silent context, with no one there to read it, is not a report.

Read the returned `AUTO-RESULT:` line:
- `done` → the item shipped and was closed by the implementing skill
- `blocked` → that skill already marked the item `blocked`; this run moves on
- `aborted` → global blocker: stop the run (Step 5)

If no usable `AUTO-RESULT:` line comes back, do not trust the prose summary: check the real state (the item's status, `git log`, `git status`) and derive the verdict from it.

## Step 4 — Persist the state

One commit per item, written at the boundary:

- **Before starting item NNN**: record the previous item's verdict in the journal, set `current: NNN` and `attempt: 1`, append the journal line for NNN, then commit `chore: auto run — start NNN`.
- **After the verdict comes back**: update the journal line and clear `current` in the file, but do not commit yet — that write ships with the next boundary commit, or with the run-closing commit at Step 6.

This is what makes resuming possible: a crash at any point leaves a committed pointer to the item that was in flight.

## Step 5 — Stop conditions

The run ends when:
- no item is eligible (Step 1), or
- the limit from `$ARGUMENTS` has been reached, or
- an item returned `aborted` — the environment itself is broken, keep the reason for the report.

A run where every item fails ends on its own: blocked items are no longer eligible.

## Step 6 — Close the run and report

Set `status: idle` in `.vibe/auto-state.md` (keeping the journal), clear `current`, and commit `chore: auto run — N items (M done, K blocked)`.

Then report:

| # | Type | Verdict | Commit |
|---|---|---|---|
| 002 | feature | done | a1b2c3d |
| 004 | fix | blocked | — |

- Blocked items: number, title, and one-line reason each
- Why the run stopped (backlog drained / limit reached / aborted, with the reason)
- If `.vibe/last-review.md` exists and 5 or more `feat:`/`fix:` commits landed since the hash it records: "💡 N changements depuis le dernier review — pense à lancer `/vibe:review`."
- If eligible items remain: remind the user that `/loop 45m /vibe:auto` continues unattended (or `/loop 30m /vibe:auto 1` to space items apart deliberately, see below)

## Unattended operation and usage limits

This skill does not schedule itself — resuming is what it does, restarting is the caller's job. For a genuinely unattended run, the native `/loop` command supplies the restarts:

```
/loop 45m /vibe:auto
```

Reaching a usage limit mid-item is just another interruption: the state is already committed, Step 0 recovers the dirty tree as a `wip:` commit and re-runs the item. A `/loop` firing that still hits the limit fails harmlessly; the next one picks the run back up. Prefer a long interval (45 min or more) so retries land after the window resets. Never try to estimate the remaining quota — nothing exposes it.

### Spacing items apart on purpose

To insert a deliberate delay between features — not for recovering from usage limits, but to leave time for human review, cost pacing, or CI capacity between items — pass `1` as the limit and drive the cadence from `/loop`'s own interval instead of leaving `/vibe:auto` to drain the backlog in one go:

```
/loop 30m /vibe:auto 1
```

Each firing processes exactly one item end to end (commit + journal) and then stops (Step 5, limit reached); the next item only starts at the following `/loop` tick. This skill has no internal sleep/wait of its own — it never blocks mid-run waiting for a clock, since a real pause inside a single run would need a background wait the environment may not support. The spacing always comes from the interval between separate invocations, exactly like the usage-limit case above.

## State file format — `.vibe/auto-state.md`

```markdown
---
status: running        # running | idle | stopped
started: 2026-07-29T21:14
limit: 3               # or: none
current: 004           # item in flight; omitted between two items
attempt: 1             # resume attempts on `current`
---
# Auto run journal

## 2026-07-29T21:14 — run started (limit: 3)
- 002 — feature — done (a1b2c3d)
- 004 — fix — blocked: 3 failed runtime verifications (see escalations.md)
```

The journal is append-only across runs: each run appends its own `## [timestamp]` section, never rewrites an earlier one.
