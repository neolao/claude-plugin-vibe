---
status: done
---
# vibe:publish Verifies The Actual CI Run After Pushing

## Description
`vibe:publish` treats a successful `git push` (and `git push --tags`) as the finish line: its Step 4 report covers push result, release result, and forge release, but never whether the CI workflow that push actually triggers (a deploy pipeline, a test matrix) succeeded. When a project's real gate — for example a GitHub Actions "Deploy to GitHub Pages" workflow — fails for a reason local checks can't see (an environment mismatch a screenshot-comparison suite is sensitive to, a secret/permission only present in CI, a matrix job local tooling doesn't run), nothing in the plugin ever notices. `vibe:auto`/`vibe:next-task` moved on to the next backlog item and kept publishing on top of it, three pushes in a row, before a human noticed (2026-09-23 cross-repo deploy incident; see backlog item 008 for the sibling gap that produced one of the three underlying bugs).

## Acceptance Criteria
- [ ] After Step 1 (push) and, if it ran, Step 2's `git push && git push --tags`, `vibe:publish` checks whether the repo has a CI/deploy workflow it can observe (e.g. `gh` available, authenticated, `origin` a `github.com` remote, at least one workflow file) — skip this whole step silently if not, same "best-effort, nothing depends on it" posture as today's forge-release step.
- [ ] When observable, poll the workflow run(s) triggered by the just-pushed commit(s) until each reaches a conclusion, with a bounded wait (long enough for a typical CI run, not indefinite) — report `⚠ CI still running after Ns — check <url>` rather than hanging forever.
- [ ] A failed run is surfaced as a first-class blocker in Step 4's result (name of the failing workflow, run URL, one-line reason if extractable from the log), not folded silently into "push succeeded."
- [ ] `vibe:auto`/`vibe:next-task`, when `vibe:publish` reports a CI failure, do not silently start the next backlog item on top of a broken deploy — the failure is surfaced in the same run's report, loud enough that a `/loop`-driven unattended run doesn't bury it under N more items.
- [ ] An eval covers: CI green (report says so, nothing changes), CI red (blocker surfaced, run stops or flags it), and no observable CI (silent skip, matching the forge-release precedent).

## Notes
Raised by a real cross-repo incident (character-viewer-web, character-editor, stage-viewer-web deploy failures ran unnoticed across several pushes each, fixed manually 2026-09-23). Deliberately scoped to *detecting and surfacing* a red run, not to fixing it — an automatic fix-and-retry loop here is a much larger, separately-worth-discussing decision (what counts as safe to retry, how many attempts, whether it should look anything like `vibe:release`'s existing one-shot self-heal in `vibe:publish` Step 2).
