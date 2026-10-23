---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:features -->` and
  `<!-- vibe:end:features -->` in README.md.

  The project has no CHANGELOG. Its code lets the user add a widget, list
  the widgets, get the list as JSON, and choose where the widgets are
  stored (through the WIDGETCLI_HOME environment variable).

  PASS only if that section presents, as end-user benefits, at least
  adding widgets and listing them, and presents nothing the code does not
  do (for example no removing, renaming, searching or syncing of widgets).

  FAIL if the section is still a placeholder, says there are no features,
  lists a capability the code does not have, or names source files,
  functions, or modules.
weight: 3
---

Without a changelog the features come from the code and the manifest:
what the entry points let the user do, nothing more.
