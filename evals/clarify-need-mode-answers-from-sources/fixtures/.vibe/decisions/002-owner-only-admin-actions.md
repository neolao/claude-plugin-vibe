# 002 — Admin-page actions are owner-only

**Status:** accepted

## Decision
Any action on the admin page (export, archive, invite) is available to the `owner` role only. `member` users see the page read-only.

## Why
Members belong to several workspaces; an action taken in the wrong one is costly to undo.
