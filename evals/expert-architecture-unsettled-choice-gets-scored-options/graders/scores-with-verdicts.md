---
type: regex
target: last_message
pattern: "\\b(BETTER|TIE|WORSE)\\b[^\\n]{0,40}\\d+[^\\n\\d]{1,12}\\d+"
weight: 1
---

At least one alternative carries the mandatory verdict against the baseline
(`BETTER`, `TIE` or `WORSE`) followed by the count of criteria won and lost
(`BETTER (3/1)`, `TIE (2 won / 2 lost)`), as the agent's definition requires
for every option — a one-line reply has none.
