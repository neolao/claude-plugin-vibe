---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Read the whole README.md.

  PASS only if all of the following hold:
  - The features section (between the features markers) describes, as
    end-user benefits, both the JSON output capability and the configurable
    storage location that are listed under CHANGELOG's [Unreleased] section
    (json output for scripting; a configurable storage path via
    WIDGETCLI_HOME) — phrased as benefits, not copied verbatim from the
    changelog wording, and without naming files, functions, or modules.
  - The install section names installing the `widgetcli` package (e.g. via
    npm) consistent with package.json.
  - The usage section shows realistic examples of the real commands the code
    supports (`list`, `add`), not invented commands.

  FAIL if any managed section still looks like a placeholder, invents
  commands/behavior not backed by the manifest or code, or leaks file/function
  names into the user-facing features/install/usage sections.
weight: 2
---

The managed sections are rewritten with real content genuinely derived from
the manifest and CHANGELOG, not left stale or invented from nothing.
