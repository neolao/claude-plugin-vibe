---
type: regex
target: last_message
pattern: "## REVIEW agents[\\s\\S]*## REVIEW flipped rows[\\s\\S]*## REVIEW findings"
weight: 2
---

Step 4's contract: three headings, in order, parsed by the build workflow.
The findings come back verbatim in the agents' FILE/CATEGORY/SEVERITY format,
each preceded by `AGENT:`, with no synthesis.
