---
name: changelog
description: Update CHANGELOG.md (Keep a Changelog format) from git history since the last tag — entries land under [Unreleased]; cutting a version is /vibe:release's job
argument-hint: "(no arguments)"
version: 1.1.0
model: claude-sonnet-5-5
---

# /vibe:changelog — CHANGELOG.md Updater

Bring `## [Unreleased]` in `CHANGELOG.md` up to date with the git history ([Keep a Changelog](https://keepachangelog.com/en/1.1.0/)). Never create a version section.

## Step 1 — Read the current state

`CHANGELOG.md` if it exists (current `[Unreleased]` entries); the latest tag (`git tag --sort=-version:refname | head -1`); the commits since it (`git log <tag>..HEAD --oneline --no-merges`, or the whole history when there is no tag).

## Step 2 — Classify the commits

| Commit pattern | Category |
|---|---|
| `feat:`, `add`, `new`, `implement` | Added |
| `refactor:`, `update`, `change`, `improve`, `migrate` | Changed |
| `deprecate` | Deprecated |
| `remove`, `drop`, `delete` | Removed |
| `fix:`, `bug`, `patch`, `correct`, `repair` | Fixed |
| `security`, `vuln`, `cve` | Security |

- The type prefix decides when there is one (`fix: remove stale sessions` is a fix, `chore(ci): fix flaky cache` housekeeping); the bare keywords classify messages without a prefix. A message that matches nothing (`Monday changes`) is classified from its diff (`git show <sha>`).
- Write each entry as its user-facing impact, not the commit wording: no function, file or other internal name, not even in backticks — a command, flag, endpoint or setting the user types may be named.
- **Skip a commit an existing `[Unreleased]` entry already covers** (`/vibe:feature` and `/vibe:fix` write theirs at implementation time).
- A revert cancels its target: when the reverted commit is in the range, drop both and remove the `[Unreleased]` entry written for it, if any; when the target was released, the revert is the change — Removed for a feature taken back, Fixed for a regression undone.
- Discard noise: merges, version bumps, `chore:` housekeeping unless significant, `wip:` partial work (the finished change arrives in a later `feat:`/`fix:` commit with its own entry), and any commit with no user-visible effect whatever its prefix — a refactor that changes nothing observable, tests, CI, formatting, dependency bumps, a documentation typo.

## Step 3 — Write

Add the new entries under `## [Unreleased]`, grouped by category; leave versioned sections untouched. No file yet: create it with the Keep a Changelog header.

## Step 4 — Report

Short, plain sentences: commits processed, kept vs discarded, categories populated. Don't print the file unless asked.
