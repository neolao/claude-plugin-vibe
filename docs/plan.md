# Implementation plan

This plan turns [the strategy](strategy/README.md) into work packages, starting from what exists. The strategy says what and why; this plan says with what, and in which order.

## Starting decisions

- **One orchestrator, for building.** `/vibe:feature` and `/vibe:fix` stay as the two entries; `skills/feature/workflow.md` stays the single file both read. The orchestrator is this workflow, reshaped.
- **Review and verification become steps of the build loop**, never a report the PO reads. `/vibe:review` and `/vibe:verify` leave the `/` menu.
- **Every brick ships with its eval cases**, like today. A changed brick bumps its `version:` and gets a new row in `evals/results/history.md`.
- **Usage reports stay on the user's machine.** The routine reads only what the user shares, and otherwise works from synthetic cases.
- **Order: bricks first, then the loop, then the surface.** A brick can be evaluated alone before the workflow depends on it.
- **Eval runs are the maintainer's call.** A package writes its cases; running them (`claude plugin eval`, `evals/docker/run.sh`) costs real tokens and is never launched without an explicit request. A "done when" that cites a score is checked by the maintainer, not by the session that wrote the package.

## What exists, and what it becomes

| Strategy element | Existing | Becomes |
|---|---|---|
| Sequence held by tasks | `tasks` 2.0.0 (native or `tasks.tsv`) | Kept. Add: bulk abandon of stale tasks when the loop goes back to a framing, round prefix, counters for the usage report. |
| Frame the need / the implementation | `clarify` 1.1.0: one design tree, standalone or called by `backlog`, `init`, `workspace-init` | Two modes of the same skill, `need` and `implementation`, each with its own sources (request and `.vibe/` first; code first) and the rule "the PO is asked only when neither holds the answer". Hidden from the menu. |
| Expert consultation | `expert-*` agents called from `workflow.md` at plan time | Kept. Called by the `implementation` framing. |
| Write the code | The main session codes itself (`Red`, `Green`, `Refactor` in `workflow.md`) | Delegated to `task-implementer`, one sub-task per launch (package 7). |
| Internal review | `review` 1.1.0: picks agents from CLAUDE.md, dedups, fixes high and medium, reports low | Hidden brick. Returns raw findings to the loop; it no longer decides severity or fixes. |
| Classify findings | Step 4 of `review` (merge, normalize severity) | New agent `review-classifier`: re-checks each finding against its source, drops false positives, merges, sets level (high / medium / low) and space (problem / solution). |
| Conformity to the request | `verify` 1.0.0, scope grid | New agent `requirements-reviewer`, from the scope grid. The rigor and finish grids are covered by `review-correctness`, the claim check and the clarity pass. `verify` is removed. |
| Claims carry their proof | Nothing beyond the classifier | New agent `claim-verifier`: checks the final report's claims (tests run, feature exercised) against the trace. |
| Clarity of the text the PO reads | `rewrite` 1.0.0, writes after validation | Hidden brick with a `direct` mode that rewrites the report without asking. |
| Project memory | `debrief` 1.0.0, end-of-task retrospective | Kept, called at the end of the orchestrator. The `need` framing reads the memory before asking the PO. |
| Opt-in judgement | `challenge`, `consult`, `learn` | Kept as commands, unchanged. |
| Report a misbehavior | `report-issue` 1.0.0 | Removed. Replaced by the routine. |
| Continuous improvement | `scheduled-tasks/improve-skills-and-agents/SKILL.md` | Kept. Add: write a red case from a shared usage report or a logged escalation, then fix the brick to green. |
| Usage report | Nothing (`.vibe/escalations.md` is the closest) | New hidden skill `report`: a `.vibe/reports/<date>-<entry>.md` with statistics only, never project detail. Shared only by the user. |
| Everything else | `backlog`, `auto`, `next-task`, `publish`, `init`, `sync`, `docs`, `changelog`, `release`, `workspace-init` | Kept. `auto` and `next-task` inherit the new loop through `workflow.md`. |

## Work packages

### 1. Base: tasks and usage report

- **`tasks`**: bulk abandon of `pending` tasks made stale by a return to a framing (`deleted`, one by one, never a `completed` one), new round tasks prefixed `Round <n> — `. Tested in `evals/tasks-script-test.sh`.
- **`report`** (hidden skill, `user-invocable: false`): `init`, one call per event (brick called, round, question asked to the PO, findings per level and space, returns to a framing, fixes), `write` at the end. A POSIX `sh` + `awk` script, like `tasks.sh`, refuses an unknown counter so reports stay comparable. Output in `.vibe/reports/`, which carries its own `.gitignore` (no change to `vibe:init` needed).
- **Done when:** the task script handles bulk abandon; a sample report passes a format check; both skills have a case at 1.00.
- **Progress (2026-10-18):** written — `tasks` 2.1.0 (`abandon`, "Going back" section), `report` 1.0.0, both script tests green on the host, cases `tasks-goes-back-to-an-earlier-step` and `report-counts-then-writes` written, not run (both need Docker and a maintainer's go).

### 2. Transverse bricks

- **`review-classifier`** (new agent): input the raw findings and the files; output each kept finding with its level and space, the dropped ones with the reason, the doubts it cannot settle alone as questions with a recommended option. Fixture: findings with a false positive, a duplicate pair, a need-space finding.
- **`requirements-reviewer`** (new agent): from the former `verify` skill's scope grid (removed in package 5). Input the request verbatim, the plan and the diff.
- **`claim-verifier`** (new agent): input a report and the trace (commands run, files). Flags a claim with no proof or contradicted by its source.
- **`rewrite` `direct` mode**: first line of `$ARGUMENTS`; rewrites and returns, no question.
- **Done when:** each agent has one positive and one negative case at 1.00 (a decoy from its "what is not a finding" section); `rewrite`'s existing case stays green.
- **Progress (2026-10-18):** written — the three agents (sonnet; classifier at `high`, the two others at `medium`), `rewrite` 1.1.0 with `mode: direct`, seven cases (`review-classifier-*` ×2, `requirements-reviewer-*` ×2, `claim-verifier-*` ×2, `rewrite-direct-mode-returns-text-without-asking`), fixtures' own tests green on the host. Not run.

### 3. Two framings

- `clarify` gets two modes in `$ARGUMENTS`: `need` (sources: the request, the backlog item, `.vibe/`, the project memory; questions about what, for whom, under which business constraints) and `implementation` (sources: the code; questions about approach and technical constraints; experts consulted here, moved from `workflow.md`). The standalone mode stays for `backlog`, `init` and `workspace-init`.
- Each mode may conclude "too many unknowns" and say so instead of asking round after round.
- `user-invocable: false`; the three callers keep working.
- **Done when:** a `need` case where the answer is in `.vibe/` and the PO is not asked; an `implementation` case where the answer is in the code and the PO is not asked; the existing standalone cases stay green.
- **Progress (2026-10-18):** written — `clarify` 1.2.0 (`mode: need` / `mode: implementation`, four added rules, `(source: …)` on self-settled decisions, `partial — spike: <question>`, `user-invocable: false`), cases `clarify-need-mode-answers-from-sources` and `clarify-implementation-mode-reads-the-code-first`. Expert consultation stays in `workflow.md` until package 4 wires the order; the README usage snippet still shows `/vibe:clarify` inside the managed markers, to be regenerated by `/vibe:docs` in package 5. Not run.

### 4. The build loop

- `workflow.md` is reshaped: `need` framing → `implementation` framing → plan approval → task list → Red / Green / Runtime / Refactor per sub-task → **internal review** (`review` brick, then `review-classifier`) → route: need-space finding back to `need`, implementation-space finding back to `implementation`, only low left → `requirements-reviewer` + `claim-verifier` on the report → `rewrite direct` → CHANGELOG, docs, sync, commit → `report write` → `debrief`.
- The loop has no fixed cap; each return is a new task round. `--auto` resolves the classifier's doubts by its gate table.
- `review` becomes a hidden brick: no fixes, no `.vibe/last-review.md`, no cadence hint; the orchestrator owns the commit.
- `feature` and `fix` SKILL.md only list their specifics, as today.
- **Done when:** the `feature-*` and `fix-*` cases are green with a trace showing one review round and the classifier call; a new case with a planted problem-space defect shows a return to `need`; `auto` and `next-task` cases stay green.
- **Progress (2026-10-18):** written — `workflow.md` reshaped (need framing → experts → implementation framing → plan → TDD → internal review → route → CHANGELOG/docs/sync/commit → final checks → report → `vibe:report write` → `debrief`), `review` 2.0.0 as a hidden brick (`## REVIEW …` contract, no fix, no commit, no `last-review.md`), `feature`/`fix` 2.0.0, cadence hints removed from `backlog` and `auto`. Cases: `feature-returns-to-need-on-problem-space-finding` (accepts the rule caught at framing or at review — the fixture cannot force the review path), three `review-*` cases rewritten for the brick, `feature-*`/`fix-*` happy paths get classifier/requirements/report graders and `max_turns: 140`; `backlog-reports-review-cadence-and-blocked-reason` loses its two cadence graders. Left for package 5: `backlog`'s "from review" step (dead: no review report exists any more), README usage snippet and website. Not run.

### 5. Surface

- Remove `verify` and `report-issue` (skills, their eval cases, their mentions in README, `docs/`, `.vibe/`, website demos).
- `review` and `rewrite` hidden. `challenge`, `consult`, `learn` unchanged.
- `/vibe:docs` refreshes the README; the website table and the `DEMOS` object are resynced by hand (`docs/index.html`).
- **Done when:** `grep` finds no orphan reference; `README` and site agree; `jq` passes on the manifests.
- **Progress (2026-10-18):** done on paper — `verify` and `report-issue` removed (skills, README rows, docs, `.vibe/`), `rewrite` 1.2.0 hidden, `backlog` 1.2.0 without its "from review" mode (steps renumbered, graders followed), README managed sections rewritten by hand to what `/vibe:docs` would derive, website resynced (command table 15 rows, review demo folded into the feature demo, verify/rewrite demos removed, `node --check` and tag balance green), 27 grader notes and the generated `.vibe/` files reworded. Only history, ADRs and backlog items keep `/vibe:review` as provenance. Not run.

### 6. Routine

- `scheduled-tasks/improve-skills-and-agents/SKILL.md` gains a step: read shared usage reports and `.vibe/escalations.md` entries given to it, write one red eval case per distinct misbehavior, then fix the brick to green before its usual cost pass.
- The eval corpus is mostly synthetic: each package above adds the cases that cover its brick's failure modes, since no real usage stream is expected.
- **Done when:** the routine runs once end to end on a planted escalation and produces a red-then-green case.
- **Progress (2026-10-18):** written — section 1b of the routine (inbox first, usable or rejected, brick named from the signal, synthetic red case, fix to green, file moved to `done/`), `evals/inbox/README.md`, `CLAUDE.md`, `docs/development.md`, README. The end-to-end run on a planted escalation is the maintainer's: it runs evals.

### 7. Later: delegate the code

- A `task-implementer` agent writes one sub-task out of the orchestrator's context, as the strategy suggests for long tasks. Planned after packages 1–6 were measured; the maintainer chose to write it at once and measure everything in one eval round.
- **Progress (2026-10-18):** written — `agents/task-implementer.md` 1.0.0 (sonnet · medium, writes code, `## IMPLEMENTATION report`), `workflow.md` "Red → green — delegated" (rule blocks quoted to the agent, the workflow re-runs the tests, doubts through the framing gate, three launches then escalation; runtime, lint, build and commit stay in the orchestrator), `feature`/`fix` 2.1.0, cases `task-implementer-implements-test-first` and `task-implementer-raises-doubt-instead-of-deciding`; the `feature-*`/`fix-*` graders that watched `Edit` calls now read the implementer's report and the files (a sub-agent's tool calls are not in the trace). Not run.

### 8. Review of packages 1–7

- Thirteen review agents on the change set, findings classified by `review-classifier` (its first real run): 5 high, 22 medium, 15 low, 6 doubts. The high and medium findings are fixed here; the doubts are the maintainer's.
- **Fixed (2026-10-18):** `report.sh` — `init` overwrites, `write` removes the counters and fails loudly, model id validated, `.gitignore` appended not clobbered, `entry`/`start` validated; `report` 1.1.0 writes on every exit and its lines come before `AUTO-RESULT:`; `workflow.md` — baseline commit recorded and used as review scope, Final checks before CHANGELOG/Commit and the report drafted whole before them, one owner for attempts (the workflow, per sub-task per round; the implementer only reports), "compare with the last entry of **Commands run**", all `CLARIFY-RESULT` forms routed with their `--auto` rows, two missing gates (design challenge, expert reopening the plan), a failed or empty brick relaunched once then escalated, a return round re-runs the framing on top of the previous synthesis and decisions, "same finding" defined by place and cause, Internal review split into Collect / Classify / Route / New round; `clarify` 1.3.0 — one tree file per mode, result forms defined once for every caller, merged set on a new round; `tasks` 2.1.1 — `abandon` prints the subject; routine — give-up rule by location, a rejected inbox file is deleted and flagged for history purge, inbox README asks for redaction before sharing; a guard in `evals/report-script-test.sh` checks the counter keys against the skill table, the workflow's `incr` calls and the routine's signals; stale docs and `.vibe/` files corrected (counts, fallback, next-task, `last-review.md` deleted, `models.md` contracts table). Not run.
- **Left as low or pending a doubt:** unread counters, prompt redites, `review`'s path mode and `internal` token, `rewrite`'s standalone body, renames (`review-classifier`, `report`, `abandon`), claim check on the framing's self-sourced decisions, a round cap.

## Order

1 → 2 → 3 → 4 → 5 → 6, then 7, then 8 (review). Packages 2 and 3 are independent of each other once 1 is done.
