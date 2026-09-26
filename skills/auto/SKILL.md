---
name: auto
description: Work the backlog autonomously — implement eligible items one after another with no human gates, resuming by itself after any interruption; --push also publishes the result
argument-hint: "[max number of items to process] [--push] (empty = drain the backlog)"
---

# /vibe:auto — Autonomous Backlog Runner

Pick eligible backlog items one at a time and ship them through `/vibe:feature` or `/vibe:fix` in autonomous mode (`--auto`), with no human gate. State is committed at every item boundary, so any interruption — crash, closed session, usage limit — is recovered by running `/vibe:auto` again.

`$ARGUMENTS`: an optional integer, the maximum number of items for this run (empty = until no item is eligible) — never an item reference (use `/vibe:feature NNN --auto` for one specific item) — and an optional `--push` flag: once the run is over, push and release via `vibe:publish`.

The run journal in `.vibe/auto-state.md` is the progress record; each item's own task list is created by the skill implementing it. If this skill stops anywhere with a dirty working tree, commit it as `wip: [short description]` before yielding.

## Step 0 — Resume or start

Read `.vibe/auto-state.md` (format at the end).

| State | Meaning | Action |
|---|---|---|
| absent, `idle`, or `stopped` | new run | write the file with `status: running`, the timestamp, and the limit (`none` if empty); go to Step 1 |
| `running`, `current` unset | interrupted between items | commit any dirty tree as `wip: resume auto run`; go to Step 1 |
| `running`, `current: NNN` now under `done/` | it finished after all | journal it `done`; go to Step 1 |
| `running`, `current: NNN` is `blocked` | the skill gave up | journal it `blocked` with its `## Blocked` reason; go to Step 1 |
| `running`, `current: NNN` still `in_progress` | interrupted mid-item | commit the dirty tree as `wip: resume auto run (item NNN)`; increment `attempt`; above 2 → mark it `blocked` ("fails to resume after interruption") and journal it; otherwise re-run it (Step 3) — the skill re-plans from the committed partial work |

On resume, the limit is the original minus the items already journaled. Any other `status: in_progress` item in `.vibe/backlog/*.md` is an orphan from an earlier crash: put it back to `status: todo`.

## Step 1 — Select the next item

Check the limit first, on every pass — including right after a verdict: if it is set and the run's journal section already holds that many items (those journaled before a resume included), select nothing and go to Step 5.

Eligible: a top-level `.vibe/backlog/*.md` with `status: todo`, every `depends_on` number resolving to a `done` item, and not yet processed in this run. Rank eligible items by:
1. Number of other `todo` items in this repo whose `depends_on` lists it — work others wait on comes first.
2. Defects before features: an item whose title or description uses defect vocabulary (bug, crash, error, regression, "doesn't work", "broken") or that came from a `/vibe:review` finding is a fix; anything else a feature.
3. Lowest number.

Take the top item; its fix/feature classification is recorded in the journal. No eligible item → Step 5.

## Step 2 — Run the item in a dedicated sub-agent

Persist the state first (Step 3), then process the item in its own agent (Agent tool, `subagent_type: "general-purpose"`), so only the verdict enters this conversation. Prompt: the working directory, the instruction to invoke `vibe:feature` or `vibe:fix` (Skill tool) with `NNN --auto`, and to return at most 3 summary lines plus the skill's final `AUTO-RESULT:` line verbatim.

- **Strictly sequential**: never two agents at once — they share one Git working tree.
- Launching the agent is what the user asked for by running `/vibe:auto`; a session rule limiting sub-agents does not apply. If launching agents is impossible, say so and invoke the skill directly in this context, warning that a long run will consume context quickly.
- The completion notification wakes this skill; as a safety net against a hung agent, schedule one long fallback wakeup (`ScheduleWakeup`, 1200–1800 s) and reschedule if it fires early. A verdict that arrives this way lands in a turn no one is reading: surface it with `PushNotification`.

Read `AUTO-RESULT:` — `done` (shipped and closed), `blocked` (the skill marked the item; move on), `aborted` (global blocker: stop, Step 5). No usable line → derive the verdict from the real state (item status, `git log`, `git status`), not from the prose.

## Step 3 — Persist the state

One commit per item: before starting NNN, record the previous verdict, set `current: NNN`, `attempt: 1`, append NNN's journal line, commit `chore: auto run — start NNN`. After the verdict, update the line and clear `current` without committing — that write ships with the next boundary or closing commit.

Print one status line per item: `● NNN slug — feature|fix` when starting, `✓ NNN slug — shipped <hash>` or `⚠ NNN slug — blocked (<reason>)` when the verdict lands. With a limit set, end the verdict line with ` — K left`, K being the limit minus the items in the run's journal section; `0 left` means the next step is Step 5, never another item.

## Step 4 — Stop conditions

No eligible item, the limit reached, or an `aborted` verdict (keep the reason for the report).

## Step 5 — Close the run and report

Set `status: idle` (journal kept), clear `current`, commit `chore: auto run — N items (M done, K blocked)`. If `--push` was given, invoke the `vibe:publish` skill now and include its result below.

Report, short and plain: a table `# | Type | Verdict | Commit`; each blocked item with its one-line reason; why the run stopped; the publish result if any; if `.vibe/last-review.md` exists and 5 or more `feat:`/`fix:` commits landed since its hash, "💡 N changes since the last review — consider running `/vibe:review`."; if eligible items remain, that `/loop 45m /vibe:auto` continues unattended.

If the publish result includes a CI failure, lead the whole report with it (before the item table) and drop the `/loop` continuation suggestion — a human needs to look before another run ships more items on top of a broken deploy.

## Unattended operation

This skill resumes but never restarts itself: `/loop 45m /vibe:auto` supplies the restarts. A usage limit mid-item is just another interruption; a `/loop` firing that still hits the limit fails harmlessly and the next one resumes — prefer a long interval. To space items apart on purpose (human review between items, cost pacing, CI capacity), pass `1` and let `/loop`'s interval set the cadence: `/loop 30m /vibe:auto 1` — one item per firing, no internal waiting.

## State file — `.vibe/auto-state.md`

```markdown
---
status: running        # running | idle | stopped
started: 2026-07-29T21:14
limit: 3               # or: none
current: 004           # item in flight; omitted between items
attempt: 1             # resume attempts on `current`
---
# Auto run journal

## 2026-07-29T21:14 — run started (limit: 3)
- 002 — feature — done (a1b2c3d)
- 004 — fix — blocked: 3 failed runtime verifications (see escalations.md)
```

The journal is append-only across runs: each run appends its own `## [timestamp]` section.
