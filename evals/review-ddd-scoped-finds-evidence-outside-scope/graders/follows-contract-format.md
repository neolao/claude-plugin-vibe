---
type: regex
target: last_message
pattern: "FILE[*_]*:.*\\n?.*CATEGORY[*_]*:.*\\n?.*SEVERITY[*_]*:[\\s*_]*(high|medium|low)"
flags: is
weight: 1
---

At least one finding follows the FILE/CATEGORY/SEVERITY/ISSUE/SUGGESTION contract
instead of free-form prose.

Markdown emphasis around a label or value (`**SEVERITY:** medium`) still
matches: `/vibe:review` reads agent output as an LLM, not with a parser, so
bold labels work in production.
