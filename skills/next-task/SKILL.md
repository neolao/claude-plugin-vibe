---
name: next-task
description: Pick the next eligible backlog item — across every active repo in a workspace if one is detected, otherwise in the current repo — implement it, then push and release
argument-hint: "NNN [in <repo>] (force a specific item) | auto [N] (autonomous, for /loop) | (empty — pick with confirmation)"
---

# /vibe:next-task — Cross-Repo Task Runner

Picks the next eligible piece of work, hands it to `/vibe:feature`/`/vibe:fix` (or to `/vibe:auto` in auto mode), then pushes and releases through `vibe:publish`. Two scopes, chosen automatically:
- **Workspace scope** — a hub repo (see `/vibe:workspace-init`) is detected: candidates come from every `active` repo in `repos.md`, cross-repo blockers and priorities are resolved, and downstream unblocks are checked after publishing.
- **Mono-repo scope** — no workspace, but the current directory has `.vibe/backlog/`: pick in this repo, then publish — what `/vibe:auto` alone does not do.

**Only Step 8 talks to the user.** Every nested skill (`vibe:feature`, `vibe:fix`, `vibe:auto`, `vibe:publish`, and what they pull in) ends with its own report, often looking like a final answer. Here it is intermediate data: capture it and continue to the next step in the same turn.

## Step 1 — Parse `$ARGUMENTS`

- `NNN` alone (mono-repo) or `NNN in <repo>` (workspace): **forced pick** — read that item; found → Step 6, not found → report and stop.
- `auto [N]`: **auto mode** — pick normally (Steps 2–5), skip confirmation, run the loop in the picked repo bounded by `N`. Meant for `/loop 1h /vibe:next-task auto 1`.
- Empty: **normal mode** — pick, confirm, hand off.

## Step 2 — Determine scope

Look in cwd only (never upward):
1. A `CLAUDE.md` written by `/vibe:workspace-init` (a `## Hub repo` line) → read the hub directory from it and verify the marker (`.git/` + `repos.md`).
2. Otherwise, any direct subdirectory carrying the marker.

- Marker found → **workspace scope**: read `repos.md` in the hub, keep `status: active` repos. If it looks stale (a listed directory is gone, or an unlisted sibling has `.vibe/backlog/`), fill the gap for this run by scanning siblings (`.git/` + `.vibe/backlog/`, excluding the hub) and mention it in the report.
- No marker, but cwd has `.vibe/backlog/` → **mono-repo scope**: Steps 4–5 and the cross-repo part of Step 7 do not apply.
- Neither → stop: "No workspace detected here (no hub repo, no `.vibe/backlog/` in the current directory). Run `/vibe:workspace-init` first if this should be a workspace root, or run this from inside a vibe-managed repo."

## Step 3 — Collect candidates

For each candidate repo, the top-level `.vibe/backlog/*.md` items with `status: todo` whose every `depends_on` (same repo only, by design) is `done`. The hub repo's own items are never candidates — they are workspace decisions, not implementable work.

## Step 4 — Cross-repo blockers and priority _(workspace scope)_

Cross-repo relationships live in prose (`## Notes`/`## Description`), not in `depends_on`. For each candidate:
- A reference to another repo's unresolved item, or to a version another repo has not published, keeps it blocked. **Done vs published**: "once `api#012` is done" is satisfied by `status: done`; "once `sdk` publishes v0.3.0" only by a matching pushed Git tag (`git ls-remote --tags`).
- A hub-repo decision naming this item as a priority or an unblocker counts for Step 5.
- Every other candidate repo's backlog or `CLAUDE.md` waiting on this repo+number counts as an item it would unblock.

Recommended, non-enforced phrasing for such notes: repo name plus `repo#NNN`, or "tag"/"release" plus the expected version.

## Step 5 — Score and pick _(workspace scope)_

Highest count of items unblocked, then flagged as a priority in a hub decision, then lowest number. Zero unblocked candidates anywhere → stop and list what blocks each, including hub items that need a Product Owner decision. Mono-repo scope picks the lowest-numbered candidate.

## Step 6 — Present and confirm

Skipped in auto mode. Show the pick (repo, number, title, one-paragraph reasoning) and, in workspace scope, 1–2 runner-ups with one line each; ask for confirmation before doing anything.

## Step 7 — Hand off, publish, verify

Record the starting directory (to return to it in Step 8), then move into the picked repo.

- **Auto mode**: invoke `vibe:auto` with `N --push` (or `--push` alone when unbounded) — it selects and ranks eligible items exactly as this skill would, runs them with `--auto`, and publishes at the end.
- **Normal mode / forced pick**: classify the item (defect vocabulary → fix, otherwise feature) and invoke `vibe:feature NNN` or `vibe:fix NNN` with its normal human gates. Whatever it reports — done, plan rejected, early exit — continue: invoke `vibe:publish` so that everything committed locally, including a `wip:` commit, reaches the remote.

Then, **workspace scope only**, re-check downstream: for every other active repo, any item or `CLAUDE.md` passage waiting on this repo or item. Apply the done-vs-published distinction — a version-phrased wait is resolved only if a tag was actually pushed; if nothing was released and a downstream item needs a published version, it is still blocked, say so. List newly unblocked items by repo, number, title.

## Step 8 — Report

Return to the starting directory (matters for chained `/loop` firings). Short, plain sentences: what was implemented (every item and verdict in auto mode); `vibe:publish`'s push, release, and forge results; downstream items newly unblocked (workspace scope); any blocker needing the user before the next run.
