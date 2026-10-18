# Inbox — what real runs send back

Drop here what a vibe run leaves behind on a user's machine and that they chose to share:

- a **usage report** written by `vibe:report` — `.vibe/reports/<timestamp>-<entry>.md` in the user's project, statistics only (bricks called, rounds, questions, findings per level and space, fixes, escalations);
- an **escalation entry** copied from a project's `.vibe/escalations.md` — `## [date] /vibe:<skill> — title`, then `Context`, `Attempts`, `Diagnosis`, one short sentence each.

Keep the file name, or prefix it with the date. A pull request adding the file is enough.

The `improve-skills-and-agents` routine reads the oldest file first, names the brick the signal implicates, writes a synthetic red eval case for the misbehavior, fixes the brick until the case is green, then moves the file to `done/` with a trailer naming the case. A file that carries a project path, a ticket or any free text beyond the escalation's own fields is rejected and moved to `done/` unread: this repository is public, nothing of a user's project belongs in it.

Nothing here is read by the plugin at runtime.
