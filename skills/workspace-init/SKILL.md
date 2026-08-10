---
name: workspace-init
description: Initialize or refresh a generic hub repo (repos registry, cross-repo backlog/decisions) and the local, untracked workspace-root CLAUDE.md that indexes it and its sibling repos
argument-hint: "[hub repo dir name, e.g. roadmap] (only used on first bootstrap)"
---

# /vibe:workspace-init — Multi-Repo Workspace Bootstrap

Sets up (or refreshes) the plumbing for a **workspace**: a parent folder — never itself a Git repo — holding several sibling repos as independent checkouts. Introduces two things, neither tied to any particular forge or organization name:

- **hub repo** — a dedicated Git repo, with no application code, that plans across the other repos: a registry of siblings (`repos.md`), plus a workspace-scoped `.vibe/backlog/`+`.vibe/decisions/` for decisions that don't belong to any single repo. Recognized by a **structural marker**, not a fixed name: any directory with `.git/` and a `repos.md` at its root is the hub repo.
- **workspace-root `CLAUDE.md`** — a local, never-committed convenience file at the parent folder's root (it can't be committed — that folder isn't a repo). Points to the hub repo and lists sibling repos, so a fresh session immediately knows how the workspace is laid out.

Idempotent — re-run any time a repo is added, retired, or renamed.

## Step 1 — Determine mode from the cwd

- cwd has `.git/` **and** a `repos.md` at its root → already inside the hub repo → go to **Step 3**, treating cwd's parent as the workspace root for Step 9.
- cwd has `.git/` **without** `repos.md` → this is a code repo, the wrong place to run this skill. Stop and report: "Run `/vibe:workspace-init` from the workspace root (the parent folder, not inside a repo), or from the hub repo itself."
- cwd has no `.git/` → potentially the workspace root → go to **Step 2**.

## Step 2 — Locate or create the hub repo

Prefer a **pointer** over scanning: if a workspace-root `CLAUDE.md` already exists here (written by a previous run — see Step 9), read the directory name from its `## Hub repo` line and check it still has the marker (`.git/` + `repos.md`). Valid → use it, go to Step 3.

Only fall back to a full scan of cwd's direct subdirectories (marker `.git/` + `repos.md`) when there is no pointer to trust — the very first bootstrap, or a pointer whose target directory was renamed or deleted.

- **Marker found** (via pointer or scan) → continue with that directory as the hub repo, go to Step 3.
- **Not found** → use `AskUserQuestion` to collect:
  1. Directory name for the hub repo (pre-fill with `$ARGUMENTS` if given, otherwise suggest a neutral name such as "roadmap" — never impose it).
  2. Git remote (optional — can be added later).
  - If the directory doesn't exist: `mkdir` then `git init` (and `git remote add origin <url>` if a remote was given).
  - If the directory already exists without `.git/` (e.g. pre-created by hand): `git init` in place.

## Step 3 — Create task list

Invoke the `vibe:tasks` skill (Skill tool) to create the tasks below. **Keep subject names short (≤ 30 chars)** — they appear in the status line. `vibe:tasks` creates the tasks via `TaskCreate`, or falls back to a scratchpad checklist if that tool is unavailable — either way, its instructions then govern how every later "mark the task completed" instruction in this skill is carried out.

Pass as `$ARGUMENTS`:

```
Update repos registry        ← no dependency
Ensure .vibe/ scaffolding    ← blockedBy "Update repos registry"
Write hub repo CLAUDE.md     ← blockedBy "Ensure .vibe/ scaffolding"
Refresh hub repo README      ← blockedBy "Write hub repo CLAUDE.md"
Refresh workspace CLAUDE.md  ← blockedBy "Refresh hub repo README"
```

## Step 4 — Update `repos.md`

Mark `Update repos registry` `in_progress`.

Scan the siblings of the workspace root (every direct subdirectory with `.git/`, excluding the hub repo itself).

- **Already listed** in `repos.md` → keep its `status`/`role` exactly as-is. Never overwrite a human judgment call about a repo's status.
- **New sibling, not yet listed** → default `status: active` if it has a `.vibe/backlog/` (a clear sign it's a vibe-managed code repo); otherwise `AskUserQuestion` for `status` (`active`/`planned`/`idea`) and a one-line role. Never guess the role.
- **Listed but the directory is gone** → keep it in the report as a discrepancy; never remove it silently — ask for confirmation first.

Write/rewrite `repos.md` at the hub repo's root:

```markdown
# Repos registry

Maintained by /vibe:workspace-init — re-run after adding, retiring, or renaming a repo in the workspace.

| Repo | Status | Role | Remote |
|---|---|---|---|
| api | active | REST backend, owns the `orders` domain | git@github.com:acme/api.git |
| web | active | Next.js frontend | git@github.com:acme/web.git |
| sdk | planned | Shared TS client — not started | — |
| billing | idea | Captured for future planning, no repo yet | — |

## Naming convention
[free text describing this workspace's repo-naming pattern, if one exists — leave "None documented yet." otherwise]
```

`status`: `active` (a candidate for `/vibe:next-task`) / `planned` (no code yet, out of picking scope) / `idea` (not even a repo yet).

Mark the task `completed`.

## Step 5 — Ensure `.vibe/` scaffolding

Mark `Ensure .vibe/ scaffolding` `in_progress`.

Create `.vibe/backlog/` and `.vibe/decisions/` in the hub repo if absent. Never touch an existing item or ADR.

Mark the task `completed`.

## Step 6 — Write the hub repo's `CLAUDE.md`

Mark `Write hub repo CLAUDE.md` `in_progress`.

Written directly by this skill — do **not** delegate to `vibe:init`: its stack-detection/DoD/review-agents template assumes application code, which a hub repo never has.

```markdown
# CLAUDE.md — [hub repo name] (workspace hub — no code)

> Auto-generated by /vibe:workspace-init. Edit freely — re-run /vibe:workspace-init to refresh the registry/scaffolding.
> Add `<!-- keep -->` on a section heading to preserve it on regeneration.

## Role

This repo holds no application code. It is the source of truth for cross-repo planning across the workspace: [repos.md](repos.md) is the registry of every sibling repo (status, role, remote); `.vibe/backlog/` and `.vibe/decisions/` hold Product Owner decisions and ADRs that span more than one repo.

**Items here are never implementable work.** They are never picked up by `/vibe:feature`, `/vibe:fix`, or `/vibe:auto` — those operate inside a single code repo. Run `/vibe:next-task` from the workspace root to pick and ship actual work in the right repo.

## Backlog & decisions

Same format as any vibe-managed repo (`status: todo|in_progress|blocked|done` frontmatter on backlog items, `.vibe/decisions/NNN-slug.md` ADRs) — scoped here to workspace-level concerns: which repo owns what, cross-repo sequencing, naming conventions. `/vibe:backlog` works in this repo too. Managed by hand, not by an autonomous run.
```

Mark the task `completed`.

## Step 7 — Refresh the hub repo's README

Mark `Refresh hub repo README` `in_progress`.

**Invoke the `vibe:docs` skill** (Skill tool, `skill: "vibe:docs"`), no argument — its existing logic (skeleton if absent, managed sections otherwise) applies unchanged.

Mark the task `completed`.

## Step 8 — Sync `.vibe/` (best-effort)

**Invoke the `vibe:sync` skill** (Skill tool, `skill: "vibe:sync"`) so `.vibe/index.md`/`models.md`/`glossary.md` stay in the same shape as any other repo in the workspace. A hub repo has little or no source code to document — `vibe:sync` already treats "nothing to update" as a normal outcome, not an error; note it in the report rather than blocking on it.

## Step 9 — Refresh the workspace-root `CLAUDE.md`

Only meaningful when a workspace root exists one level above the hub repo (Step 1/2 established it, or is the hub repo's own parent when Step 1 started inside the hub repo). Full idempotent overwrite (with `<!-- keep -->` support), **never committed** — the workspace root isn't a Git repo, so nothing here is version-controlled; losing this file costs nothing, it regenerates from `repos.md`.

```markdown
# CLAUDE.md — [workspace name] (workspace root — not a git repo)

> Auto-generated by /vibe:workspace-init. This directory is not version-controlled: this file is local-only convenience context.
> Re-run /vibe:workspace-init here to refresh it. Add `<!-- keep -->` on a section heading to preserve it.

## Hub repo
`[hub-dir]/` — source of truth for cross-repo planning (`repos.md` registry, workspace-scope backlog/decisions in `.vibe/`). Start there for anything spanning more than one repo. Its own items are Product Owner decisions, never implementable — never route them through `vibe:feature`/`vibe:fix`/`vibe:auto`.

## Sibling repos
| Repo | Status | Role |
|---|---|---|
[mirrored from repos.md, active/planned/idea repos alike]

## Cross-repo workflow
Run `/vibe:next-task` from this directory to pick, implement, and ship the next eligible task across active repos.
```

The `## Hub repo` line is the pointer Step 2 (and `/vibe:next-task`) reads on later runs — keep its exact directory name in the backtick-quoted path.

## Step 10 — Commit and report

Mark `Refresh workspace CLAUDE.md` `completed`.

In the hub repo: if `repos.md`, `.vibe/`, `CLAUDE.md`, or `README.md` actually changed, stage and commit them in a single commit — `chore: bootstrap hub repo` on first-time init (Step 2 created it), `chore: refresh workspace registry` on a later run. No changes → nothing to commit, say so plainly. Never push automatically here (that's `/vibe:next-task`'s job, not this skill's).

Report, short and plain:
- Hub repo location (created / already existed).
- Repos added / updated / flagged as missing in `repos.md`.
- Files refreshed (hub `CLAUDE.md`, README, `.vibe/`, workspace-root `CLAUDE.md`).
- Commit hash and message, or "nothing to commit".
- Reminder: push the hub repo's commit whenever convenient (this skill never pushes).
