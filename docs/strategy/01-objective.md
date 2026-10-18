# Objective

vibe is the public plugin for **vibe coding**: the human is the Product Owner. They describe the need and judge the result. They do not write code, run tests or review diffs.

The plugin is generic: it works on any project, in any language, with no dependency on a given employer, forge or tool. It is the public counterpart of a personal plugin (`neolao`), with a different promise:

| | neolao (personal) | vibe (public) |
|---|---|---|
| Human role | Developer, in the loop | Product Owner, outside the loop |
| Review | A deliverable the developer reads | Internal only: findings drive fixes, the PO never reads them |
| Reporting a misbehavior | A command the developer runs | No command: a routine adds eval cases |
| Language | The developer's | English |

## The promise

The PO is only asked for what only a PO can decide: what is needed, which trade-off is acceptable, whether the result fits. Everything else is automated and proven — tests written first, the feature exercised for real, the build re-checked, the code reviewed by agents, the fixes applied.

If the result is not good, the tooling is what gets fixed, not the PO's workload.
