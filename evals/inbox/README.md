# Inbox — what real runs send back

Drop here what a vibe run leaves behind on a user's machine and that they chose to share:

- a **usage report** written by `vibe:report` — `.vibe/reports/<timestamp>-<entry>.md` in the user's project, statistics only (bricks called, rounds, questions, findings per level and space, fixes, escalations);
- an **escalation entry** copied from a project's `.vibe/escalations.md` — `## [date] /vibe:<skill> — title`, then `Context`, `Attempts`, `Diagnosis`, one short sentence each. **Redact it before sharing**: these fields were written about your code, so replace every path, identifier, ticket or product name with the brick, the step and the kind of failure ("the implementer's third launch still failed the red test on a boundary case"). A pull request is public from the moment it is opened.

Keep the file name, or prefix it with the date. A pull request adding the file is enough.

The `improve-skills-and-agents` routine reads the oldest file first, names the brick the signal implicates, writes a synthetic red eval case for the misbehavior, fixes the brick until the case is green, then moves the file to `done/` with a trailer naming the case. A file that still carries a project path, an identifier, a ticket or a product name is rejected: the routine deletes it and asks for it to be purged from the repository's history — this repository is public, nothing of a user's project belongs in it.

Nothing here is read by the plugin at runtime.
