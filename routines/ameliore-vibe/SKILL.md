---
name: amliore-vibe
description: Améliore Vibe
---

But : amener chaque skill et chaque agent au score parfait (1.00) au coût le plus bas, puis durcir sa suite de cas pour lui trouver de nouvelles failles.

Dépôt : ~/workspace/claude-plugin-vibe. Périmètre : les skills de `skills/` et les agents de `agents/`, avec leurs cas sous `evals/`. Les conventions d'eval du dépôt sont dans la section « Agent model evals » de son `CLAUDE.md` : lis-la avant de commencer, elle fait foi.
**Une exécution de la routine = une seule cible (un skill ou un agent), dont on enchaîne tous les objectifs.** Ne touche à aucune autre cible pendant cette exécution, même si tu y remarques un problème : note-le dans la ligne de history.md.
Suis les étapes avec TaskCreate.

## Pérenniser ce que tu apprends sur l'exécution d'un cas
Quand tu découvres un problème ou une amélioration dans l'exécution d'un cas d'eval, pérennise-le pour que les exécutions suivantes n'aient pas à le redécouvrir.
Ça couvre ce qui concerne la façon de lancer ou de faire tourner un cas, pas le comportement de la cible : une commande ou un drapeau qui manque, une variable d'environnement à fournir, une limite du sandbox, une fixture qui ne s'installe pas, un piège de lecture de la trace, une étape à faire avant ou après le run.
- Si c'est une connaissance, écris-la dans la section « Agent model evals » du `CLAUDE.md`, ou `evals/docker/README.md` pour ce qui touche à Docker, à l'endroit où la prochaine exécution la lira. Ne la note pas seulement dans history.md, et pas dans ce prompt de routine (`routines/ameliore-vibe/SKILL.md`) : ne modifie jamais la routine elle-même, c'est à l'utilisateur de la faire évoluer.
- Si c'est un défaut d'un outil d'eval du dépôt (`evals/tokens.py`, `evals/docker/run.sh`, un script de scaffold), corrige l'outil.
Cette mise à jour est permise même si elle sort du périmètre de la cible. Commite-la à part, avant le commit de la cible, avec un message qui dit ce qui a été appris et comment tu l'as constaté.

## Effort (agents seulement)
Un agent peut fixer `effort:` dans son frontmatter : `low`, `medium`, `high`, `xhigh`, `max`. haiku ne gère pas l'effort : un agent sur haiku n'a pas de champ `effort:`. Un agent sans `effort:` hérite de l'effort de la session, qui n'est pas maîtrisé en eval : la première fois que tu règles l'effort d'un agent, écris le niveau explicitement. Quand tu changes le modèle d'un agent, repars de `effort: high` (retire le champ s'il passe sur haiku).

## 0. Garde de départ
`git status --porcelain` doit être vide et `git pull --rebase` doit réussir. Sinon, arrête-toi sans rien faire : quelqu'un travaille dans le dépôt, ou une exécution précédente n'est pas finie.

## 1. Choix de la cible
Pour chaque cible, son premier objectif en attente est le premier qui s'applique :
1. un de ses cas n'a aucune ligne non périmée dans `evals/results/history.md` (chercher `<nom-du-cas> |` sans le pipe ouvrant : une ligne périmée porte ⚠️ dans la cellule Case) ;
2. la dernière ligne non périmée d'un de ses cas est sous 1.00 ;
3. tous ses cas sont à 1.00.
Une cible dont un cas a sa dernière ligne marquée `**Manual follow-up needed:**` est exclue : ce cas est entre les mains de l'utilisateur.
Choisis la cible dont le premier objectif en attente a le plus petit numéro. À égalité, prends celle dont la ligne la plus récente est la plus ancienne.

## 2. Déroulé sur la cible, dans cet ordre
1. **Évaluer** : lance chacun de ses cas qui n'a pas de ligne non périmée.
2. **Corriger** : tant qu'un de ses cas est sous 1.00, applique la section 4.
3. **Réduire le coût** : une fois tous ses cas à 1.00, tente de réduire sa consommation, en baissant d'un cran son `effort:` ou son `model:` (agent seulement), et/ou en allégeant son prompt. Relance tous ses cas. Garde la réduction seulement si tous restent à 1.00 **et** que le coût est plus bas que celui de la dernière ligne de chaque cas. Sinon, reviens en arrière ; une ligne note l'essai.
4. **Durcir** : ajoute **un seul** nouveau cas, plus élaboré mais pertinent, fait pour essayer de faire baisser le score. Respecte les règles de cas du `CLAUDE.md` (une fixture ne nomme jamais le défaut qu'elle contient, un grader = une affirmation vérifiable, le prompt injecté reproduit mot pour mot le contrat du skill, un cas doit pouvoir atteindre 1.00). Lance-le. S'il est sous 1.00, applique la section 4. L'exécution se termine ensuite, même si la cible réussit ce nouveau cas.

## 3. Lancer
Un cas nouveau ou modifié se valide d'abord en `--runs 1`. Ce run de validation ne donne pas de ligne dans history.md ; seul le run complet qui suit en donne une.

Cas sans `Bash`, sur l'hôte, depuis la racine du dépôt — **la commande canonique**, ses deux lignes ensemble :
```bash
claude plugin eval . --case '<nom-du-cas>' --scaffold --judge-model sonnet \
  --ablation none --keep-temp --trust-plugin --no-publish \
  --output-dir evals/results/<nom-du-cas>
python3 evals/tokens.py evals/results/<nom-du-cas> --cleanup
```
Cas qui accorde `Bash` (son `allowed_tools`, ou le `--allow-tools` que demande sa définition) : lis d'abord `evals/docker/README.md`, puis lance `zsh -ic 'cd ~/workspace/claude-plugin-vibe && evals/docker/run.sh <nom-du-cas> --allow-tools <outils du cas>'`. Le `zsh -ic` est obligatoire : l'app ne transmet pas `CLAUDE_CODE_OAUTH_TOKEN` aux commandes qu'elle lance, seul le `~/.zshrc` le fournit. Ce script ajoute lui-même les drapeaux canoniques et lance `tokens.py` dans le même conteneur. Si `CLAUDE_CODE_OAUTH_TOKEN` manque, ne retire jamais `Bash` du cas pour le faire tourner sur l'hôte : documente le blocage dans la note et passe à l'objectif suivant.

N'improvise pas une autre commande, et ne fais jamais de `rm -rf /private/tmp/e-*` global : `tokens.py --cleanup` supprime exactement les dossiers du run.
Le juge est toujours sonnet : ne le change jamais, et ne rejoue jamais un cas avec un autre juge pour faire passer un score.

## 4. Score insuffisant
Lis la trace pour savoir qui est fautif :
- **le cas** (grader mal visé, fixture ambiguë) → corrige le cas et applique la règle « A changed case retires its own history » du haut de history.md (⚠️ dans la cellule Case, note ouverte par `**Obsolete (YYYY-MM-DD):**`) ;
- **la cible** (comportement contraire à sa propre définition) → corrige son prompt. Pour un agent, si un correctif du prompt ne suffit pas, monte d'abord son `effort:` d'un cran (`low` → `medium` → `high` → `xhigh` → `max` ; sans champ `effort:`, commence à `xhigh`), et ne monte son `model:` d'un cran (haiku → sonnet → opus) qu'une fois `max` atteint, ou depuis haiku, qui n'a pas d'effort.
Relance après chaque correctif. Garde une copie de chaque version essayée (cible et cas) dans le scratchpad, avec son score.
**Abandon** :
- agent : quand opus en `effort: max` échoue encore après un correctif ;
- skill (pas de `model:`) : après 5 correctifs sans atteindre 1.00.
Quand tu abandonnes, remets la cible et le cas dans la version qui a obtenu le meilleur score, et commite ce meilleur résultat. La note de sa ligne commence par `**Manual follow-up needed:**`, suivie de ton diagnostic ; le message de commit le dit aussi. L'exécution se termine là, sans passer aux objectifs suivants.

## 5. history.md
Le fichier est en anglais : écris tes lignes en anglais, avec ses colonnes (Date, Agent, Agent version, Case, Model, Score, Pass rate, Cost, Tokens in/out, Notes).
Une ligne par run complet, y compris les essais sous 1.00 (autre modèle, autre effort, correctif non retenu), dans le même commit que le résultat final. La colonne Tokens reprend la ligne `Tokens in/out` de `tokens.py` ; la note nomme le modèle et l'effort testés et ce qui a été essayé. Si `tokens.py` échoue (trace absent, rapprochement de coût en échec), n'écris aucun chiffre : mets l'erreur dans la note.

## 6. Commit
Bump la `version:` de la cible si elle a été modifiée (prompt, ou modèle ou effort pour un agent), selon la règle du `CLAUDE.md` (patch, minor ou major). `git add` uniquement les fichiers touchés, commite avec un message en anglais préfixé `test:` comme les commits d'eval existants, puis pousse sur main. Si le push est refusé, fais `git pull --rebase` une seule fois, puis arrête et documente.
