# Standard de coordonnées des dots

## Statut

Ce document fixe la convention de repérage à utiliser pour tous les PDF de test du projet `notewise_bullet_generator`.

Objectif : éviter les corrections ambiguës du type "un peu plus haut", "le dernier carré", "le trait sous le titre".

Les corrections visuelles doivent désormais être données à partir de coordonnées directement alignées sur les dots de la grille 5 mm.

---

## 1. Principe général

Un repère de coordonnées correspond toujours à un **dot réel** de la grille.

La grille du projet repose sur :

```text
GRID_STEP_MM = 5
```

Donc :

```text
1 colonne = 5 mm
1 ligne = 5 mm
```

Les coordonnées ne doivent pas être une grille décorative indépendante. Elles doivent être calculées sur la même base que les fonctions de géométrie du projet :

```python
gx(col)
gy(row)
```

---

## 2. Origine du repère

Convention retenue :

```text
A1 = premier dot en haut à gauche de la zone utile
```

Puis :

```text
A, B, C, D... = colonnes de gauche à droite
1, 2, 3, 4... = lignes de haut en bas
```

Attention : dans le code ReportLab, l'axe vertical naturel part du bas de page. Le repère utilisateur doit, lui, être lisible visuellement depuis le haut de la page.

Il faudra donc prévoir une conversion explicite entre :

```text
coordonnée utilisateur : A1, B1, A2...
coordonnée interne ReportLab : gx(...), gy(...)
```

---

## 3. Texte

Pour un texte, la coordonnée désigne le **point de départ du texte**.

Exemple :

```text
Mettre PRIORITÉS en A5
```

Signifie :

```text
le texte PRIORITÉS commence au dot A5
```

Pour les petits ajustements fins, on peut exceptionnellement préciser un décalage en millimètres :

```text
Mettre PRIORITÉS en A5 + 1 mm vers le haut
```

Mais la position de base doit rester une coordonnée de dot.

---

## 4. Carrés

Pour un carré, la coordonnée désigne le **coin supérieur gauche du carré**.

Exemple :

```text
Mettre un carré en L14
```

Signifie :

```text
le coin supérieur gauche du carré est placé sur le dot L14
```

Cette convention est prioritaire. Ne pas utiliser une convention implicite du type "carré centré sur le dot".

---

## 5. Traits horizontaux

Pour un trait horizontal, on donne le dot de départ et le dot d'arrivée.

Exemple :

```text
Trait horizontal de C8 à R8
```

Signifie :

```text
le trait commence au dot C8
le trait finit au dot R8
```

---

## 6. Traits verticaux

Pour un trait vertical, on donne le dot de départ et le dot d'arrivée.

Exemple :

```text
Trait vertical de K10 à K24
```

Signifie :

```text
le trait commence au dot K10
le trait finit au dot K24
```

---

## 7. Fichiers de test

Chaque page importante doit pouvoir être produite en deux versions :

```text
*_debug_coords.pdf
*_clean.pdf
```

La version debug contient :

```text
dots + lettres de colonnes + numéros de lignes
```

La version clean contient :

```text
dots uniquement, sans coordonnées
```

Les coordonnées ne doivent jamais apparaître dans la version finale destinée à l'usage réel dans Notewise.

---

## 8. Règle de travail

Nouvelle méthode de correction visuelle :

```text
1. Générer un PDF debug avec coordonnées.
2. Donner les corrections avec coordonnées.
3. Modifier le code localement.
4. Régénérer debug + clean.
5. Valider visuellement.
6. Intégrer seulement ensuite dans le générateur principal.
```

---

## 9. Exemples de demandes correctes

```text
Supprimer le trait horizontal de B6 à R6.
Ajouter un carré en L14.
Déplacer le texte PRIORITÉS de A5 à A4.
Remonter NOTES de K22 à K21.
Aligner le début des traits de TÂCHES sur N13.
```

---

## 10. Ce qu'il faut éviter

Éviter les indications non coordonnées :

```text
un peu plus haut
le dernier carré
le trait du milieu
la ligne juste au-dessus
le bloc du bas
```

Ces formulations peuvent être utilisées oralement pour expliquer, mais la correction finale doit être exprimée avec les coordonnées des dots.

---

## 11. Formule courte à retenir

```text
A1 = dot en haut à gauche.
Colonnes = lettres.
Lignes = numéros.
Chaque coordonnée = un dot réel tous les 5 mm.
Texte : coordonnée = départ du texte.
Carré : coordonnée = coin supérieur gauche.
Trait : coordonnée = départ et arrivée.
```
