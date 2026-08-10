---
status: todo
---
# Fix Naming Issues In Demo Site Script

## Description
The showcase website's inline script (`docs/index.html`) has a few unclear names: a single-letter constant `P` for the prompt HTML snippet, single-letter keys `t`/`d` in the demo-step data, an abbreviation `gen` for a timer-cancellation token, and two same-named `IntersectionObserver` instances (`ro`, `io`) for different purposes.

## Acceptance Criteria
- [ ] `P` is renamed to a self-descriptive constant name (e.g. `PROMPT_HTML`).
- [ ] The `t`/`d` keys in the `DEMOS` step objects are renamed to `type`/`delayMs`.
- [ ] `gen` is renamed to reflect its role as a cancellation token (e.g. `runToken`).
- [ ] The two `IntersectionObserver` instances are renamed to reflect their distinct purposes (e.g. `revealObserver`, `playbackObserver`).
- [ ] The site still renders and the terminal demos still play correctly after the rename.

## Notes
Raised by `/vibe:review` (review-naming, Low). `docs/index.html` is off-limits to `/vibe:docs` — handle this file directly, per `CLAUDE.md`'s "Site GitHub Pages" section.
