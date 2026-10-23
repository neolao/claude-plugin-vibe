---
type: llm
focus: trace
criteria: |
  Look at every Bash tool call and its output (git commands in particular).

  PASS only if some commit was made inside the `roadmap/` repo (cwd
  `roadmap` or `git -C roadmap ...`) whose subject line (the first line
  of the message, including one written through a heredoc or `-m`) is
  "chore: refresh workspace registry", and no commit anywhere has a
  message starting with "chore: bootstrap hub repo".

  FAIL if no such refresh commit was made, if a bootstrap commit was
  made, if a new hub directory was created (next to `roadmap/` or inside
  it), or if the skill stopped with a message asking to run it from the
  workspace root.
weight: 2
---

Inside the hub repo is a valid place to run from: the hub is refreshed,
never re-bootstrapped, and the skill does not stop as it would inside a
code repo.
