---
type: regex
pattern: '"":\s*\{\s*"name":\s*"fixture-app",\s*"version":\s*"1\.2\.4"'
target: { source: file, path: "package-lock.json" }
match: contains
weight: 2
---

The `packages[""]` entry of `package-lock.json` reads 1.2.4 as well — the
second place npm keeps it.
