---
type: llm
focus: trace
criteria: |
  Look at every Bash tool call and its output (git commands in particular).

  PASS only if some commit was made inside the `roadmap/` repo (cwd `roadmap`
  or `git -C roadmap ...`) whose subject line (the first
  line of the message, including one written through a heredoc or `-m`) is
  "chore: refresh workspace registry", and no commit anywhere has a message
  starting with "chore: bootstrap hub repo".

  FAIL if no such refresh commit was made, or if a bootstrap commit was made,
  or if a new hub directory was created next to `roadmap/`.
weight: 2
---

On an existing hub, the commit is the refresh one, never the first-bootstrap
one, and no second hub is created.
