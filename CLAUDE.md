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
- Le contenu marketing (bénéfices, tableau des commandes, agents, typical flow) est dérivé du README : le resynchroniser à la main quand les skills changent — `/vibe:docs` ne touche jamais aux fichiers non-Markdown de `docs/` (`index.html`, `.nojekyll`, assets), par conception.
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

- [ ] Le(s) fichier(s) Markdown modifié(s)/créé(s) ont un frontmatter complet et valide (`name`, `description`, et `argument-hint` ou `context`/`agent` selon le type ; pour un agent, `model:` et `version:` bumpée si son prompt ou son `model:` a changé — voir modèles existants dans `skills/*/SKILL.md` et `agents/*.md`)
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

## Agent model evals <!-- keep -->

Chaque agent de `agents/*.md` porte un champ `model:` et un champ `version:` (semver, ex. `1.0.0`) dans son frontmatter. Le modèle est un choix de coût/qualité par agent, distinct de la relecture manuelle ci-dessus ; la version identifie sans ambiguïté *quelle définition* de l'agent a produit un score donné — les deux se valident avec `claude plugin eval`, pas avec la suite de tests (qui n'existe pas et ne doit pas exister ici).

- Les cas vivent dans `evals/<nom-du-cas>/` (`prompt.md` pour le prompt, `graders/*.md` pour les critères) — un cas par scénario à vérifier pour un agent. Tout ce qui définit un cas est committé normalement.
- Une fixture statique (fichier de code à faire réviser par l'agent) a besoin des **deux** : `context.add_dirs` dans `case.yaml` ne fait que déclarer un droit de lecture, il ne copie rien — il faut en plus un `context.scaffold_script` (script bash dans le dossier du cas, ex. `fixture.sh`) qui copie `fixtures/` dans l'espace de travail vide du run (`cp -r "$(dirname "${BASH_SOURCE[0]}")/fixtures" .`), lancé uniquement via `--scaffold`.
- Toute modification du prompt ou du `model:` d'un agent bumpe son `version:` (patch pour un ajustement de formulation, minor pour un changement de checklist/catégorie, major pour une refonte de portée) — c'est ce bump qui signale qu'un nouveau run d'eval est dû, pas une inspection manuelle du diff.
- `evals/results/` est régénéré à chaque run et gitignored (`report.html`, `aggregate-result.json`, coûts liés à l'instant du run) — sauf `evals/results/history.md`, qui reste tracké : après un run jugé significatif (bump de `version:` sur un agent, ou nouveau cas), y ajouter une ligne (date, agent, version d'agent, cas, modèle, score, pass rate, coût, tokens, note courte) avant de committer. Le coût vient directement du total du CLI ; les tokens demandent `--keep-temp` (voir history.md pour le détail) — sans surcoût API, juste un run à ne pas nettoyer. Un score identique entre deux runs ne les rend pas équivalents : celui qui consomme moins de tokens/$ est le meilleur.
- **Modifier un cas périme son propre historique.** Toucher à une fixture, ajouter/scinder/supprimer un grader ou changer un poids change *ce que* le score mesure : les lignes déjà écrites pour ce cas ne se comparent plus aux suivantes. Dans le même commit que la modification du cas, marquer chacune de ces lignes d'un ⚠️ dans la colonne `Case` et ouvrir leur note par `**Obsolete (YYYY-MM-DD):** <ce qui a changé dans le cas>` — jamais supprimer la ligne, jamais retoucher ses chiffres. La comparaison repart du premier run postérieur au changement.
- **Une fixture ne nomme jamais le défaut qu'elle contient.** Les commentaires d'une fixture décrivent d'où le code est appelé et à quoi il sert (« Called from the checkout flow », « Called once per frame; the frame budget is 16ms »), jamais ce qui cloche. Un commentaire du type `# Isolation: état mutable partagé entre tests` transforme le cas en exercice de recopie et le score en 1.00 qui ne garantit rien. Même règle côté précision : du code propre n'a pas besoin de se défendre — pas de « not feature envy », pas de « no shared mutable state ». La seule exception est la justification qui *fait partie du domaine évalué* et que la définition de l'agent lui dit d'accepter (un fire-and-forget explicitement marqué, un cache avec un coût mesuré) : là, le commentaire est le signal, pas la réponse.
- **Un grader = une affirmation vérifiable.** Un cas de précision se découpe en un grader par motif neutralisé, pas un seul grader fourre-tout : un unique juge LLM qui porte les deux tiers du score rend le cas binaire et bruyant (voir les 0.56 / 1.00 / 0.33 de `review-naming` sur une fixture inchangée). Côté recall, un grader par catégorie, chacun avec **son propre ancrage dans le code** — si trois graders pointent la même ligne sous trois étiquettes, on mesure la verbosité du rapport, pas la détection.
- **Le prompt injecté à un agent reproduit mot pour mot ce que le skill lui envoie en vrai** (contrat de `skills/review/SKILL.md`, liste d'exclusions, drapeau de vérification dynamique). Un eval qui simplifie le contrat teste un agent qui n'existe pas — et peut contredire ses propres graders.
- **`allowed_tools` du cas doit couvrir les `tools:` dont l'agent a besoin *dans le mode testé*.** `review-tests`, `review-dependencies` et `review-web-security` déclarent `Bash` : sans `--allow-tools Bash` le cas mesure un agent amputé. Seule exception, `review-web-security` en mode statique : le prompt lui interdit de lancer quoi que ce soit, donc ses deux cas statiques n'ont pas `Bash` — c'est le cas de vérification dynamique qui le donne. Ce que le sandbox fournit compte aussi — pas de `pytest` installé, donc les fixtures de test se lancent avec `python3 -m unittest`.
- **Un cas qui accorde `Bash` se lance dans Docker, pas sur l'hôte** : sur le Mac du mainteneur, `~/.docker` contient des liens symboliques (Docker Desktop) et le sandbox d'eval refuse tout cas `Bash` (`DOCKER_CONFIG` n'y change rien). `evals/docker/run.sh <case-glob> [flags]` lance le cas dans un conteneur Linux avec les drapeaux canoniques, puis `tokens.py` sur le même run — voir `evals/docker/README.md`. Il faut `CLAUDE_CODE_OAUTH_TOKEN` (ou `ANTHROPIC_API_KEY`) dans l'environnement ; s'il manque, le signaler plutôt que de retirer `Bash` d'un cas pour le faire tourner sur l'hôte. Les cas sans `Bash` tournent toujours sur l'hôte.
- **Un cas doit pouvoir atteindre 1.00.** Deux graders mutuellement exclusifs (chemin A / chemin B d'un même skill) plafonnent le score sous le `--threshold 1.0` par défaut : un seul grader tolérant aux deux chemins, qui vérifie que l'agent *annonce* celui qu'il a pris.
- **Un cas de vérification dynamique se prouve à la main avant d'être committé.** L'app de la fixture n'a aucune dépendance à installer (bibliothèque standard), écoute sur `127.0.0.1` et garde son état en mémoire, pour qu'une instance locale soit jetable et relançable ; chaque exploit attendu est rejoué au curl et son résultat observé est recopié dans le grader correspondant. Un grader dynamique qui décrit un exploit jamais exécuté mesure une croyance, pas l'agent.
- **Un scaffold n'écrit rien hors du workspace du run.** Un `../origin.git` est partagé entre runs concurrents et survit au nettoyage ; le dépôt bare de secours vit dans le workspace (et dans `.gitignore`).
- Lancer un eval coûte de vrais tokens (appels réels au(x) agent(s) + juge LLM sur plusieurs runs) — c'est un geste manuel du Product Owner ou de Claude sur demande explicite, jamais déclenché automatiquement par un skill ou un hook.
- Valider un cas **nouveau ou modifié** isolément en `--runs 1` avant de le lancer à pleine échelle — un montage cassé (fixture non exposée, mauvais `subagent_type`, etc.) coûte le même prix à chaque run raté, et se découvre pour le prix d'un seul. Une fois les cas validés, les grouper dans une seule commande (`--case "review-*"`) ne coûte pas moins cher qu'un cas à la fois : chaque run est un process indépendant, rien n'est mutualisé entre cas. Le regroupement n'aide qu'en confort (un seul rapport) ; `-j`/`--concurrency` réduit le temps d'attente, pas le prix ; `--ablation none` divise le prix par ~2 une fois qu'on ne compare plus à une baseline sans plugin.

## Constraints

- Ne jamais committer de secrets ou identifiants
- Contenu de `skills/*/SKILL.md` (et fichiers voisins comme `skills/feature/workflow.md`) et `agents/*.md` (instructions à Claude, dialogue utilisateur, gabarits de rapport) toujours écrit en anglais, sans exception — le plugin tourne sur des projets/conversations dans n'importe quelle langue, aucun texte figé dans une langue particulière n'y a sa place
- Chaque skill (`skills/<nom>/SKILL.md`) et chaque agent (`agents/<nom>.md`) doit avoir un frontmatter complet et cohérent avec les fichiers existants (`tools:` en lecture seule sur les agents review, sauf ceux qui exécutent quelque chose)
- Pas de texte destiné au mainteneur (« kept identical », « update both together ») dans un prompt runtime : ce qui est partagé vit dans un seul fichier lu à l'invocation (`skills/feature/workflow.md`, contrat des agents dans `skills/review/SKILL.md`), voir ADR 004
- Ne pas laisser de fichier skill/agent orphelin ou de contenu obsolète après un renommage/suppression
- Garder le README comme index à jour des skills et de `docs/` (voir `/vibe:docs`)
- Ne pas ajouter de stack applicative (Node, Python, etc.) à ce dépôt sans demande explicite — ce n'est pas ce type de projet
  - Exception : `evals/` contient tout ce dont les évaluations ont besoin et peut donc héberger des scripts (Python, Bash…) — fixtures, scaffolds, outils comme `evals/tokens.py`. Ils ne constituent pas une stack applicative du plugin.

## Review agents

Agents actifs pour `/vibe:review` sur ce projet :

| Agent | Actif | Raison |
|---|---|---|
| `vibe:review-naming` | ✅ | conventions de nommage des skills/agents et fichiers |
| `vibe:review-security` | ✅ | secrets, injections dans le script et les manifestes JSON |
| `vibe:review-robustness` | ✅ | gestion d'erreurs du script shell |
| `vibe:review-hygiene` | ✅ | fichiers skill/agent obsolètes, contenu dupliqué entre définitions |
| `vibe:review-antipatterns` | ✅ | anti-patterns dans le script shell et les définitions de skills |
| `vibe:review-simplicity` | ✅ | s'applique au script shell et aux définitions Markdown (couvre aussi la complexité du script) |
| `vibe:review-overengineering` | ✅ | machinerie injustifiée dans le script et la structure du plugin |
| `vibe:review-tests` | ❌ | pas de suite de tests dans ce dépôt, par choix délibéré — rien à exécuter |
| `vibe:review-dependencies` | ❌ | aucun manifeste de dépendances dans ce dépôt |
| `vibe:review-solid` | ❌ | pas de code orienté objet/modulaire |
| `vibe:review-ddd` | ❌ | pas de couche domaine explicite |
| `vibe:review-architecture` | ✅ | `.vibe/` existe (généré par `/vibe:sync`) — pas d'architecture hexagonale à vérifier |
| `vibe:review-performance` | ❌ | pas d'API/serveur |
| `vibe:review-web-security` | ❌ | pas de surface HTTP exposée (ni statique, ni mode dynamique) |
