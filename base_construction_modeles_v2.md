# Base de construction des modèles de pages — version révisée

## Objet

Ce document définit la **doctrine de construction** de tous les modèles de pages du carnet.

Il sert de base unique pour fabriquer :
- les pages daily ;
- les pages mensuelles ;
- les pages index ;
- les pages projet ;
- les pages parking ;
- les pages de notes ;
- et toute autre variante future.

L'objectif est d'obtenir :
- une cohérence visuelle forte ;
- un alignement parfait ;
- une méthode simple et réutilisable ;
- une séparation claire entre **grille**, **structure** et **texte**.

---

## Principe général

Un modèle de page ne doit pas être dessiné “à l’œil”.

Il doit être construit selon l’ordre suivant :

1. **le quadrillage de base en dots** ;
2. **la structure**, en remplaçant certains alignements de dots par des traits pleins ;
3. **le texte**, ajouté seulement après.

Formule de référence :

> **grille de dots d'abord, structure ensuite, texte en dernier**

---

# 1. La grille mère

## 1.1. Nature de la grille

Toute page repose sur un **quadrillage régulier de dots**.

Ce quadrillage est la couche primitive du modèle.  
Tout le reste en dérive.

## 1.2. Pas de base

Le pas de base est :

- **5 mm**

Cela signifie que :
- l’écart horizontal entre deux colonnes de dots est de 5 mm ;
- l’écart vertical entre deux lignes de dots est de 5 mm.

## 1.3. Règle fondamentale

Toutes les décisions géométriques doivent être pensées à partir de cette grille.

On ne raisonne donc pas d’abord :
- en placement libre ;
- en coordonnées visuelles approximatives ;
- en “ça semble centré” ;
- en millimètres choisis indépendamment du quadrillage.

On raisonne d’abord en :
- colonne 0, colonne 1, colonne 2, ...
- ligne 0, ligne 1, ligne 2, ...

## 1.4. Marges

Les marges doivent elles aussi être **calées sur la grille**.

Exemple :
- 10 mm = 2 pas de grille ;
- 15 mm = 3 pas de grille.

Une marge ne doit pas casser la logique du quadrillage.

---

# 2. La structure

## 2.1. Définition

La structure d’une page est obtenue en choisissant certaines :
- **colonnes** de la grille ;
- **lignes** de la grille ;

et en remplaçant les dots correspondants par des **traits pleins**.

Autrement dit :

> un trait plein n’est pas un objet indépendant du quadrillage ;  
> c’est une transformation locale du quadrillage.

## 2.2. Règle d’alignement absolu

Un trait plein doit toujours tomber **exactement** sur :
- une colonne de dots, ou
- une ligne de dots.

Jamais :
- entre deux colonnes ;
- entre deux lignes ;
- “presque aligné” ;
- ou décalé pour arranger le texte.

## 2.3. Rythmes structurels

Les rythmes doivent toujours être exprimés en **pas de grille**.

Exemples :

### Vertical
- `trait - 2 colonnes de dots - trait`

signifie :

- une verticale pleine toutes les **3 colonnes** de grille

### Horizontal
- `ligne - 1 rangée de dots - ligne`

signifie :

- une horizontale pleine toutes les **2 lignes** de grille

## 2.4. Le vide fait partie de la structure

Une zone vide utile peut être volontairement conservée :
- en bas ;
- à droite ;
- dans une zone manuscrite ;
- dans un encart.

Le vide n’est pas un oubli.  
C’est une décision structurelle.

---

# 3. Le texte

Le texte est une couche d’annotation.  
Il ne définit jamais la géométrie.

## 3.1. Principe

Le texte vient **après** :
- la grille ;
- les traits pleins ;
- l’organisation spatiale.

## 3.2. Règle de placement

Le texte doit être placé selon l’une de ces deux logiques :

### Cas A — texte entre deux lignes
Le texte est placé **dans l’espace entre deux lignes structurelles**.

C’est le cas normal pour :
- les titres de section ;
- les libellés de bloc ;
- les mots comme `Temps`, `Bonus`, `Notes`, etc.

Exemple :
- `TEMPS` entre la ligne supérieure du bloc et la première ligne d’écriture ;
- `NOTES` entre la ligne de séparation et la zone de notes.

### Cas B — texte en face d’une ligne
Le texte est placé **exactement en correspondance avec une ligne**.

C’est le cas normal pour :
- les heures ;
- certains repères numériques ;
- certains index de ligne.

Exemple fondamental :
- `8h` est en face de la ligne 8h ;
- `9h` est en face de la ligne suivante.

Ainsi, l’espace entre la ligne `8h` et la ligne `9h` représente clairement **une heure**.

## 3.3. Conséquence pratique

Le texte ne doit jamais être placé de manière ambiguë.

En particulier :
- une heure ne doit pas flotter entre deux lignes si elle est censée correspondre à une ligne ;
- un titre de bloc ne doit pas être collé à une ligne s’il est censé nommer l’espace entre deux lignes.

---

# 4. Doctrine de construction

## Étape 1 — Définir la page
Définir :
- le format de page ;
- les marges ;
- le pas de grille.

## Étape 2 — Générer la grille mère
Dessiner tout le fond en dots.

## Étape 3 — Définir la structure
Choisir :
- les colonnes pleines ;
- les lignes pleines ;
- les rythmes ;
- les zones ouvertes.

## Étape 4 — Appliquer la substitution
Remplacer certains alignements de dots par des traits pleins.

## Étape 5 — Poser le texte
Ajouter ensuite :
- titres ;
- jours ;
- heures ;
- numéros ;
- annotations.

Ordre impératif :

> **fond → structure → texte**

---

# 5. Objets de base autorisés

Les objets fondamentaux d’un modèle sont :

- **dots**
- **traits pleins**
- **texte**

On évite les éléments décoratifs inutiles.

Un modèle doit rester lisible, sobre et fonctionnel.

---

# 6. Conséquences pour les modèles concrets

## 6.1. Daily

Pour un daily :
- le quadrillage reste visible ;
- certaines lignes deviennent pleines ;
- certaines colonnes deviennent pleines ;
- les heures sont placées **en face de lignes** ;
- les titres de zones sont placés **entre deux lignes**.

## 6.2. Mensuel

Pour un suivi mensuel :
- les lignes de jours sont des lignes du quadrillage devenues pleines ;
- les colonnes de suivi sont des colonnes du quadrillage devenues pleines ;
- les numéros de jours et les horaires sont ajoutés ensuite ;
- l’espace vide à droite ou en bas peut être volontairement gardé.

## 6.3. Index / Projet / Notes

Même logique :
- d’abord le quadrillage ;
- puis les substitutions structurelles ;
- puis les annotations.

---

# 7. Représentation logique recommandée

Un modèle doit être définissable par quatre blocs :

## 7.1. Fond
- format
- marges
- pas de grille
- dots

## 7.2. Structure
- colonnes pleines
- lignes pleines
- rythmes répétitifs
- zones ouvertes

## 7.3. Texte
- contenu
- type
- ancrage
- règle de placement :
  - entre deux lignes
  - en face d’une ligne

## 7.4. Usage
- fonction réelle de la page
- écriture attendue
- degré de liberté manuscrite

---

# 8. Exemple abstrait

```yaml
page:
  format: A5
  grid:
    step_mm: 5
    margins_mm:
      left: 10
      right: 10
      top: 10
      bottom: 10

structure:
  vertical_solid_columns: [6, 9, 12, 15, 18]
  horizontal_solid_rows: [4, 6, 8, 10, 12]

text:
  - kind: section_label
    text: "TEMPS"
    placement: between_rows
    row_top: 12
    row_bottom: 11

  - kind: hour_label
    text: "8h"
    placement: on_row
    row: 10

  - kind: hour_label
    text: "9h"
    placement: on_row
    row: 9
```

Dans cet exemple :
- la grille existe d’abord ;
- la structure transforme certains axes ;
- le texte est ajouté ensuite selon une règle claire de placement.

---

# 9. Test de conformité d’un modèle

Avant de valider un modèle, vérifier :

1. Toute la page repose-t-elle bien sur une grille de dots 5 mm ?
2. Tous les traits pleins tombent-ils exactement sur des lignes/colonnes de dots ?
3. La structure a-t-elle été pensée avant le texte ?
4. Les rythmes sont-ils exprimables en pas de grille ?
5. Les titres sont-ils placés entre deux lignes quand c’est leur rôle ?
6. Les heures ou repères linéaires sont-ils placés en face de leur ligne ?
7. L’espace vide utile a-t-il été volontairement conservé ?
8. Le modèle reste-t-il lisible, simple et manuscritement exploitable ?

Si une réponse est non, le modèle doit être corrigé.

---

# 10. Résumé opérationnel

Pour construire une page :

1. poser la grille ;
2. choisir les axes structurels ;
3. remplacer certains axes de dots par des traits pleins ;
4. ajouter le texte selon une règle explicite :
   - soit entre deux lignes ;
   - soit en face d’une ligne.

---

# 11. Phrase de référence

> **Un modèle de page est une grille de dots transformée localement par quelques traits pleins, puis annotée par un texte placé soit entre deux lignes, soit en face d’une ligne.**
