---
name: next-task
description: Pick the next eligible backlog item — across every active repo in a workspace if one is detected, otherwise in the current repo — implement it, then push and release
argument-hint: "NNN [in <repo>] (force a specific item) | auto [N] (autonomous, for /loop) | (empty — pick with confirmation)"
version: 1.1.0
model: claude-sonnet-5-5
---

# /vibe:next-task — Cross-Repo Task Runner

Picks the next eligible piece of work, hands it to `/vibe:feature`/`/vibe:fix` (with `--auto` in auto mode), then pushes and releases through `vibe:publish`. Two scopes, chosen automatically:
- **Workspace scope** — a hub repo (see `/vibe:workspace-init`) is detected: candidates come from every `active` repo in `repos.md`, cross-repo blockers and priorities are resolved, and downstream unblocks are checked after publishing.
- **Mono-repo scope** — no workspace, but the current directory has `.vibe/backlog/`: pick in this repo, then publish — like `/vibe:auto 1 --push`, but with a confirmation and the build skill's normal human gates outside auto mode.

**Only Step 8 talks to the user.** Every nested skill (`vibe:feature`, `vibe:fix`, `vibe:publish`, and what they pull in) ends with its own report, often looking like a final answer. Here it is intermediate data: capture it and continue to the next step in the same turn.

## Step 1 — Parse `$ARGUMENTS`

- `NNN` alone (mono-repo) or `NNN in <repo>` (workspace): **forced pick** — read that item; found → Step 6, not found → report and stop.
- `auto [N]`: **auto mode** — pick normally (Steps 2–5), skip confirmation, hand off up to `N` items (empty = until nothing is eligible), each picked afresh after the previous verdict. Unattended, meant for `/loop 1h /vibe:next-task auto 1`: nothing asks a question in this mode — the stops of Steps 1, 2 and 5 are reports, the build skills run with `--auto`, and `vibe:publish` answers nested questions in its place — so the turn never ends waiting for an answer.
- Empty: **normal mode** — pick, confirm, hand off.

## Step 2 — Determine scope

Look in cwd only (never upward):
1. A `CLAUDE.md` written by `/vibe:workspace-init` (a `## Hub repo` line) → read the hub directory from it and verify the marker (`.git/` + `repos.md`).
2. Otherwise, any direct subdirectory carrying the marker.

- Marker found → **workspace scope**: read `repos.md` in the hub, keep `status: active` repos. Only its `Repo` and `Status` columns are read, in whatever order and alongside whatever other columns the table holds (`Role`, `Remote`, a hand-added `Path` or `Owner`); `Repo` is the sibling's directory name under the workspace root. The registry is stale when an `active` row's directory is gone, or when an unlisted sibling has `.git/` + `.vibe/backlog/` — a `planned`, `idea` or `archived` row needs no directory and is never questioned. Fill the gap for this run: add each unlisted sibling with `.git/` + `.vibe/backlog/` (the hub excluded) as `active`; a registered row keeps its status whatever the scan finds, so an `archived` repo whose directory is still there stays out. Mention it in the report.
- No marker, but cwd has `.vibe/backlog/` → **mono-repo scope**: Step 4, the workspace tiers of Step 5 and the cross-repo part of Step 7 do not apply.
- Neither → stop: "No workspace detected here (no hub repo, no `.vibe/backlog/` in the current directory). Run `/vibe:workspace-init` first if this should be a workspace root, or run this from inside a vibe-managed repo."

## Step 3 — Collect candidates

For each candidate repo, the top-level `.vibe/backlog/*.md` items with `status: todo` whose every `depends_on` (same repo only, by design) is `done`. The hub repo's own items are never candidates — they are workspace decisions, not implementable work.

## Step 4 — Cross-repo blockers and priority _(workspace scope)_

Cross-repo relationships live in prose (`## Notes`/`## Description`), not in `depends_on`. For each candidate:
- A reference to another repo's unresolved item, or to a version another repo has not published, keeps it blocked. **Done vs published**: "once `api#012` is done" is satisfied by `status: done`; "once `sdk` publishes v0.3.0" only by a matching pushed Git tag. Never conclude "not released" from the backlog or from memory: run `git -C <that repo> ls-remote --tags` (and `git -C <that repo> tag` when it has no remote) and read the result.
- A hub-repo decision naming this item as a priority or an unblocker counts for Step 5.
- Every other candidate repo's backlog or `CLAUDE.md` waiting on this repo+number counts as an item it would unblock.

Recommended, non-enforced phrasing for such notes: repo name plus `repo#NNN`, or "tag"/"release" plus the expected version.

## Step 5 — Score and pick

Rank the unblocked candidates, the same tiers as `vibe:auto` with the workspace ones added:
1. Highest count of items unblocked — the same-repo `todo` items whose `depends_on` lists it, plus, in workspace scope, the cross-repo count of Step 4.
2. Flagged as a priority in a hub decision _(workspace scope)_.
3. Defects before features (the classification of Step 7).
4. Lowest number, then the registry order of the repo.

Zero unblocked candidates → stop and list what blocks each, including hub items that need a Product Owner decision.

## Step 6 — Present and confirm

Skipped in auto mode. Show the pick (repo, number, title, one-paragraph reasoning) and, in workspace scope, 1–2 runner-ups with one line each; ask for confirmation before doing anything.

## Step 7 — Hand off, publish, verify

Record the starting directory (to return to it in Step 8), then move into the picked repo. Classify the item: defect vocabulary in its title or description (bug, crash, error, regression, "doesn't work", "broken") → `vibe:fix`, otherwise `vibe:feature`.

- **Normal mode / forced pick**: invoke `vibe:feature NNN` or `vibe:fix NNN` with its normal human gates. Whatever it reports — done, plan rejected, early exit — continue: invoke `vibe:publish` so that everything committed locally, including a `wip:` commit, reaches the remote.
- **Auto mode**: the pick is handed to the build skill itself, never to `vibe:auto` — it ranks within one repo and knows nothing of the cross-repo blockers of Step 4, so it could start an item this skill holds back. Invoke `vibe:feature NNN --auto` or `vibe:fix NNN --auto` and read its `AUTO-RESULT:` line; without a usable line, the item under `done/` is `done`, `status: blocked` is `blocked`, anything else stops the run and is reported as an item left mid-way. `done` or `blocked` with items left under `N` → run Steps 2–5 again (the item just shipped may have unblocked others) and hand off the next pick, one at a time, moving into its repo; `aborted`, or nothing eligible → stop handing off. Then invoke `vibe:publish` in every repo that received a commit, one after the other.

Then, **workspace scope only**, re-check downstream: for every other active repo, any item or `CLAUDE.md` passage waiting on a repo or item shipped in this run. Apply the done-vs-published distinction — a version-phrased wait is resolved only if a tag was actually pushed; if nothing was released and a downstream item needs a published version, it is still blocked, say so. List newly unblocked items by repo, number, title.

## Step 8 — Report

Return to the starting directory (matters for chained `/loop` firings). Short, plain sentences: what was implemented (every item and verdict in auto mode); `vibe:publish`'s push, release, CI, and forge results; downstream items newly unblocked (workspace scope); any blocker needing the user before the next run. If `vibe:publish` reports a CI failure, lead the whole report with it, before anything else.
