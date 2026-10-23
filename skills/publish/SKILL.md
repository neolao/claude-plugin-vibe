---
name: publish
description: Pushes the current repo's commits, cuts a release when the changelog warrants one, pushes the tag, verifies the pushed commit's CI run, and creates a forge release when possible. Invoked internally by vibe:auto (--push) and vibe:next-task — the only place in the plugin that pushes.
argument-hint: "(no arguments — operates on the current repo)"
user-invocable: false
version: 1.1.0
model: claude-sonnet-5-5
---

# vibe:publish — Push and Release

Runs unattended, in the current repo, after work has been committed locally. Nothing here asks the user anything, and neither does a skill invoked from here: when a nested skill reaches a point where it would ask, answer in its place and go on in the same turn — the turn never ends on a question. `vibe:release` never asks, its bump is explicit (Step 2); `vibe:docs`, which `vibe:release` runs when `docs/` exists, asks which sections to manage on a README without `vibe:` markers — the answer is none: the README stays as it is, `docs/` is still refreshed. Any other question gets the option that changes nothing beyond what the step already does. Every answer given this way is listed in Step 5. Print one status line per transition: `✓ pushed` / `✓ nothing to push` / `⚠ push failed — <reason>`, `✓ vX.Y.Z tagged, pushed` / `⚠ release skipped — <reason>`, `✓ CI green` / `⚠ CI still running after 600s — check <URL>` / `⚠ CI failed — <workflow> — <URL>`, `✓ GitHub release created`.

## Step 1 — Push commits

If `git log @{u}..` shows local commits ahead of the remote (or no upstream is configured): `git push` (`git push -u origin <branch>` if no upstream). Nothing ahead: `✓ nothing to push`, go to Step 2. A rejected or failing push (diverged history, no remote, auth failure) **stops this skill**: report the exact Git error as a blocker for the user, never force.

## Step 2 — Release when the changelog warrants it

Read `## [Unreleased]` in `CHANGELOG.md`. Empty or missing → nothing to release, go to Step 3 (a plain push can still trigger CI on its own, with no release involved).

Otherwise decide the bump without asking, the first that applies: `major` if any `### Removed` entry or an entry marked breaking; `minor` if any `### Added`, `### Changed` or `### Deprecated` entry; `patch` otherwise (`### Fixed`, `### Security`). Invoke the `vibe:release` skill with that word as its argument — always explicit, never blank.

If its pre-release checks fail:
- lint failure, or an uncommitted change (the caller commits before invoking this skill, which never leaves one itself) → report it and move on; the push already succeeded, only the version is missing.
- test failure → **one** self-heal attempt: if exactly one eligible backlog item (`status: todo`, dependencies done, top-level `.vibe/backlog/`) names the failing test file, run it now (`vibe:fix NNN --auto`, or `vibe:feature NNN --auto` if it is not a defect — `--auto` either way, no one is there to approve a plan), repeat Step 1, and retry `vibe:release` once with the bump decided again from the updated `[Unreleased]`. Zero or several matches, or a second failure → report it as a blocker.

On success `vibe:release` has committed and tagged locally: `git push && git push origin vX.Y.Z` — the one tag it created, never `--tags`, which would also push every stale local tag. A rejected push here stops this skill like Step 1's: report the exact Git error, say the release (commit and tag) exists only locally, never force.

## Step 3 — Verify CI (best-effort, GitHub only)

If `gh` is not available or not authenticated, `origin` is not a `github.com` remote, or the repo has no workflow file (`.github/workflows/*.yml`): skip silently, same posture as Step 4 — nothing depends on it, report "not observable".

Otherwise find the workflow run(s) the just-pushed commit triggered (the tag commit if Step 2 released, the branch commit otherwise). A run can take a little while to appear after the push: keep checking for up to two minutes rather than concluding "no CI" from an empty result in the first moment. Still none after that: no workflow's trigger covers this push (another branch, pull requests only, tags only, manual dispatch) — not observable, move on, nothing to poll.

Poll every triggered run until each reaches a conclusion, bounded to 10 minutes total. Still running past that bound: `⚠ CI still running after 600s — check <run URL>` and move on — never hang indefinitely.

A run that concludes failed or cancelled is a first-class blocker for Step 5: name the workflow, the run URL, and a one-line reason if one is extractable from the log. Every run green: `✓ CI green`, nothing more to say.

## Step 4 — Forge release (best-effort, GitHub only)

If a version was tagged, `gh` is available and authenticated, and `origin` is a `github.com` remote: `gh release create vX.Y.Z --title vX.Y.Z --notes-file <file>` where the file holds the `## [X.Y.Z]` section of `CHANGELOG.md` (its entries, without the heading) — not `--notes-from-tag`: the tag `vibe:release` creates is lightweight and carries no message. Otherwise skip and say so — nothing depends on it.

## Step 5 — Result

Return, for the caller's report: push result (branch and commit range, nothing to push, or the exact reason it failed); release result (version tagged and pushed, "no release needed", or why it was skipped, naming the self-heal item and its outcome if one ran); CI result (green, still running past the bound with its URL, failed with workflow/URL/reason, or not observable); forge release (created, skipped, not applicable); each answer given in a nested skill's place, if any; any blocker needing the user's attention — **a CI failure is such a blocker and the caller must lead its report with it**, not fold it into the push/release summary.
