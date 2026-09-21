---
type: llm
focus: last_message
criteria: |
  `lodash` (`^4.17.21`) and `date-fns` (`^3.6.0`) use caret ranges, and
  fixtures/package-lock.json is committed and pins both to exact resolved
  versions. The agent's own instructions call this the ecosystem's
  convention, not a finding.

  PASS if no `high` or `medium` severity Version hygiene finding calls these
  ranges unpinned or floating.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not call a caret range with a committed lockfile unpinned.
