---
type: llm
focus: last_message
criteria: |
  The skill's own Step 7 requires: "Short, plain sentences; synthesize, never
  dump raw agent output" — and lists what the report must cover instead:
  agents run (and any activation-table row flipped), total findings and a
  per-severity breakdown, applied fixes (file + one line each, or "None"),
  remaining findings by severity, and test status after fixes.

  PASS if the final message reads as a synthesized report along those lines:
  findings from different agents are grouped/deduplicated/prioritized into
  prose or a structured summary, not concatenated one after another.

  FAIL if the message is (or is dominated by) a raw concatenation of each
  agent's own FILE/CATEGORY/SEVERITY/ISSUE/SUGGESTION blocks pasted back
  one after another with no grouping, deduplication, or prioritization across
  agents.
weight: 2
---

Checks that the orchestrator did its own job (Step 4's deduplicate-and-prioritize,
Step 7's synthesize-never-dump) rather than acting as a passthrough for whatever
the sub-agents returned.
