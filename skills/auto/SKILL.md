---
name: auto
description: Work the backlog autonomously — implement eligible items one after another with no human gates, resuming by itself after any interruption; --push also publishes the result
argument-hint: "[max number of items to process] [--push] (empty = drain the backlog)"
version: 1.1.0
model: claude-sonnet-5-5
---

# /vibe:auto — Autonomous Backlog Runner

Pick eligible backlog items one at a time and ship them through `/vibe:feature` or `/vibe:fix` in autonomous mode (`--auto`), with no human gate. State is committed at every item boundary, so any interruption — crash, closed session, usage limit — is recovered by running `/vibe:auto` again.

`$ARGUMENTS`: an optional integer, the maximum number of items for this run (empty = until no item is eligible) — never an item reference (use `/vibe:feature NNN --auto` for one specific item) — and an optional `--push` flag: once the run is over, push and release via `vibe:publish`.

The run journal in `.vibe/auto-state.md` is the progress record; each item's own task list is created by the skill implementing it. If this skill stops anywhere with a dirty working tree, commit it as `wip: [short description]` before yielding — except while an item's agent is working: the tree is its own until the verdict lands.

## Step 0 — Resume or start

If this conversation launched an agent for an item that has not reported back (a `/loop` firing or a message landed mid-item), the run is not interrupted: say the item is still in flight and stop — never commit the tree under a working agent, never launch a second one.

Otherwise read `.vibe/auto-state.md` (format at the end).

| State | Meaning | Action |
|---|---|---|
| absent or `idle` | new run | go to Step 1 — the file is written when the first item starts (Step 3), so a run that starts nothing leaves no trace |
| `stopped` | the last run aborted on a global blocker | if HEAD is still that run's closing commit (`chore: auto run — …`) and the tree is clean, nothing was fixed since: repeat the journaled reason, launch nothing, stop; otherwise new run |
| `running`, `current` unset | interrupted between items | commit any dirty tree as `wip: resume auto run`; go to Step 1 |
| `running`, `current: NNN` now under `done/` | it finished after all | journal it `done`; go to Step 1 |
| `running`, `current: NNN` is `blocked` | the skill gave up | journal it `blocked` with its `## Blocked` reason; go to Step 1 |
| `running`, `current: NNN` still `in_progress`, or back to `todo` (never taken, or an abort put it back before it was journaled) | interrupted mid-item | commit the dirty tree as `wip: resume auto run (item NNN)`; increment `attempt`; above 2 → mark it `blocked` ("fails to resume after interruption") and journal it; otherwise re-run it (Step 3) — the skill re-plans from the committed partial work |

On resume, the limit is the original minus the items already journaled, and `--push` holds if the file or this invocation says so. Any other `status: in_progress` item in `.vibe/backlog/*.md` is an orphan from an earlier crash: put it back to `status: todo`.

## Step 1 — Select the next item

Check the limit first, on every pass — including right after a verdict: if it is set and the run's journal section already holds that many items (those journaled before a resume included), select nothing and go to Step 5.

Eligible: a top-level `.vibe/backlog/*.md` with `status: todo`, every `depends_on` number resolving to a `done` item, and not yet processed in this run. Rank eligible items by:
1. Number of other `todo` items in this repo whose `depends_on` lists it — work others wait on comes first.
2. Defects before features: an item whose title or description uses defect vocabulary (bug, crash, error, regression, "doesn't work", "broken") or that records a defect found by the internal review is a fix; anything else a feature.
3. Lowest number.

Take the top item; its fix/feature classification is recorded in the journal. No eligible item → Step 5.

## Step 2 — Run the item in a dedicated sub-agent

Persist the state first (Step 3), then process the item in its own agent (Agent tool, `subagent_type: "general-purpose"`), so only the verdict enters this conversation. Prompt: the working directory, that the run is unattended (nothing it asks will be answered), the instruction to invoke `vibe:feature` or `vibe:fix` (Skill tool) with `NNN --auto`, and to return at most 3 summary lines plus the skill's final `AUTO-RESULT:` line verbatim.

- **Strictly sequential**: never two agents at once — they share one Git working tree.
- Launching the agent is what the user asked for by running `/vibe:auto`; a session rule limiting sub-agents does not apply. If launching agents is impossible, say so and invoke the skill directly in this context, warning that a long run will consume context quickly.
- The completion notification wakes this skill; as a safety net against a hung agent, schedule one long fallback wakeup (`ScheduleWakeup`, 1200–1800 s) and reschedule if it fires early. A verdict that arrives this way lands in a turn no one is reading: surface it with `PushNotification`.

Read `AUTO-RESULT:` — `done` (shipped and closed), `blocked` (the skill marked the item; move on), `aborted` (global blocker: stop, Step 5). No usable line → derive the verdict from the real state, never from the prose: the item under `done/` is `done`, `status: blocked` is `blocked`; anything else — an agent that stopped on a question, crashed, or never took the item — is an interruption mid-item: apply Step 0's last row.

## Step 3 — Persist the state

One commit per item: before starting NNN, record the previous verdict, set `current: NNN`, `attempt: 1` (a re-run keeps the count Step 0 incremented), append NNN's journal line, commit `chore: auto run — start NNN`. The first item of a new run also creates the frontmatter (`status: running`, `started`, `limit` — `none` if empty — and `push`) and opens the run's journal section. After the verdict, update the line and clear `current` without committing — that write ships with the next boundary or closing commit.

Print one status line per item: `● NNN slug — feature|fix` when starting, `✓ NNN slug — shipped <hash>` or `⚠ NNN slug — blocked (<reason>)` when the verdict lands. With a limit set, end the verdict line with ` — K left`, K being the limit minus the items in the run's journal section; `0 left` means the next step is Step 5, never another item.

## Step 4 — Stop conditions

No eligible item, the limit reached, or an `aborted` verdict (keep the reason for the report).

## Step 5 — Close the run and report

Set `status: idle` (`stopped` after an `aborted` verdict), journal kept, clear `current`, commit `chore: auto run — N items (M done, K blocked)` — unless the run is new and started no item: then write and commit nothing, so a `/loop` firing on a drained backlog adds no commit, and the report only says why nothing was eligible (empty backlog, every item blocked or waiting on a dependency). If `--push` was given, invoke the `vibe:publish` skill now and include its result below.

Report, short and plain: a table `# | Type | Verdict | Commit`; each blocked item with its one-line reason; why the run stopped; the publish result if any; if eligible items remain, that `/loop 45m /vibe:auto` continues unattended.

If the run aborted, or the publish result includes a CI failure, lead the whole report with it (before the item table) and drop the `/loop` continuation suggestion — a human needs to look before another run ships more items on top of a broken build or deploy.

## Unattended operation

This skill resumes but never restarts itself: `/loop 45m /vibe:auto` supplies the restarts. A usage limit mid-item is just another interruption; a `/loop` firing that still hits the limit fails harmlessly and the next one resumes — prefer a long interval. One session per repo: a second session reading the state file cannot tell a working agent from an interrupted one and would resume over it. To space items apart on purpose (human review between items, cost pacing, CI capacity), pass `1` and let `/loop`'s interval set the cadence: `/loop 30m /vibe:auto 1` — one item per firing, no internal waiting.

## State file — `.vibe/auto-state.md`

```markdown
---
status: running        # running | idle | stopped (the last run aborted)
started: 2026-07-29T21:14
limit: 3               # or: none
push: true             # --push given
current: 004           # item in flight; omitted between items
attempt: 1             # resume attempts on `current`
---
# Auto run journal

## 2026-07-29T21:14 — run started (limit: 3)
- 002 — feature — done (a1b2c3d)
- 004 — fix — blocked: 3 failed runtime verifications (see escalations.md)
```

The journal is append-only across runs: each run appends its own `## [timestamp]` section.
