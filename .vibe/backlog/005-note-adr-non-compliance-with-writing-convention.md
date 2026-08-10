---
status: todo
---
# Note ADR Non Compliance With Writing Convention

## Description
`.vibe/decisions/001` and `002` each have at least one field written as a dense, multi-fact sentence, which doesn't follow the short-plain-sentence convention `002` itself introduced. ADRs are append-only, so these two files can't be edited — the goal is to make sure new ones don't repeat this.

## Acceptance Criteria
- [ ] `skills/feature/SKILL.md`'s ADR-writing instructions are re-read and confirmed clear enough to prevent this in future ADRs (already state "one or two short, plain sentences per field" as of this review — verify it's sufficient, or reinforce it).
- [ ] No attempt is made to edit `001` or `002` in place.

## Notes
Raised by `/vibe:review` (review-architecture, Low). Informational — existing ADRs stay as written by design.
