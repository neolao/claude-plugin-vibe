---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:features -->` and
  `<!-- vibe:end:features -->` in README.md.

  PASS only if that section describes, as end-user benefits, both
  capabilities listed under CHANGELOG's [Unreleased] section: JSON output of
  the widget list for scripting, and a configurable storage location (via
  the WIDGETCLI_HOME environment variable or equivalent wording). Phrasing
  them as benefits rather than copying the changelog lines is expected.

  FAIL if either capability is missing, if the section is still a
  placeholder, or if it names source files, functions, or modules.
weight: 1
---

The features section is derived from the CHANGELOG, including the
[Unreleased] entries, and phrased for the end user.
