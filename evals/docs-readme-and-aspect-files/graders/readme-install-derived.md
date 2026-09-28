---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:install -->` and
  `<!-- vibe:end:install -->` in README.md.

  PASS only if that section gives a concrete way to install the `widgetcli`
  command that is consistent with package.json (an npm package named
  `widgetcli` exposing a `widgetcli` bin, run with Node.js). Installing from
  a registry (`npm install -g widgetcli`) or from a checkout of the source
  (`npm install -g .`, `npm link`) are both acceptable.

  FAIL if the section is still a placeholder, gives no install command, or
  describes an install method unrelated to an npm/Node.js package.
weight: 1
---

The install section is derived from the manifest.
