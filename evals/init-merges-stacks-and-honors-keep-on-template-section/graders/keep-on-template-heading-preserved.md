---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "## Testing conventions <!-- keep -->\\n\\n- Unit tests live in `tests/`, one file per domain module\\.\\n- Payment tests live in `tests/integration/` and run against the payments sandbox only when `PAYMENTS_SANDBOX_KEY` is set\\. Never replace the sandbox with a mock in these tests: the 2025 refund outage passed a fully mocked suite\\."
flags: ""
match: contains
weight: 2
---

`## Testing conventions` is also a template section, but the hand-written
version carries `<!-- keep -->`: its heading and body survive byte-for-byte
instead of being replaced by the template's generated bullets.
