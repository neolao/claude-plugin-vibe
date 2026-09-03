---
name: release
description: Create a versioned release — bump version, finalize CHANGELOG.md, commit and tag
argument-hint: "[version, e.g. 1.2.0 | major | minor | patch] (empty = suggest from the changelog and confirm)"
---

# /vibe:release — Release Workflow

Create a versioned release following Semantic Versioning. Everything is local: this skill never pushes — `vibe:publish` (via `/vibe:auto --push` or `/vibe:next-task`) or the user does.

## Step 1 — Determine the version

- A version number (`1.2.0`) → use it.
- `major` / `minor` / `patch` → bump the latest tag (`git tag --sort=-version:refname | head -1`).
- No argument → read `## [Unreleased]` in `CHANGELOG.md` and suggest `patch` if only Fixed entries, `minor` if any Added, `major` if any Removed or breaking change; **wait for confirmation**.

Then invoke the `vibe:tasks` skill with: `Run pre-release checks` → `Finalize CHANGELOG.md` → `Refresh docs` → `Bump version` → `Commit and tag`, each blocked by the previous one.

## Step 2 — Pre-release checks

Run the test command (all tests pass) and the lint command (exit 0); stop on an uncommitted change and warn the user.

## Step 3 — Finalize CHANGELOG.md

Invoke the `vibe:changelog` skill (no argument) so every commit since the last tag is reflected under `[Unreleased]`. Then cut the release: rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD`, insert a fresh empty `## [Unreleased]` above it, and add or update the compare links at the bottom (`git remote get-url origin` for the base URL).

## Step 4 — Refresh docs

If `README.md` has `vibe:` managed section markers or `docs/` exists: invoke the `vibe:docs` skill with `--full`, so the release ships with documentation that reflects the new version. Otherwise skip.

## Step 5 — Bump the version

Set the version field of every project manifest to `X.Y.Z` (`package.json`, `Cargo.toml`, `pyproject.toml`, `pom.xml`, `build.gradle`, `composer.json`, gemspec, …), using each file's own syntax.

## Step 6 — Commit and tag

Stage `CHANGELOG.md`, the manifests, and `README.md`/`docs/` if Step 4 changed them; commit `chore: release vX.Y.Z`; `git tag vX.Y.Z`.

## Step 7 — Report

Short, plain sentences: version released, changes included (N Added, N Fixed, …), tag created, and that nothing was pushed.
