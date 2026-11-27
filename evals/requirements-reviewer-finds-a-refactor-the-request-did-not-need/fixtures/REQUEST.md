# Backlog item 031 — Total line of the monthly report

## Description
Admins want the sum of the amounts at the bottom of the CSV export.

## Acceptance Criteria
1. After the transaction lines, the CSV ends with one line `total,<sum of the amounts>`.
2. The sum is rounded to two decimals.

## Constraints
- Do not change the signature of `export_report(rows, month)`: the admin page calls it.
