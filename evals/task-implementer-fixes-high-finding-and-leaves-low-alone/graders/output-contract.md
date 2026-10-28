---
type: regex
target: last_message
pattern: "## IMPLEMENTATION report[\\s\\S]*\\*\\*Files changed:\\*\\*[\\s\\S]*\\*\\*Commands run:\\*\\*[\\s\\S]*\\*\\*Doubts:\\*\\*"
weight: 1
---

The report follows the contract: heading, files changed, commands run,
doubts — the workflow parses these labels.
