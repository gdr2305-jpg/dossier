# Discussion — bullet journal numérique et Notewise

## Objet

Ce document garde la trace de la réflexion menée sur :

- la transposition d’un bullet journal papier vers un usage numérique sur tablette ;
- la création de modèles de pages A5 ;
- la logique de construction des templates à partir d’une grille de dots 5 mm ;
- l’architecture fonctionnelle d’un carnet numérique ;
- et la recherche d’applications capables d’améliorer la navigation interne, les renvois et l’usage quotidien.

---

## 1. Vision générale du bullet journal numérique

Le bullet journal visé n’est pas un planner rigide, mais un **cahier unique** dans lequel tout ou presque peut entrer :

- notes ;
- emploi du temps ;
- listes ;
- mémos ;
- travail ;
- personnel ;
- prière ;
- réunions ;
- idées ;
- projets ;
- réflexions.

L’objectif est de conserver ce qui faisait la force du papier :

- **index** ;
- **numérotation stable des pages** ;
- **renvois entre pages** ;
- **unité du carnet** ;
- **transfert sélectif** vers un nouveau carnet quand le précédent est terminé.

---

## 2. Architecture retenue du carnet

Le carnet est conçu en deux zones.

### Zone fixe au début

Le choix retenu est de réserver **40 pages au début** du carnet.

Répartition :

- pages 1 à 6 : index ;
- pages 7 à 10 : future log / vision annuelle ;
- pages 11 à 16 : listes durables ;
- pages 17 à 24 : collections stables ;
- pages 25 à 40 : réserve libre.

### Flux vivant ensuite

À partir de la **page 41**, commence le flux vivant du journal :

- mois ;
- semaines si besoin ;
- jours ;
- notes ;
- réunions ;
- projets ;
- travail ;
- personnel ;
- prière ;
- etc.

Formule de référence :

> le début du carnet contient l’infrastructure ; à partir de la page 41 commence la vie réelle du journal.

---

## 3. Doctrine de construction des modèles

Une réflexion approfondie a été menée sur la façon correcte de construire les modèles de pages.

### Principe fondamental

Un modèle ne doit pas être dessiné directement “à l’œil”.

Il doit être construit selon l’ordre suivant :

1. **grille mère en dots 5 mm** ;
2. **structure** obtenue en remplaçant certains alignements de dots par des traits pleins ;
3. **texte** ajouté ensuite.

Formule de référence :

> grille de dots d’abord, structure ensuite, texte en dernier.

### Règles importantes

- toutes les lignes et colonnes pleines doivent tomber **exactement** sur des lignes ou colonnes du quadrillage de dots ;
- les rythmes doivent être pensés en pas de grille ;
- le texte doit être placé soit **entre deux lignes**, soit **en face d’une ligne** ;
- pour les heures, le choix retenu est qu’une heure corresponde à une ligne, afin que l’espace entre deux lignes représente clairement un intervalle d’une heure.

---

## 4. Daily page

Plusieurs versions de pages daily A5 ont été testées.

La version retenue comme base satisfaisante est une version proche de la **v4**, avec :

- format A5 ;
- dots 5 mm ;
- page 1 = daily ;
- page 2 = dots seuls ;
- plage horaire ajustée ;
- dots plus visibles ;
- structure alignée sur la grille ;
- logique stricte de placement du texte.

Le daily a été pensé comme une page simple comprenant notamment :

- date ;
- page ;
- priorités ;
- zone temps ;
- tâches / bonus ;
- notes ;
- report / migration ;
- indexation éventuelle.

---

## 5. Réflexion sur les liens internes

Un point important de la réflexion a porté sur la possibilité de créer facilement des renvois internes.

L’idée explorée était :

> si écrire simplement `#1` créait automatiquement un lien vers la page 1, alors le numérique deviendrait au moins aussi puissant que le papier.

Constats :

- le format PDF sait gérer des liens internes ;
- Samsung Notes semble savoir **utiliser** certains liens déjà présents dans un PDF ;
- en revanche, aucune preuve solide n’a été trouvée montrant que Samsung Notes sache **créer nativement** des liens internes de type `#1` → page 1 ;
- l’idée d’un outil externe de post-traitement a été jugée peu viable en pratique.

---

## 6. Applications explorées

Plusieurs familles d’applications ont été examinées.

### Carnet manuscrit / PDF annoté

- Samsung Notes ;
- Goodnotes ;
- Nebo / MyScript Notes ;
- Notewise.

### Prise de notes généraliste / notes reliées

- OneNote ;
- Apple Notes ;
- Evernote ;
- Joplin ;
- Obsidian ;
- Bear ;
- UpNote ;
- RemNote.

### Journaling / diary

- Day One ;
- Journey ;
- Apple Journal.

### Étude / cours / documents

- LiquidText ;
- MarginNote ;
- RemNote.

Le but n’était pas de trouver “la meilleure application du marché”, mais de repérer celles qui se rapprochent d’un **bullet journal numérique enrichi**, avec un bon équilibre entre manuscrit, carnet, navigation, renvois et structure.

---

## 7. Pourquoi Notewise est apparue comme très intéressante

Parmi les applications étudiées, **Notewise** a retenu l’attention de façon particulière.

### Points forts relevés

Notewise documente explicitement une fonction permettant de **connecter les notes avec des liens**.

Il est possible de créer des liens vers :

- une page du même carnet ;
- une autre note ;
- une page d’une autre note ;
- un site web.

Notewise sait aussi :

- ouvrir les liens déjà présents dans un PDF ;
- utiliser les outlines PDF ;
- créer des outlines personnalisés ;
- organiser des pages et des carnets ;
- annoter des PDF ;
- enregistrer de l’audio ;
- proposer des fonctions d’étude et d’IA ;
- synchroniser les notes via Notewise Cloud.

### Limite importante

Aucune preuve n’a été trouvée montrant que Notewise transforme automatiquement une notation simple comme `#1` en lien vers une page.

La logique actuelle semble plutôt être :

- sélection d’un contenu ;
- création explicite du lien ;
- choix de la destination.

Donc, Notewise est plus avancé que Samsung Notes sur la question des renvois, mais n’atteint pas encore le geste idéal imaginé.

---

## 8. Comparatif synthétique Samsung Notes / Notewise

### Samsung Notes

Points forts :

- intégration native à l’écosystème Samsung ;
- simplicité d’usage ;
- bonne sensation de carnet ;
- annotation PDF ;
- stylet naturellement bien intégré.

Point faible principal :

- faiblesse sur les **liens internes** et la navigation structurée.

### Notewise

Points forts :

- vraie logique de carnet structuré ;
- liens internes entre pages et notes ;
- outlines et bookmarks ;
- meilleure profondeur fonctionnelle ;
- PDF, audio, organisation, sync, web et collaboration.

Point faible principal :

- application plus riche et plus complexe ;
- création de liens moins magique que le geste idéal `#1`.

Conclusion synthétique :

> Samsung Notes correspond mieux au cahier simple.
> Notewise semble plus proche d’un avenir numérique structuré.

---

## 9. Bilan général de la discussion

Les grandes idées retenues sont les suivantes.

### Sur le carnet

- garder un **cahier unique** ;
- réserver une **zone fixe de 40 pages** au début ;
- faire commencer le **flux vivant à la page 41** ;
- conserver index + pagination comme cœur du système.

### Sur les modèles

- construire les pages à partir d’une **grille mère en dots 5 mm** ;
- remplacer localement certains axes par des **traits pleins** ;
- ajouter le **texte seulement ensuite**.

### Sur les applications

- Samsung Notes reste bon pour la simplicité ;
- Notewise apparaît comme une piste particulièrement sérieuse pour un système de notes centralisé, manuscrit et mieux relié.

---

## 10. Orientation possible pour la suite

La discussion conduit à une piste claire :

- conserver la logique du bullet journal-cahier ;
- tester un système numérique qui garde index, pagination, renvois et flux vivant ;
- évaluer sérieusement si **Notewise** permet de mieux incarner cela que Samsung Notes au quotidien.

La question pratique sous-jacente devient :

> quel outil permet le mieux de rester fidèle à l’esprit du cahier papier tout en profitant des avantages du numérique ?
