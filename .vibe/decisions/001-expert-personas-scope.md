---
date: 2026-07-24
status: accepted
---
# Expert personas: prescriptive consultants, scoped to domains without a review counterpart
**Context:** Adding specialized expert personas (sub-agents) consultable by `/vibe:feature` and `/vibe:fix` — at plan time (Step 2) and on demand during implementation — to inject domain requirements a Product Owner never states (UI states, HTTP semantics, CLI conventions…).
**Decision:** Experts *prescribe before* (requirements folded into the plan), reviewers *critique after* (existing code via `/vibe:review`) — that boundary is written into every `agents/expert-*.md`. The initial roster is limited to the 7 domains with **no** `review-*` counterpart: ui-ux, frontend-design, api-rest, cli-dx, data, linux, ops. Selection is per-task (matching the brief against agent descriptions, 3 experts max per run), with no per-project activation table in CLAUDE.md.
**Reason:** Four candidate personas (security, performance, QA, design patterns) would have shadowed an existing reviewer, creating near-duplicate expertise grids to keep in sync — exactly the cross-definition duplication `review-hygiene` hunts. Task-based selection makes a per-project table redundant: a project without UI never produces a task matching `expert-ui-ux`.
**Rejected alternatives:** (1) All 11 personas with strictly ex-ante angles — accepted content proximity deemed too costly to maintain; may be revisited if usage proves the need. (2) Inline guideline files loaded by the skills instead of sub-agents — cheaper but loses the independent perspective and the established `agents/` pattern. (3) A per-project activation table like the `review-*` one — redundant with per-task matching, added maintenance for no filtering gain.
