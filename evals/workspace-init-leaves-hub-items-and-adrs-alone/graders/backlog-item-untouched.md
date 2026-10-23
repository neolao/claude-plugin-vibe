---
type: regex
target:
  source: file
  path: roadmap/.vibe/backlog/001-decide-error-envelope.md
pattern: "^---\\nstatus: todo\\n---\\n# Decide the error envelope shared by every repo\\n\\n## Description\\nThe API and the storefront disagree on how an error is shaped\\. One envelope, owned by the API, used by all\\.\\n\\n## Acceptance Criteria\\n- \\[ \\] The envelope is written down in an ADR of this hub\\n- \\[ \\] Every active repo links to it from its CLAUDE\\.md\\n\\n## Notes\\nProduct Owner decision — not implementable work\\.\\n$"
flags: ""
match: contains
weight: 2
---

The hub's existing backlog item is byte for byte what the fixture
wrote: the refresh touches no item.
