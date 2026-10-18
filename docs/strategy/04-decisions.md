# Decisions

Settled with the maintainer. They replace the former open questions.

1. **Orchestrators.** One orchestrator for building (`feature` and `fix` as two entries): need framing, implementation framing, TDD, internal review loop. No dedicated research, splitting or documentation orchestrator for now; `backlog` and `docs` stay as they are.
2. **User-facing commands.** `review` and `verify` leave the `/` menu and serve the build loop. `challenge`, `consult` and `learn` stay as opt-in commands. `report-issue` is removed.
3. **Usage reports.** Each orchestrator writes anonymous statistics locally. Nothing leaves the user's machine unless they choose to share it. The improvement routine reads the reports it is given, plus synthetic cases.
4. **Surface.** Few visible commands for the PO. Bricks become `user-invocable: false`, like `tasks` and `publish`.

## Consequence for the plan

The routine cannot rely on a stream of real usage: its cases come mostly from synthetic scenarios and from reports users opt to share. Plan the eval corpus accordingly.
