---
type: llm
focus: last_message
criteria: |
  Read the whole final message, including the questions asked and the
  answers given during the interview, and the closing "### Synthesis"
  section.

  PASS only if the Synthesis section demonstrably folds in the specific
  answers given during the interview — e.g. it names the actual export
  format chosen, states plainly whether shared/Workspace content is in or
  out of scope, and states whether the export is synchronous or
  asynchronous — as concrete decisions about the feature.

  FAIL if the Synthesis is a generic restatement of "let users export their
  data" that could have been written before any question was asked, ignores
  one or more of the answers actually given, or invents an answer that
  contradicts what was actually decided in the interview.
weight: 2
---

The synthesis must be grounded in the actual answers given, not a
rewording of the original vague request.
