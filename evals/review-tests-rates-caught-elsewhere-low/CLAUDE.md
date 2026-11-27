# CLAUDE.md — payroll-service

## Project overview

A small Python service under `fixtures/`: `payroll.net_pay` computes the
amount written to the bank transfer file — it is the critical logic of this
service — and `memo.Memoizer` caches the result of a function per input.

## Testing conventions

Run the whole suite with `python3 -m unittest discover -s fixtures -v`
(no third-party test runner is installed). There is no separate e2e or
integration script — everything here is a fast unit test.
