# Backlog item 013 — Filter the report by period

## Description
Admins can restrict the monthly report to a period inside the month.

## Acceptance Criteria
1. `filter_period(rows, start, end)` returns the rows whose date is between `start` and `end`, both included.
2. Rows outside the period are left out.

## Constraints
- Dates are ISO strings (`YYYY-MM-DD`); do not introduce a date library.
