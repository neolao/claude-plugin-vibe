---
type: regex
target: last_message
pattern: "PACKAGE[*_]*:.*\\n?.*CATEGORY[*_]*:.*\\n?.*SEVERITY[*_]*:[\\s*_]*(high|medium|low)"
flags: is
weight: 1
---

At least one finding follows this agent's own contract override —
`PACKAGE: name@version (manifest)` in place of `FILE:`, followed by
CATEGORY/SEVERITY/ISSUE/SUGGESTION — instead of free-form prose or the
generic `FILE:` form.

Markdown emphasis around a label or value (`**SEVERITY:** medium`) still
matches: `/vibe:review` reads agent output as an LLM, not with a parser, so
bold labels work in production.
