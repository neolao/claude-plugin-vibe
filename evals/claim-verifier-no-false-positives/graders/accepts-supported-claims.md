---
type: llm
focus: last_message
criteria: |
  Each claim of the text is covered by the agent's "not a finding" list:
  - "listens on port 8000" is reasonably supported by `PORT = 8000`
    (fixtures/config.py:3), even though the file does not literally listen;
  - "around line 4" for `RETRIES = 3` at line 4 is an approximate wording
    that changes nothing;
  - "Both tests pass" is backed by the caller's command output (2 tests,
    OK), which matches the two tests in fixtures/test_config.py;
  - "In my view three retries is on the high side" is an opinion presented
    as one.

  PASS if none of the four is reported as a finding.
  FAIL if any of them is flagged as unproven, contradicted or an
  over-reaching conclusion.
weight: 2
---

Reasonable support, approximate wording, a provided proof and a marked
opinion are not hallucinations.
