---
type: tool_used
tool: Write
min: 0
max: 0
weight: 1
---

List mode is read-only: no `Write` tool call should happen at all — in
particular, the skill must not "fix" 002's `depends_on` by itself.
