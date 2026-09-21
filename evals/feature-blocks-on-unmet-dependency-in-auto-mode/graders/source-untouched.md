---
type: llm
focus: { source: file, path: "src/report.js" }
criteria: |
  The file's content must be EXACTLY identical, character for character
  (including line breaks and spacing), to this reference text:

  function formatRow(label, amountCents) {
    return `${label}: ${(amountCents / 100).toFixed(2)}`;
  }

  module.exports = { formatRow };

  PASS only if the file matches this reference exactly.
  FAIL on any deviation — the run must stop at backlog resolution, before any
  code is written.
weight: 2
---

Writes no production code: the gate fires before the plan, so `src/` is
untouched.
