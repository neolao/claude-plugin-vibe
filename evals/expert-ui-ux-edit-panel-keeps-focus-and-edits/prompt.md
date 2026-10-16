---
name: expert-ui-ux-edit-panel-keeps-focus-and-edits
description: >-
  Recall side of the focus rule: a custom edit panel sliding over a table
  used all day from the keyboard. expert-ui-ux must require that focus moves
  into the panel when it opens and returns to the row that opened it when it
  closes, that typed-but-unsaved edits are not silently lost when the panel
  is dismissed, and that the permanent delete is confirmed — as a
  requirement, since the brief rules out a trash for this change — while
  prescribing nothing about how the panel or the focus ring looks, which is
  `expert-frontend-design`'s side of the boundary.
tags: [expert-ui-ux, recall, focus-management]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ui-ux` sub-agent (Agent tool, `subagent_type: "vibe:expert-ui-ux"`) with this brief plus the consultation request below.

Brief:

```
In our inventory web app, the products page is a table of a few hundred
rows. We're adding an edit panel: the Edit button at the end of a row slides
a panel in from the right, over the table, with the product's fields (name,
SKU, price, supplier, a free-text note), a Save button and a Delete button.
Save closes the panel and the row shows the new values; Delete removes the
product. The design system has no drawer or side-panel component, so the
panel is built for this page. Warehouse staff spend their day on this page
and work it from the keyboard, many rows in a row. A deleted product is gone
for good: there is no trash or archive today, and adding one is not part of
this change.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
