---
name: changelog
description: Update CHANGELOG.md (Keep a Changelog format) from git history since the last tag — entries land under [Unreleased]; cutting a version is /vibe:release's job
argument-hint: "(no arguments)"
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
| `security`, `vuln`, `cve`, `auth` | Security |

- Write each entry as its user-facing impact, not the commit wording.
- **Skip a commit an existing `[Unreleased]` entry already covers** (`/vibe:feature` and `/vibe:fix` write theirs at implementation time).
- Discard noise: merges, version bumps, `chore:` housekeeping unless significant.

## Step 3 — Write

Add the new entries under `## [Unreleased]`, grouped by category; leave versioned sections untouched. No file yet: create it with the Keep a Changelog header.

## Step 4 — Report

Short, plain sentences: commits processed, kept vs discarded, categories populated. Don't print the file unless asked.
