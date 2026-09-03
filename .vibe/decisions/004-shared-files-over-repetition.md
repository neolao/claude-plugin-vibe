---
date: 2026-09-03
status: accepted
---
# Shared content lives in one file read at invocation, never repeated across prompts
**Context:** The plugin had doubled in size (18k → 38k words) by repeating every shared rule at each point of use, with 20 "kept identical — update both together" notes shipped inside runtime prompts. Copies had already diverged.
**Decision:** Anything two or more skills or agents need is written once and reached at runtime: the feature/fix implementation workflow in `skills/feature/workflow.md` (read by both SKILL.md), the review finding contract in `skills/review/SKILL.md` (injected into every agent prompt), push-and-release in the hidden `vibe:publish` skill. Maintainer-only notes never appear in a prompt.
**Reason:** A skill can read a neighbouring file and invoke another skill (the `vibe:tasks` pattern proved it), so the include mechanism ADR 002 assumed missing does exist. One copy cannot diverge; a prompt only carries text the executing agent needs.
**Rejected alternatives:** Keeping the copies aligned by hand with sync notes — already failing; merging feature and fix into one skill — their user-facing surfaces differ and the shared file gives the same result.
