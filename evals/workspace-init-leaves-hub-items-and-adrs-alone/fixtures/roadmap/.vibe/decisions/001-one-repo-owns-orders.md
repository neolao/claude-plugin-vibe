---
status: accepted
date: 2026-09-14
---
# 001 — One repo owns the orders domain

## Context
Two repos were writing order records.

## Decision
`orders-api` owns the `orders` domain; every other repo reads it through the API.

## Consequences
The storefront drops its local order table.
