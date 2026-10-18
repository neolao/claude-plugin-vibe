# Inbox — what real runs send back

Drop here the one thing a vibe run leaves behind on a user's machine that can be shared without exposing the project:

- a **usage report** written by `vibe:usage-report` — `.vibe/usage-reports/<timestamp>-<entry>.md` in the user's project, statistics only (bricks called, rounds, questions, findings per level and space, fixes, escalations);

Nothing else is accepted — in particular no escalation entry from `.vibe/escalations.md`: its fields describe the project's code. Keep the file name, or prefix it with the date. A pull request adding the file is enough.

The `improve-skills-and-agents` routine reads the oldest file first, names the brick the signal implicates, writes a synthetic red eval case for the misbehavior, fixes the brick until the case is green, then moves the file to `done/` with a trailer naming the case. A file that is not a usage report, or that carries any text beyond the report's own keys, is rejected: the routine deletes it and asks for it to be purged from the repository's history — this repository is public, nothing of a user's project belongs in it.

Nothing here is read by the plugin at runtime.
