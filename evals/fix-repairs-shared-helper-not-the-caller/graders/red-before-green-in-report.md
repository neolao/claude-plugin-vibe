---
type: regex
target: trace
pattern: "The report follows:[\\s\\S]{0,300}?## IMPLEMENTATION report[\\s\\S]{0,3000}?Commands run:\\*\\*[\\s\\S]{0,1500}?fail[\\s\\S]{0,1500}?pass"
flags: i
weight: 2
---

Red before green, read from the implementer's `## IMPLEMENTATION report` as
handed back to the workflow: its **Commands run** list shows the test command
failing before it passes. Anchored on the hand-back so the workflow's own
description of that report does not match. A regex, not an `llm` grader: the
trace of a full run is several hundred KB and the judge split on it.
