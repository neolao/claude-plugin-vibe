---
type: regex
pattern: 'version\s*=\s*"1\.11\.0"'
target: { source: file, path: "pyproject.toml" }
match: contains
weight: 2
---

`pyproject.toml` carries version 1.11.0 as well (Step 5: every manifest).
