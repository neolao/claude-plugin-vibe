# CLAUDE.md — claude-plugin-vibe

> Auto-généré par /vibe:init. Modifiable librement — relancer /vibe:init pour régénérer.
> Ajouter `<!-- keep -->` sur un titre de section pour la préserver lors d'une régénération.

## Project overview

`claude-plugin-vibe` est un **plugin Claude Code** : il ne s'agit pas d'une application avec un runtime propre, mais d'un ensemble de définitions Markdown (skills et agents) qui outillent la méthodologie « vibe coding » — l'humain reste Product Owner (il décrit le besoin et évalue le résultat), Claude écrit, teste, revoit et livre le code des *autres* projets sur lesquels ce plugin est installé.

**Stack :** aucune — pas de manifeste de langage (`package.json`, `pyproject.toml`, etc.). Le contenu est du Markdown (skills, agents) + un script Bash (`scripts/subagent-statusline.sh`) + des manifestes JSON (`plugin.json`, `marketplace.json`, `settings.json`).
**Type :** Claude Code plugin (méta-outillage), pas une application exécutable.

## Architecture

```
claude-plugin-vibe/
├── .claude-plugin/   # manifeste du plugin (plugin.json) et du marketplace (marketplace.json)
├── skills/           # commandes slash /vibe:* — un dossier par skill, chacun avec un SKILL.md
├── agents/           # sub-agents de revue spécialisés, un par dimension de qualité
├── scripts/          # scripts shell (ex: subagent-statusline.sh pour la barre de statut)
├── settings.json     # câble le hook subagentStatusLine au script ci-dessus
└── README.md         # description du plugin + index de docs/ (géré par /vibe:docs)
```

<!-- L'import ci-dessous charge la carte compacte du dépôt dans chaque session. Maintenu par /vibe:sync. -->
@.vibe/index.md

## Site GitHub Pages <!-- keep -->

Le site vitrine <https://neolao.github.io/claude-plugin-vibe/> est servi par GitHub Pages depuis `docs/` sur `main`. **Aucun build** : `docs/index.html` est une page unique autonome (CSS/JS inline, zéro CDN) — modifier le fichier et pousser suffit, le déploiement prend une à deux minutes.

À savoir pour la faire évoluer :
- Les démos de terminal sont des animations scriptées dans l'objet JS `DEMOS` en bas de `index.html` (types de lignes : `cmd` tapée au clavier, `out` affichée, `run` avec spinner résolu via `after`+`done`, `gap`). Ajouter une démo = un bloc `.term` avec `data-demo="<clé>"` + une entrée dans `DEMOS`.
- Le contenu marketing (bénéfices, tableau des commandes, agents, typical flow) est dérivé du README : le resynchroniser à la main quand les skills changent — `/vibe:docs` a interdiction de toucher aux fichiers du site (`index.html`, `.nojekyll`, assets non-Markdown), voir `skills/docs/SKILL.md`.
- `docs/.nojekyll` doit rester présent (GitHub Pages sert alors le HTML tel quel).
- Ne pas réintroduire les pièges mobiles corrigés : `overflow-x: clip` sur `html`+`body`, halo du hero plafonné à `min(900px, 130vw)`, tableau des commandes en cartes empilées sous 640 px.
- Vérification sans navigateur : `node --check` sur le script inline extrait, contrôle d'équilibre des balises (parseur HTML Python), `python3 -m http.server` dans `docs/`.

## Development workflow (Vibe Coding)

L'utilisateur reste **Product Owner uniquement** : il décrit ce qu'il veut (nouveau skill, nouvel agent, évolution du README) et évalue le résultat — il n'écrit pas et ne teste pas manuellement les fichiers.

### Particularité de ce dépôt

Ce dépôt n'a **pas de suite de tests automatisée ni de linter**, par choix délibéré : il n'y a pas de code applicatif à exécuter, seulement des définitions Markdown/JSON consommées par Claude Code lui-même. La qualité repose donc sur :
- la relecture manuelle du contenu généré (skills, agents, README) présenté à l'utilisateur avant validation,
- la cohérence stricte du frontmatter et de la structure entre fichiers similaires,
- une validation JSON basique des manifestes avant commit.

Ne pas introduire de `package.json`, suite de tests ou linter pour ce dépôt sans demande explicite de l'utilisateur.

### Definition of Done

Une tâche (nouveau skill, nouvel agent, modification de la doc) est terminée seulement si :

- [ ] Le(s) fichier(s) Markdown modifié(s)/créé(s) ont un frontmatter complet et valide (`name`, `description`, et `argument-hint` ou `context`/`agent` selon le type — voir modèles existants dans `skills/*/SKILL.md` et `agents/*.md`)
- [ ] Les fichiers JSON touchés (`plugin.json`, `marketplace.json`, `settings.json`) restent syntaxiquement valides (vérification manuelle, ex. `jq .` ou relecture attentive)
- [ ] Aucun secret ni identifiant en dur
- [ ] Le `README.md` reste cohérent avec les skills existants (tableau « Skills (commands) » à jour) — utiliser `/vibe:docs` si le changement est user-facing
- [ ] Aucun contenu de démonstration ou brouillon oublié dans les fichiers livrés
- [ ] Le résultat est présenté à l'utilisateur pour relecture avant d'être considéré comme terminé — il n'y a pas de gate automatique ici

**Ne jamais présenter un résultat comme terminé sans l'avoir relu soi-même** (pas de tests pour le garantir à la place).

### Workflow pour ajouter/modifier un skill ou un agent

1. Repérer le skill/agent existant le plus proche en portée et en suivre la structure (frontmatter, ton, niveau de détail)
2. Rédiger/modifier le fichier Markdown avec un frontmatter complet
3. Si des fichiers JSON sont touchés, relire leur syntaxe attentivement
4. Mettre à jour `README.md` (table des skills, sections gérées) si le changement change le comportement visible pour l'utilisateur du plugin — via `/vibe:docs`
5. Présenter la diff à l'utilisateur pour validation

### Self-correction loop

En l'absence de tests/lint automatisés, l'auto-correction se limite à :
- relire son propre changement avant de le présenter,
- vérifier la cohérence avec les fichiers similaires existants,
- signaler à l'utilisateur toute ambiguïté sur la portée d'un nouveau skill/agent plutôt que de deviner.

## Testing conventions

Pas de suite de tests automatisée dans ce dépôt (choix délibéré, voir « Particularité de ce dépôt » ci-dessus). La confiance vient de la relecture humaine du contenu Markdown/JSON produit, pas de tests exécutables.

## Constraints

- Ne jamais committer de secrets ou identifiants
- Chaque skill (`skills/<nom>/SKILL.md`) et chaque agent (`agents/<nom>.md`) doit avoir un frontmatter complet et cohérent avec les fichiers existants
- Ne pas laisser de fichier skill/agent orphelin ou de contenu obsolète après un renommage/suppression
- Garder le README comme index à jour des skills et de `docs/` (voir `/vibe:docs`)
- Ne pas ajouter de stack applicative (Node, Python, etc.) à ce dépôt sans demande explicite — ce n'est pas ce type de projet

## Review agents

Agents actifs pour `/vibe:review` sur ce projet :

| Agent | Actif | Raison |
|---|---|---|
| `vibe:review-naming` | ✅ | conventions de nommage des skills/agents et fichiers |
| `vibe:review-complexity` | ✅ | s'applique au script `scripts/subagent-statusline.sh` |
| `vibe:review-security` | ✅ | secrets, injections dans le script et les manifestes JSON |
| `vibe:review-robustness` | ✅ | gestion d'erreurs du script shell |
| `vibe:review-hygiene` | ✅ | fichiers skill/agent obsolètes, contenu dupliqué entre définitions |
| `vibe:review-tests` | ❌ | pas de suite de tests dans ce dépôt, par choix délibéré — rien à exécuter |
| `vibe:review-dependencies` | ❌ | aucun manifeste de dépendances dans ce dépôt |
| `vibe:review-solid` | ❌ | pas de code orienté objet/modulaire |
| `vibe:review-ddd` | ❌ | pas de couche domaine explicite |
| `vibe:review-architecture` | ✅ | `.vibe/` existe (généré par `/vibe:sync`) |
| `vibe:review-performance` | ❌ | pas d'API/serveur |
| `vibe:review-web-security` | ❌ | pas de surface HTTP exposée |
