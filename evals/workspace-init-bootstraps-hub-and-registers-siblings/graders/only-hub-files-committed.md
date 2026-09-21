---
type: llm
focus: trace
criteria: |
  Look at every Bash tool call and its output across the run (git commands
  in particular).

  PASS only if both of these hold:
  - Some commit was made inside the `roadmap/` hub repo (working directory
    `roadmap` or a `git -C roadmap ...` / `git --git-dir=roadmap/.git ...`
    invocation) whose message is or starts with "chore: bootstrap hub repo",
    and that commit's changed files are confined to files under `roadmap/`
    (e.g. `repos.md`, `CLAUDE.md`, `README.md`, `.vibe/...`) — never the
    top-level `CLAUDE.md` sitting next to `roadmap/`.
  - No git command anywhere in the trace adds, stages, or commits the
    top-level `CLAUDE.md` (the workspace-root one, not `roadmap/CLAUDE.md`).
    This file is documented as local-only and must never be committed by
    this skill.

  FAIL if the top-level workspace-root `CLAUDE.md` is ever `git add`ed or
  appears among a commit's changed files, or if `roadmap/`'s own files were
  never committed at all.
weight: 2
---

`/vibe:workspace-init` commits the hub repo's own files (one
`chore: bootstrap hub repo` commit on first init) but never commits the
workspace-root `CLAUDE.md`, which is local-only convenience context for a
directory that isn't even a git repo.
