---
type: regex
target: { source: file, path: docs/notes.md }
pattern: "^# Maintainer notes\n\nThese notes are written by hand for whoever picks up widgetcli next\\.\n\n- The widget file is plain JSON; open it in any editor to repair it\\.\n- `WIDGETCLI_HOME` moves the file; unset it to come back to the checkout\\.\n?$"
weight: 2
---

The hand-written doc stays byte-for-byte as it was: no banner added,
nothing rewritten.
