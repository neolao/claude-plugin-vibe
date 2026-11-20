---
type: llm
focus: last_message
criteria: |
  fixtures/planner/static/js/calendar.js is the project's own script (it
  posts the booking form and lists the bookings); it states no library
  name or version. fixtures/planner/__init__.py and
  fixtures/planner/templates/index.html are the project's own code too.

  PASS if no finding block (`PACKAGE:` ... `CATEGORY:` ... `SEVERITY:`)
  names calendar.js, __init__.py or index.html as the package it reports
  on. A finding on jQuery or on flask, or one saying the audit tool could
  not run, passes.
  FAIL if any finding block reports calendar.js, __init__.py or
  index.html as a package (vendored library, unused, abandoned or any
  other category).
weight: 1
---

Does not turn the project's own code into a package: only a file that
states a library version is a dependency copied into the tree.
