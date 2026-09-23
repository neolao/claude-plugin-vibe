---
status: todo
---
# Verify The Real Build Command, Not Just Tests, Before Shipping

## Description
`workflow.md`'s "Baseline check" runs the project's build step (if any) only once, as a pre-condition before planning, to detect pre-existing breakage. Nothing re-runs it afterward: "Green — implement" re-runs the test suite, "Refactor and lint" re-runs tests and the lint command, and `vibe:release`'s "Pre-release checks" run only the test and lint commands. A test runner that doesn't type-check (Vitest/Jest by default transpile TypeScript via esbuild/babel, discarding type errors rather than reporting them) will report green while the actual production build (`tsc && vite build`, `tsc --noEmit`, `cargo build`, …) fails.

This shipped a real type error to a deployed app: `character` org's `stage-viewer-web` repo had a test helper's parameter narrowed to `BGElement[]` where a call site legitimately passed `null` (the format's own nil-slice convention, handled correctly everywhere else). `npm test` and lint both passed at commit time; only `npm run build` — never re-run by any vibe skill after the baseline check — would have caught it. The bug shipped straight through `vibe:auto`/`vibe:next-task` and broke every subsequent CI deploy until a human noticed and fixed it directly (2026-09-23, cross-repo deploy incident write-up in the `kakutou` workspace's session history).

## Acceptance Criteria
- [ ] `workflow.md`'s "Refactor and lint" step re-runs the same build command the Baseline check detected (if any), not just tests and lint — a failing build here is treated exactly like a failing test (diagnose, fix the code, re-run; 3 attempts then escalate), before the task can reach Commit.
- [ ] `vibe:release`'s "Pre-release checks" (Step 2) run the build command too, not only test and lint — a release must never be cut on top of a build that doesn't actually compile.
- [ ] Both changes are worded generically ("the build command, if the project has one" — same phrasing already used by the Baseline check), not tied to any one language/toolchain.
- [ ] An eval (or an addition to an existing one, e.g. `feature-*`/`release-cuts-a-version`) exercises a project where tests pass but the build command fails, confirming the skill now blocks instead of shipping.

## Notes
Raised by a real cross-repo incident (character-viewer-web, character-editor, stage-viewer-web deploy failures, fixed manually 2026-09-23) — see also backlog item 009, the sibling gap that let these same failures go unnoticed for several pushes in a row once they reached CI.
