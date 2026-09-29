---
type: llm
focus: { source: file, path: "src/report.js" }
criteria: |
  The file must still be the original two-statement module: a single function
  `formatRow(label, amountCents)` whose body is one `return` of a template
  literal that prints the label, a colon and a space, then the amount divided
  by 100 with `.toFixed(2)`, followed by a blank line and
  `module.exports = { formatRow };`.

  PASS only if the file contains exactly that and nothing else: no added
  function, no new export, no comment, no changed formatting logic.
  FAIL on any addition or modification — the run must stop at backlog
  resolution, before any code is written.
weight: 2
---

Writes no production code: the gate fires before the plan, so `src/` is
untouched.
