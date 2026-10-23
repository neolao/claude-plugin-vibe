---
type: regex
pattern: '"name":\s*"fixture-app",\s*"version":\s*"1\.2\.4",\s*"lockfileVersion"'
target: { source: file, path: "package-lock.json" }
match: contains
weight: 2
---

The root `version` of `package-lock.json` reads 1.2.4.
