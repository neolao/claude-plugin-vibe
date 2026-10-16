# Rigor & Edge Cases Grid

## Mission
Hunt logic errors, gaps in the reasoning and degraded cases.

## Checklist
1. **Edge cases**: are extreme scenarios, errors and limit values handled?
2. **Soundness**: are there internal contradictions or fragile assumptions?
3. **Risks**: does the solution create side effects or regressions?

## Expected output
- `[PASS]` if the logic is robust — only when every checklist item carries a cited proof (file:line or a quoted sentence of the deliverable); an item without proof counts as `[FAIL]`.
- `[FAIL]` + the list of flaws or risks found otherwise.
