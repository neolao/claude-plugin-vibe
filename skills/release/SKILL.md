---
name: release
description: Create a versioned release — bump version, finalize CHANGELOG.md, commit and tag
argument-hint: <version, e.g. 1.2.0> | major | minor | patch
---

# /vibe:release — Release Workflow

Create a versioned release following Semantic Versioning.

## Step 1 — Determine version

**If `$ARGUMENTS` is a version number** (e.g. `1.2.0`): use it directly.

**If `$ARGUMENTS` is `major`, `minor`, or `patch`:**
- Run `git tag --sort=-version:refname | head -1` to find the latest tag
- Bump accordingly (semver rules)

**If no argument:**
- Read `CHANGELOG.md` [Unreleased] section
- Suggest: `patch` if only Fixed entries; `minor` if any Added; `major` if any Removed or breaking changes
- Present the suggestion and **wait for confirmation** before proceeding

## Step 1b — Create task list

Create the full task list using TaskCreate. **Keep subject names short (≤ 30 chars)** — they appear in the status line.

```
Run pre-release checks    ← no dependency
Finalize CHANGELOG.md     ← blockedBy "Run pre-release checks"
Refresh docs              ← blockedBy "Finalize CHANGELOG.md"
Bump version              ← blockedBy "Refresh docs"
Commit and tag            ← blockedBy "Bump version"
```

## Step 2 — Pre-release checks

Mark the `Run pre-release checks` task `in_progress`.

1. Run the test command (from manifest) — all tests must pass
2. Run the lint command (from manifest) — must exit 0
3. Check for uncommitted changes — if any exist, stop and warn the user

Mark the task `completed`.

## Step 3 — Finalize CHANGELOG.md

Mark the `Finalize CHANGELOG.md` task `in_progress`.

**Invoke the `vibe:changelog` skill** using the Skill tool (`skill: "vibe:changelog"`, `args: "[version]"`) — to move [Unreleased] entries into the new version section with today's date.

Mark the task `completed`.

## Step 3b — Refresh docs

Mark the `Refresh docs` task `in_progress`.

**Invoke the `vibe:docs` skill** using the Skill tool (`skill: "vibe:docs"`, `args: "--full"`) — full regeneration so the release ships with up-to-date documentation (notably the README features section now including the new version's entries).

If `README.md` has no `vibe:` managed section markers and no `docs/` directory exists: skip — this project does not use managed documentation.

Mark the task `completed`.

## Step 4 — Bump version in manifest

Mark the `Bump version` task `in_progress`.

Update the version field in the project manifest:

| File | Field |
|---|---|
| `package.json` | `"version": "X.Y.Z"` |
| `Cargo.toml` | `version = "X.Y.Z"` |
| `pyproject.toml` | `version = "X.Y.Z"` |
| `pom.xml` | `<version>X.Y.Z</version>` |
| `build.gradle` | `version = 'X.Y.Z'` |
| `composer.json` | `"version": "X.Y.Z"` |
| `Gemfile` / `*.gemspec` | `s.version = 'X.Y.Z'` |

Mark the task `completed`.

## Step 5 — Commit and tag

Mark the `Commit and tag` task `in_progress`.

1. Stage: `CHANGELOG.md` + manifest file(s) + `README.md` and `docs/` if Step 3b modified them
2. Commit: `chore: release vX.Y.Z`
3. Tag: `git tag vX.Y.Z`

Mark the task `completed`.

## Step 6 — Report

- Version released: `vX.Y.Z`
- Changes included: N Added, N Fixed, N Changed, etc.
- Tag created: `vX.Y.Z`
- **Do NOT push unless the user explicitly asks**
