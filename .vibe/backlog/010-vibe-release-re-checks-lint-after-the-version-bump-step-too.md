---
status: todo
---
# vibe:release Re-Checks Lint After The Version-Bump Step Too

## Description
Item 008's fix moved `vibe:release`'s build/lint/test check to Step 2 ("Pre-release checks"), which runs *before* Step 5 ("Bump the version"). That leaves a gap Step 2 cannot see: Step 5 itself can introduce a fresh lint/format violation, and nothing re-checks between Step 5 and Step 6 ("Commit and tag").

This is exactly what happened the day both items 008 and 009 shipped: `web-ui-kit`'s `chore: release v0.14.0` ran `npm version`, which rewrote the whole of `package.json` using npm's own JSON serializer — reformatting an unrelated `"files": ["dist"]` array from one line to three, violating Biome's format rules. Step 2's checks had already passed cleanly before this happened. The release was tagged and pushed anyway; only item 009's new CI-verification step (Step 3 of `vibe:publish`) caught it, after the fact, as a failed GitHub Actions run — one release (v0.14.0) had to be immediately superseded by a fix commit and a second release (v0.14.1). Item 009 worked exactly as designed and caught this fast (single failed run, fixed within the hour) — but a same-turn re-check would have avoided cutting the broken release at all.

## Acceptance Criteria
- [ ] `vibe:release` re-runs the lint command (and the build command, if the project has one) immediately after Step 5, before Step 6 commits and tags — a failure here blocks the release the same way a Step 2 failure does (report, stop, don't commit/tag), rather than shipping and relying on Step 3's CI check to catch it after the fact.
- [ ] If the re-check fails specifically because of the version-bump edit itself (a manifest reformatted in a way that violates the project's own lint/format rules — the exact `npm version` case above), the skill runs the project's own formatter/lint-fix command (if one exists, e.g. `biome check --write`, `prettier --write`) on the affected file(s) and re-checks once before giving up and reporting a blocker.
- [ ] An eval covers: the version-bump step introducing a format violation → caught and auto-fixed before commit, release proceeds; a violation the auto-fix command can't resolve → release blocked, nothing committed or tagged.

## Notes
Raised by a real incident in `web-ui-kit` (`chore: release v0.14.0` / `v0.14.1`, 2026-09-23, ~08:36-16:16 the same day items 008 and 009 were closed) — a residual gap in item 008's own fix, found by re-auditing CI status shortly after both items shipped. See items 008 and 009 for the earlier parts of this same investigation.
