---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:usage[\\s\\S]*widgetcli add[\\s\\S]*widgetcli list[\\s\\S]*vibe:end:usage"
weight: 1
---

The commands in the usage section are what the user types: they are
never translated.
