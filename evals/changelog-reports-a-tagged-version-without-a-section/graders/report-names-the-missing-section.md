---
type: llm
focus: last_message
criteria: |
  The repository is tagged v1.0.0 and v1.1.0; CHANGELOG.md has a [1.0.0]
  section and no [1.1.0] section.
  PASS if the report says that v1.1.0 (the tag the range starts at) has
  no section in the changelog, or that the commits up to v1.1.0 are
  written up nowhere — any wording that lets the reader know the gap
  exists.
  FAIL if the report does not mention that v1.1.0 lacks a section, or
  claims to have created one.
weight: 2
---

A tag cut without its section leaves its changes out of the file for
good unless the report says so.
