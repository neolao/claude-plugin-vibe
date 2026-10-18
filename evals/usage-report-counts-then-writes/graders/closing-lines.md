---
type: regex
target: last_message
pattern: "📊 Report —[^\\n]*\\.vibe/usage-reports/[^\\n]*feature\\.md[\\s\\S]*Local only\\. Share it with the plugin's maintainers if you want it to feed the evals\\."
weight: 1
---

The closing block is the skill's: the `📊 Report — <path>` line, then the
local-only sentence word for word. This is where the user learns the report
never leaves their machine unless they share it.
