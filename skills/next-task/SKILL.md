---
name: next-task
description: Pick the next eligible backlog item — across every active repo in a workspace if one is detected, otherwise in the current repo — implement it, then push and release
argument-hint: "NNN [in <repo>] (force a specific item) | auto [N] (autonomous, for /loop) | (empty — pick with confirmation)"
---

# /vibe:next-task — Cross-Repo (and Mono-Repo) Task Runner

Picks the next eligible piece of work, hands it off to `/vibe:feature`/`/vibe:fix` (directly, or repeatedly with `--auto` in auto mode) to implement, then **pushes and releases** — the one place in this plugin where a skill pushes and publishes on its own. `/vibe:feature`/`/vibe:fix`/`/vibe:auto` deliberately never push; this skill exists specifically to close that gap.

Two scopes, chosen automatically (Step 2), never as an option to pick:
- **Workspace scope** — a hub repo (see `/vibe:workspace-init`) is detected: candidates come from every `active` repo in `repos.md`, cross-repo blockers and priorities are resolved, downstream unblocks are checked after publishing.
- **Mono-repo scope** — no workspace detected, but the current directory is itself a vibe-managed repo (`.vibe/backlog/` present): picks within this one repo only. This is what distinguishes it from `/vibe:auto` even here — `/vibe:auto` stops at the last local commit, this skill pushes and releases afterward.

Requires either scope to do anything useful — if neither is detected, it stops (Step 2).

**Only Step 10 talks to the user.** Every nested invocation in Steps 7–9 (`vibe:feature`, `vibe:fix`, `vibe:release`, and whatever those pull in — `vibe:changelog`, `vibe:docs`, `vibe:sync`) ends with its own report, and `vibe:feature`/`vibe:fix` end with an `AUTO-RESULT:` line on top of that. Both read like a finished, user-facing answer — they are not, here: they are this skill's intermediate data, produced mid-run and consumed by the *next* step. Getting one back is never a stopping point and never something to relay as-is: capture what it says and continue immediately, in the same turn, to whichever step comes next (Step 8 after Step 7, Step 8b/8c after 8a, Step 9 after 8, Step 10 after 9) — all the way to Step 10, the only step that produces this skill's actual final report.

## Step 1 — Parse `$ARGUMENTS`

- **Forced pick** — `NNN` alone (mono-repo scope), or `NNN in <repo>` (workspace scope): read that item directly. Found → skip straight to **Step 7 — Hand off**. Not found → report the miss and stop.
- **Auto mode** — starts with the literal word `auto`, optionally followed by an integer (`auto`, `auto 3`): run the normal picking (Steps 2–5) but skip confirmation (Step 6), and in Step 7 drive the feature/fix loop directly in the picked repo, bounded by that integer if given. Meant to be driven by `/loop`, e.g. `/loop 1h /vibe:next-task auto 1`.
- **Normal mode** — `$ARGUMENTS` empty: pick automatically (Steps 2–5), confirm (Step 6) before handing off (Step 7).

## Step 2 — Determine scope

Look for a workspace, cwd only (this skill is meant to run from the workspace root or from within a single repo — it does not search upward through parent directories):

1. Does cwd have a `CLAUDE.md` written by `/vibe:workspace-init` (a `## Hub repo` line)? Read the hub repo directory name from it, verify the marker (`.git/` + `repos.md`) still holds there.
2. If not, does any direct sibling of cwd carry the marker (`.git/` + `repos.md`) itself? (Handles a stale/missing workspace-root `CLAUDE.md`.)

- **Marker resolved (1 or 2) → workspace scope.** Read `repos.md` in the hub repo, keep only `status: active` entries as candidates. If `repos.md` looks stale (a listed repo directory is gone, or a sibling with `.vibe/backlog/` isn't listed at all): fall back to a direct filesystem scan (`.git/` + `.vibe/backlog/`, excluding the hub repo) to fill the gap for this run, and mention the staleness in the final report — this run isn't blocked on it, but `/vibe:workspace-init` should be re-run.
- **No marker anywhere, but cwd itself has `.vibe/backlog/` → mono-repo scope.** The current repo is the only candidate. Steps 4–5 (cross-repo blocker resolution and scoring) and the cross-repo part of Step 9 do not apply — go straight from Step 3 to Step 6 with this one repo, no alternatives to list.
- **Neither** → stop: "No workspace detected here (no hub repo, no `.vibe/backlog/` in the current directory). Run `/vibe:workspace-init` first if this should be a workspace root, or run this from inside a vibe-managed repo."

## Step 3 — Collect candidates

For each candidate repo (every active repo in workspace scope, or just the current one in mono-repo scope): list `.vibe/backlog/*.md` at the top level (not `done/`), read `status` and `depends_on`. Keep only `status: todo` items whose every `depends_on` entry is already `done` (same-repo dependencies only — `depends_on` never references another repo).

The hub repo itself is never a source of candidates — its items are workspace-level decisions, not implementable work (see `/vibe:workspace-init`'s hub `CLAUDE.md`).

## Step 4 — Resolve cross-repo blockers and priority signals _(workspace scope only)_

An item can be blocked or prioritized by something outside its own repo's `depends_on` — by design, `depends_on` only ever references items in the *same* repo. Cross-repo relationships live in **prose**, not frontmatter, deliberately (see "Cross-repo blocker phrasing" below). For each Step 3 candidate:

- Read its `## Notes`/`## Description` for a reference to another repo or an unresolved item — if unresolved, drop this candidate (still blocked).
- **`done` vs. published**: a reference can point at a backlog item's *status* ("once item 033 is done") or at a *version* ("once `sdk` publishes v0.3.0", "needs a tagged release"). These are not the same thing — an item-status reference is satisfied by `status: done` alone; a version-phrased reference is only satisfied once that repo actually has a matching Git tag pushed (checked here, and reused by Step 9).
- Check the hub repo's `.vibe/decisions/` for any explicit statement that this item unblocks other work or is a priority — note it, it feeds Step 5.
- Check every *other* candidate repo's backlog/`CLAUDE.md` for a reference to this item's repo+number as something it's waiting on — count these as "items this would unblock."

**Cross-repo blocker phrasing** — no machine-readable tag is introduced for this (deliberately: it would duplicate the prose as a second channel to keep in sync, and the done-vs-published distinction resists a simple fixed schema). Recommended, non-enforced phrasing for `## Notes`: name the repo plus either the item (`repo-name#NNN`) or the word "tag"/"release" plus the expected version — e.g. "Blocked on the `sdk` repo publishing an initial tagged release with X" or "Needs `api#012` done first."

## Step 5 — Score and pick _(workspace scope only — mono-repo scope picks the lowest-numbered Step 3 candidate directly)_

Rank the surviving candidates:
1. Highest count of "items this would unblock" (Step 4) wins.
2. Tie-break: explicitly flagged as a priority in a hub-repo decision.
3. Tie-break: lowest item number.

If there are zero unblocked candidates anywhere: stop and report that every open task is blocked, listing what's blocking them — including any hub-repo backlog item that needs a Product Owner decision first. Do not guess; surface the decision(s) needed instead.

## Step 6 — Present and confirm

Skipped entirely in auto mode — go straight to Step 7 with the Step 5 pick.

Show the pick (repo if workspace scope, item number, title, one-paragraph reasoning) and, in workspace scope, 1–2 runner-up alternatives with a one-line reason each was passed over. Ask the user to confirm before doing anything else — even with only one candidate, the reasoning should be visible before work starts.

## Step 7 — Hand off

On confirmation (normal mode), or immediately (auto mode / forced pick):

1. Record the absolute path of the starting directory (workspace root, or the single repo in mono-repo scope) — needed to return to it in Step 10 regardless of how deep the hand-off changes the working directory.
2. Move into the picked (or forced) repo's directory (no-op in mono-repo scope — already there).
3. **Auto mode**: run the auto-mode loop below.
4. **Normal mode / forced pick**: classify feature vs. fix from the item's title/description (bug/error/incorrect/crash/regression → fix; new capability → feature), then invoke `vibe:feature NNN` or `vibe:fix NNN` (Skill tool) — no `--auto` here, the confirmation already happened in Step 6 and each skill's own human-facing gates apply normally. Whatever the invoked skill reports when it finishes (a completed implementation, a rejected plan, an early exit) — that is not this skill's final answer either; carry it forward and continue straight to Step 8.

### Auto-mode loop

Don't delegate to `vibe:auto` — drive the loop directly, since it already knows exactly which repo to work in from Step 5, so blind delegation to another skill's own item-selection would throw that away. Bounded by the optional integer `N` from Step 1 (absent → no limit, drain this repo's eligible backlog, same semantics as a bare `/vibe:auto` call).

Each iteration:
1. Re-collect this repo's eligible items (`status: todo`, `depends_on` satisfied) — freshly, since the previous iteration may have changed the state.
2. No eligible item left → stop the loop (repo drained).
3. Rank them the same way `vibe:auto`'s Step 1 does, and take the top-ranked item; its classification (fix vs. feature) is already known from that ranking.
4. Invoke `vibe:feature NNN --auto` or `vibe:fix NNN --auto` (Skill tool) directly on that exact item — the `--auto` flag already exists on both skills (see their own "Autonomous mode (`--auto`)" section), nothing new to build here.
5. Read the `AUTO-RESULT:` line: `done`/`blocked` → continue the loop if the `N` budget allows; `aborted` → stop the loop immediately (global blocker, go to Step 8 with whatever was accomplished so far).
6. Loop ends when: `N` is reached, the backlog is drained, or an item came back `aborted`.

Status line: same glyph convention as `vibe:auto`'s own loop (see its Step 4/6) — `● NNN slug — feature|fix` before invoking an item, then `✓ NNN slug — shipped <hash>` or `⚠ NNN slug — blocked (<reason>)`/`aborted` once the `AUTO-RESULT:` line lands. One line per item, no restating.

Control returns here once the invoked skill(s) finish (report, `AUTO-RESULT:` line(s), or early exit) — **do not stop and relay that report as if it were this skill's own answer; the turn is not over.** Continue to Step 8 regardless of outcome, including `blocked`/`aborted`/a rejected or stopped normal-mode run. `vibe:feature`/`vibe:fix` only ever commit **locally** by their own documented design; anything that landed there — including a `wip:` commit from their own "never end a turn with uncommitted files" rule — still needs to reach the remote.

## Step 8 — Push and publish

Still inside the picked repo's directory. Same one-line-per-transition convention as Step 7: `✓ pushed` / `⚠ push failed — <reason>` for 8a, `✓ vX.Y.Z tagged, pushed` / `⚠ release skipped — <reason>` for 8b.

### 8a — Push commits

1. `git status` / `git log @{u}..` — no local commit ahead of the remote (or no upstream configured) → skip to 8b.
2. `git push` (`git push -u origin <branch>` if no upstream yet).
3. Push rejected or fails (diverged history, no remote, auth failure, …) → **stop here**, do not attempt 8b. Report the exact Git error as a blocker for the user to resolve — never force through.

### 8b — Release, if the changelog warrants it

Everything from here through Step 9 runs unattended in **both** normal and auto mode — once Step 7 returned control, there is no more human confirmation anywhere in this skill, including inside the nested `vibe:release`/`vibe:changelog`/`vibe:docs` calls.

Read the repo's `CHANGELOG.md` `## [Unreleased]` section.

- Empty or missing → nothing to release, go to Step 9.
- Non-empty → compute the semver bump the same way `vibe:release` itself suggests, but decide it here rather than waiting on a human: `patch` if only `### Fixed` entries, `minor` if any `### Added`, `major` if any `### Removed` or an entry flagged as breaking.
- Invoke `vibe:release` (Skill tool) with that word (`patch`/`minor`/`major`) as `$ARGUMENTS` — **always with an explicit bump**, never blank, since a blank argument makes `vibe:release` wait for confirmation that would never come here.

If `vibe:release`'s own pre-release checks fail, it stops on its own before committing anything. What happens next depends on why:
- **Dirty tree that isn't ours, or the lint command fails**: report the failure and move on — the 8a push already succeeded, only the version bump is missing; flag it as a follow-up blocker in the Step 10 report.
- **The test command fails**: see "Self-heal a pre-existing test failure" below.

#### Self-heal a pre-existing test failure

Bounded to a single attempt, before giving up:
1. Identify the failing test file(s) from the output already visible in this context (produced while following `vibe:release`'s own Step 2).
2. Search this repo's eligible backlog (`status: todo`, `depends_on` satisfied, top-level `.vibe/backlog/`, never `done/`) for an item whose Description/Notes names that exact test file — the trace left by `vibe:feature`/`vibe:fix`'s own autonomous-mode convention of filing a backlog item for a pre-existing, out-of-scope failure discovered mid-run rather than silently fixing it.
3. **Exactly one match**: classify it (same rule as Step 7's auto-mode ranking) and run it right now via `vibe:fix NNN --auto` (or `vibe:feature NNN --auto`), in this same repo directory. Push whatever it commits (repeat 8a). Retry `vibe:release` once, same bump level (no need to recompute it: an added `### Fixed` entry alongside an existing `### Added` one doesn't change a `minor` bump).
4. **Zero matches, more than one match, or the retried release still fails**: this isn't (or wasn't) the recoverable case — give up, report the failure, flag it as a follow-up blocker in the Step 10 report. Never attempt a second self-heal in the same run.

On success (first attempt, or after the one self-heal retry above), `vibe:release` commits and tags **locally only** by its own design. Push both right away: `git push && git push --tags`.

### 8c — Release on the forge (best-effort, GitHub only)

If a version was tagged in 8b, `gh` is available and authenticated, and `git remote get-url origin` resolves to a `github.com` remote: create a GitHub Release from the pushed tag (`gh release create vX.Y.Z --notes-from-tag`). Best-effort visibility only — nothing else in this pipeline depends on the release object existing, only on the pushed tag. Missing/unauthenticated `gh`, or a non-GitHub remote (GitLab, Gitea, …): skip silently and say so in the report — not covered yet.

## Step 9 — Verify downstream is actually unblocked _(workspace scope only)_

Re-run a narrow version of Step 4's scan, scoped to the repo just pushed/released:

1. For every other active repo, re-check any backlog item or `CLAUDE.md` passage naming this repo (or this item's number) as something it's waiting on.
2. Apply the done-vs-published distinction from Step 4: a version-phrased reference is only resolved once Step 8b actually tagged **and** 8a/8b pushed it — confirm with `git ls-remote --tags <remote>` rather than assuming. An item/status-phrased reference is resolved once that item is `done`, release or not.
3. If 8b was skipped (nothing in `[Unreleased]`) but some downstream item specifically needs a published version: it is **still blocked** — say so, don't report it resolved just because local code shipped.
4. List any newly-unblocked cross-repo item(s) by repo, number, title. In auto mode this is what the next `/loop` firing will act on automatically.

## Step 10 — Final report

Return to the directory recorded in Step 7 before reporting (important for chained `/loop N /vibe:next-task auto 1` firings). Short, plain sentences — no filler:

- What was implemented — in auto mode, every item the Step 7 loop processed (number, type, verdict, commit), not just the first; in normal/forced mode, the single item's report / `AUTO-RESULT:`.
- Push result: branch pushed (commit range), or the exact reason it wasn't.
- Release result: version tagged and pushed, "no release needed" (empty changelog), or why a due release was skipped. If Step 8b's self-heal ran, say so explicitly: which item was forced, which test file it was matched against, and whether the retried release then succeeded or still failed.
- Forge release: created, skipped (no `gh` / non-GitHub remote), or not applicable.
- Downstream (workspace scope only): any newly-unblocked cross-repo item(s), or confirmation nothing else was waiting.
- Any unresolved blocker from 8a/8b/9 needing the user's attention before the next run can make further progress — call these out plainly.
