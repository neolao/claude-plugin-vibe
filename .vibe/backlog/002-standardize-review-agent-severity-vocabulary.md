---
status: todo
---
# Standardize Review Agent Severity Vocabulary

## Description
Each `review-*` agent uses its own severity words (some `critical`/`high`/`medium`/`low`, others `warning`/`problem`). `/vibe:review`'s Step 4 has to hard-code a translation table to normalize them into High/Medium/Low. One shared vocabulary would remove the need for that table.

## Acceptance Criteria
- [ ] Every `agents/review-*.md` emits severity using the same fixed set of words.
- [ ] `/vibe:review`'s Step 4 translation table is removed or reduced to a no-op mapping.
- [ ] Existing review reports still show High/Medium/Low as before.

## Notes
Raised by `/vibe:review` (review-antipatterns, Medium). Touches 17 agent files — plan and apply carefully, one pass.
