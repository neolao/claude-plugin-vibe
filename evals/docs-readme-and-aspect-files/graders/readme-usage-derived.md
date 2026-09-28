---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:usage -->` and
  `<!-- vibe:end:usage -->` in README.md.

  The CLI implements exactly these commands: `widgetcli add <name>`,
  `widgetcli list`, and `widgetcli list --json`. It also reads one
  environment variable, `WIDGETCLI_HOME`, which sets the storage folder.

  PASS only if that section shows realistic examples of `add` and `list`,
  and shows no command or flag outside the three above (for example no
  `remove`, `delete`, or `--help` command). Setting `WIDGETCLI_HOME` in an
  example is allowed. Invoking the commands through `npm start --` instead
  of `widgetcli` is allowed too.

  FAIL if the section is still a placeholder, omits `add` or `list`, or
  shows a command or flag the CLI does not implement.
weight: 1
---

The usage section only shows commands the code supports.
