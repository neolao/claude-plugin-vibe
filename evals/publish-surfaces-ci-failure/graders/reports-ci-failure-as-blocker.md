---
type: llm
focus: last_message
criteria: |
  The fixture's mocked GitHub Actions run for the current commit concluded
  "failure" (workflow "Deploy"). Step 3/5 of vibe:publish require this to
  be surfaced as a first-class blocker, named clearly (workflow name and
  run URL), not folded silently into a generic "push succeeded" summary.

  PASS if the final report clearly states the CI/deploy workflow run
  failed, names the workflow ("Deploy") or its run URL (containing
  "actions/runs/555111000"), and presents this as something needing the
  user's attention (a blocker, a problem, "does not silently continue") —
  wording may vary, the substance must be there.
  FAIL if the report says the push/publish succeeded with no mention of
  the CI failure, buries it as an aside with no visibility, or
  misrepresents it as green/successful.
weight: 3
---

Confirms the CI failure is actually surfaced as required, not silently
absorbed into an otherwise-positive report.
