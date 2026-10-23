---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*legacy-batch\\s*\\|\\s*archived\\s*\\|\\s*Nightly invoice batch job\\s*\\|"
flags: ""
match: contains
weight: 3
---

`legacy-batch` was `active` and its directory is gone; the answer was
"archive it", so its row stays, with the status `archived` and its role
untouched.
