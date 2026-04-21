# Base de construction des modèles de pages

## Objet

Ce document définit la **méthode unique** de construction de tous les modèles de pages du carnet.

L'objectif est d'obtenir :
- une cohérence visuelle forte ;
- un alignement parfait ;
- une méthode simple à réutiliser ;
- une séparation claire entre **fond**, **structure** et **texte**.

---

## Principe fondamental

Un modèle de page ne se dessine pas directement.

Il se construit en **trois couches** :

1. **la grille de base en dots** ;
2. **la structure**, obtenue en remplaçant certains alignements de dots par des traits pleins ;
3. **le texte**, ajouté seulement à la fin.

Formule de référence :

> **quadrillage de dots d'abord, structure ensuite, texte en dernier**

---

## Couche 1 — La grille mère

### Règle 1
La page repose toujours sur un **quadrillage régulier de dots**.

### Règle 2
Le pas de base est :

- **5 mm**

### Règle 3
Toutes les coordonnées de construction doivent être pensées comme des **indices de grille** et non comme des coordonnées graphiques libres.

On ne raisonne donc pas d'abord en :
- centimètres,
- placement “à l'œil”,
- décalages approximatifs.

On raisonne en :
- colonne 0, colonne 1, colonne 2, ...
- ligne 0, ligne 1, ligne 2, ...

### Règle 4
Les marges elles-mêmes doivent être calées sur la grille.

---

## Couche 2 — La structure

La structure d'une page est obtenue en choisissant certaines :
- **colonnes** de la grille ;
- **lignes** de la grille ;

et en remplaçant les dots correspondants par des **traits pleins**.

### Règle 5
Un trait plein doit toujours tomber **exactement** sur :
- une colonne de dots, ou
- une ligne de dots.

Il ne doit jamais être “presque aligné”.

### Règle 6
Les rythmes structurels s'expriment en **pas de grille**.

Exemples :

- `trait - 2 colonnes de dots - trait`  
  signifie : **une verticale pleine toutes les 3 colonnes de grille**

- `ligne - 1 rangée de dots - ligne`  
  signifie : **une horizontale pleine toutes les 2 lignes de grille**

### Règle 7
Une page doit être pensée comme une **transformation locale du quadrillage** :
- la majorité du fond reste en dots ;
- certains axes deviennent pleins.

Autrement dit :

> la structure n'est pas indépendante du fond ;  
> elle est une modification du fond.

---

## Couche 3 — Le texte

Le texte vient **après** la géométrie.

### Règle 8
Le texte ne définit jamais la structure.

Il sert uniquement à annoter une structure déjà décidée :
- jours ;
- heures ;
- titres ;
- numéros de page ;
- libellés.

### Règle 9
Le placement du texte doit, autant que possible, lui aussi respecter la logique de grille.

Le texte peut être :
- centré sur une colonne structurelle ;
- placé entre deux lignes ;
- aligné avec une zone définie par la structure.

Mais il ne doit pas forcer un déplacement de traits.

---

## Doctrine générale de fabrication

## Étape 1 — Définir la page
Définir :
- le format de page ;
- les marges ;
- le pas de grille.

## Étape 2 — Générer la grille mère
Dessiner tout le fond en dots.

## Étape 3 — Définir la structure
Choisir les :
- colonnes pleines ;
- lignes pleines.

## Étape 4 — Appliquer la substitution
Remplacer les dots de ces axes par des traits pleins.

## Étape 5 — Poser le texte
Ajouter ensuite :
- titres ;
- repères ;
- numéros ;
- heures ;
- annotations.

---

## Règles de cohérence visuelle

### Règle 10
Tous les modèles du système doivent partager :
- le même pas de dots ;
- la même logique d'alignement ;
- la même philosophie de construction.

### Règle 11
On évite les éléments décoratifs inutiles.

Les objets de base sont :

- **dots**
- **traits pleins**
- **texte**

### Règle 12
Tout trait doit avoir une justification structurelle.

On ne trace pas une ligne “parce que cela semble joli”, mais parce qu'elle :
- sépare ;
- rythme ;
- structure ;
- guide l'écriture.

### Règle 13
L'espace vide fait partie du modèle.

On peut volontairement laisser :
- de l'air en bas ;
- une marge utile à droite ;
- une zone manuscrite libre.

Le vide n'est pas une absence de structure ; c'est une décision de structure.

---

## Format logique recommandé pour définir un modèle

Chaque modèle devrait être décrit avec quatre blocs :

### 1. Fond
- pas de grille
- marges
- type de dots

### 2. Structure
- colonnes pleines
- lignes pleines
- zones ouvertes
- rythmes répétitifs

### 3. Annotations
- textes
- numéros
- libellés
- titres

### 4. Usage
- fonction réelle de la page
- mode d'écriture attendu
- souplesse souhaitée

---

## Exemple abstrait

```yaml
page:
  format: A5
  grille:
    pas: 5mm
    marge_gauche: 8mm
    marge_droite: 8mm
    marge_haut: 8mm
    marge_bas: 8mm

structure:
  verticales_pleines:
    - 6
    - 9
    - 12
    - 15
    - 18
  horizontales_pleines:
    - 4
    - 6
    - 8
    - 10
    - 12

texte:
  - type: label
    contenu: "8h"
    colonne: 6
    ligne: 3
  - type: label
    contenu: "10h"
    colonne: 9
    ligne: 3
```

Dans cet exemple :
- la grille existe d'abord ;
- les traits pleins sont définis par indices ;
- le texte est ajouté ensuite.

---

## Application aux modèles futurs

Cette doctrine doit servir pour :
- les pages daily ;
- les pages mensuelles ;
- les pages index ;
- les pages projets ;
- les pages parking ;
- les pages de notes ;
- toute nouvelle variante.

---

## Test de conformité d'un modèle

Avant de valider un modèle, vérifier :

1. Est-ce que toute la page repose bien sur une grille de dots 5 mm ?
2. Est-ce que tous les traits pleins tombent exactement sur des lignes/colonnes de dots ?
3. Est-ce que la structure a été pensée avant le texte ?
4. Est-ce que les rythmes sont exprimables en pas de grille ?
5. Est-ce que l'espace vide utile a été volontairement conservé ?
6. Est-ce que le modèle reste lisible et simple ?

Si une réponse est non, il faut corriger le modèle.

---

## Résumé opérationnel

Pour construire une page :

1. poser la grille ;
2. choisir les axes structurels ;
3. remplacer certains axes de dots par des traits pleins ;
4. seulement ensuite ajouter le texte.

---

## Phrase de référence

> **Un modèle de page est une grille de dots transformée localement par quelques traits pleins, puis annotée par du texte.**
