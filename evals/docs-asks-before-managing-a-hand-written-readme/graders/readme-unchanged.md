---
type: regex
target: { source: file, path: README.md }
pattern: "^# widgetcli\n\nA tiny CLI to manage widgets from the command line\\.\n\n## About this project\n\nWidgetcli started as a personal weekend project to learn how to package small CLI tools; this paragraph is maintained entirely by hand and must never be rewritten by any tooling, no matter what else changes in this file\\.\n\n## Getting started\n\nInstall it with `npm install -g \\.` from a checkout, then run `widgetcli add \"My widget\"` and `widgetcli list`\\.\n?$"
weight: 2
---

The whole README is hand-written and stays byte-for-byte as it was:
nothing rewritten, nothing appended, no heading added.
