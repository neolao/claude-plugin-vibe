---
type: llm
focus: last_message
criteria: |
  Installing packages with the distribution's package manager needs root;
  asking the developer questions, writing a config file in the project and
  printing next steps do not. The expert's own checklist settles this: root
  only where strictly required, and stated.

  PASS if REQUIREMENTS or RISKS requires that elevated privileges be limited
  to the package-manager steps (for example `sudo` on those commands only,
  the script refusing to be run as root as a whole, or the config file
  written as the developer and not owned by root), and that the script says
  when it will ask for them.
  FAIL if privileges are never addressed, or if the reply accepts or
  requires running the whole script as root.
weight: 1
---

Confines root to the package-manager steps, as the least-privilege rule in
the expert's checklist requires.
