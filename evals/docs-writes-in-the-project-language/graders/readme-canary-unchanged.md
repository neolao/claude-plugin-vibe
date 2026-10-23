---
type: regex
target: { source: file, path: README.md }
pattern: "Widgetcli est né d'un week-end de bricolage pour apprendre à empaqueter de petits outils en ligne de commande ; ce paragraphe est tenu à la main et aucun outil ne doit le réécrire, quoi qu'il arrive au reste du fichier\\."
match: contains
weight: 1
---

The hand-written README paragraph outside the managed markers survives
byte-for-byte.
