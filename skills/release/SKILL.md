---
name: release
description: Create a versioned release — bump version, finalize CHANGELOG.md, commit and tag
argument-hint: "[version, e.g. 1.2.0 | major | minor | patch] (empty = suggest from the changelog and confirm)"
version: 1.1.0
model: claude-sonnet-5-5
---

# /vibe:release — Release Workflow

Create a versioned release following Semantic Versioning. Everything is local: this skill never pushes — `vibe:publish` (via `/vibe:auto --push` or `/vibe:next-task`) or the user does.

## Step 1 — Read the argument

The current version is the latest version tag: `git tag --list 'v[0-9]*' '[0-9]*' --sort=-version:refname | head -1` — the patterns matter, `--sort` alone puts a `deploy-…` or `vnext` tag first. A pre-release tag (`v1.3.0-rc.1`) sorts above its final version: skip it when `v1.3.0` is also tagged. No tag yet → the version the manifests carry (the highest when they disagree), or `0.0.0`.

- A version number (`1.2.0`, `1.3.0-rc.1`) → use it.
- `major` / `minor` / `patch` → bump the current version; a pre-release finalizes first (`patch` or `minor` on `1.3.0-rc.1` gives `1.3.0`, `major` gives `2.0.0`).
- No argument → the bump is suggested in Step 3, once the changelog is complete.

Then invoke the `vibe:tasks` skill with: `Run pre-release checks` → `Finalize CHANGELOG.md` → `Refresh docs` → `Bump version` → `Commit and tag`, each blocked by the previous one.

## Step 2 — Pre-release checks

Run the test command, the lint command, and the build command if the project has one. Stop and warn the user, without cutting the release, on any failure among these three or on an uncommitted change — a release is never cut on top of a build that doesn't actually compile.

## Step 3 — Finalize CHANGELOG.md

Invoke the `vibe:changelog` skill (no argument) so every commit since the last tag is reflected under `[Unreleased]` — before the version is chosen, so a bump suggested without an argument is judged on the complete section, not on the entries someone remembered to write. `[Unreleased]` still empty afterwards → nothing to release: stop and say so, whatever the argument (a change the changelog does not know of needs its entry first; the tree is as it was, the refresh wrote nothing).

No argument → suggest the bump, the first that applies: `major` if any `### Removed` entry or an entry marked breaking; `minor` if any `### Added`, `### Changed` or `### Deprecated` entry; `patch` otherwise (`### Fixed`, `### Security`) — the rule `vibe:publish` applies when it decides in the user's place; **wait for confirmation**.

Then cut the release: rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD`, insert a fresh empty `## [Unreleased]` above it, and add or update the links at the bottom in the form the file already uses: `[X.Y.Z]` compares the previous version tag to `vX.Y.Z` (`…/compare/vPREV...vX.Y.Z`; a first version has nothing to compare to and links its tag, `…/releases/tag/vX.Y.Z`), `[Unreleased]` compares `vX.Y.Z` to `HEAD`. The base URL is `git remote get-url origin`, rewritten as `https://host/owner/repo` when it is an SSH URL; no remote → no links.

## Step 4 — Refresh docs

If `README.md` has `vibe:` managed section markers or `docs/` exists: invoke the `vibe:docs` skill with `--full`, so the release ships with documentation that reflects the new version. Otherwise skip.

## Step 5 — Bump the version

Set the version field of every project manifest to `X.Y.Z` (`package.json`, `Cargo.toml`, `pyproject.toml`, `pom.xml`, `build.gradle`, `composer.json`, gemspec, …), using each file's own syntax.

## Step 6 — Commit and tag

Stage `CHANGELOG.md`, the manifests, and `README.md`/`docs/` if Step 4 changed them; commit `chore: release vX.Y.Z`; `git tag vX.Y.Z`.

## Step 7 — Report

Short, plain sentences: version released, changes included (N Added, N Fixed, …), tag created, and that nothing was pushed.
