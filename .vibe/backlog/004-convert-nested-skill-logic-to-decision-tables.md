---
status: todo
---
# Convert Nested Skill Logic To Decision Tables

## Description
A few skill steps express a state machine as nested prose bullets instead of a table: `auto`'s resume logic (Step 0), `sync`'s glossary step (Step 7), and `workspace-init`'s repo-location logic (Steps 1-2). A short lookup table would be easier to follow than the nested bullets.

## Acceptance Criteria
- [ ] `skills/auto/SKILL.md` Step 0 expresses its resume-state resolution as a table (state → outcome → action).
- [ ] `skills/sync/SKILL.md` Step 7 separates its exclusion rules, lifecycle rules, and legacy migration into distinct, non-competing blocks.
- [ ] `skills/workspace-init/SKILL.md` Steps 1-2 use a table if a third fallback case is ever added (no change required otherwise, per the review agent's own note).
- [ ] No behavior change — same decisions, same outcomes, just easier to read.

## Notes
Raised by `/vibe:review` (review-complexity, Low — readability only). Low priority, do when convenient.
