---
type: llm
focus: last_message
criteria: |
  The repository is tagged v1.0.0 and v1.1.0, and CHANGELOG.md has a
  section for each.
  PASS if the report describes what was added (the fix under Fixed,
  since v1.1.0) and does not say that any tag or version lacks a section
  in the changelog, nor that any commit is written up nowhere.
  FAIL if the report warns that v1.1.0 (or any version) has no section,
  or that some released change is missing from the file.
weight: 2
---

The missing-section warning must not fire when the section is there.
