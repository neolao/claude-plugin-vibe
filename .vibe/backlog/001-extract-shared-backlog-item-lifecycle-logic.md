---
status: todo
---
# Extract Shared Backlog Item Lifecycle Logic

## Description
Several skills (`feature`, `fix`, `backlog`, `auto`, `next-task`) each reimplement their own logic to resolve a backlog reference and to read/write an item's `status` field. There is no single shared routine owning these operations, so a future change risks updating one copy and missing another.

## Acceptance Criteria
- [ ] One shared internal skill (or equivalent single definition) resolves a backlog reference (`NNN`/`NNN-slug`) to its file path.
- [ ] The same shared definition owns backlog `status` transitions (`todo` → `in_progress` → `done`/`blocked`).
- [ ] `feature`, `fix`, `backlog`, `auto`, and `next-task` all call this shared definition instead of their own copy.
- [ ] No behavior change for any existing command — same inputs produce the same outputs as before.

## Notes
Raised by `/vibe:review` (review-antipatterns + review-hygiene, Medium). Architectural change — plan it as a dedicated feature rather than a quick edit.
