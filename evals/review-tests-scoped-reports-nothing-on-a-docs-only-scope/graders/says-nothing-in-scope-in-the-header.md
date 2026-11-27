---
type: llm
focus: last_message
criteria: |
  The only file in scope is fixtures/README.md, a Markdown document.

  PASS if the report's `SUITE EXECUTED:` line (or the sentence that
  stands in for it) says the suite was NOT RUN because nothing in scope
  is code or a test — any wording that names the scope holding no code
  and no test passes.
  FAIL if the line reports a run with counts, or gives another reason
  (no runner, no tests found, missing runtime), or is absent.
weight: 1
---

Says why the suite was not run: the scope holds no code and no test.
