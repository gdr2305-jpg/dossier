# Notewise Bullet Generator

## 1. Objectif du projet

Ce projet vise à construire un **bullet journal numérique complet**, optimisé pour une utilisation sur tablette avec stylet.

L’objectif n’est pas simplement de produire un PDF, mais de créer un **outil de travail quotidien structuré, rapide et robuste**, équivalent (voire supérieur) à un bullet journal papier.

---

## 2. Philosophie du bullet journal

### 2.1 Stabilité des repères

Contrairement à un bullet papier :

- les pages fixes ne bougent jamais
- les emplacements sont constants
- la navigation devient réflexe

👉 Cela réduit fortement la charge cognitive.

---

### 2.2 Séparation structure / contenu

Le système repose sur deux blocs :

**Structure fixe (pré-générée)**
- index
- mois
- collections

**Zone vivante (daily)**
- écriture libre
- adaptation au réel

👉 On ne redessine jamais la structure.
👉 On se concentre uniquement sur l’usage.

---

### 2.3 Navigation rapide

Chaque page contient des accès directs vers :
- INDEX
- MOIS
- PARKING
- PRIÈRES

👉 Le carnet devient **navigable comme une application**.

---

### 2.4 Minimalisme fonctionnel

Le design est volontairement :
- sobre
- basé sur une grille régulière
- sans surcharge

👉 objectif : écrire vite et penser vite.

---

## 3. Choix de Notewise

### 3.1 Pourquoi Notewise

Le choix de Notewise repose sur :

- excellente gestion du stylet
- fluidité d’écriture
- bonne gestion des PDF volumineux
- support des hyperliens internes

👉 Notewise permet d’utiliser le PDF comme un **outil interactif réel**.

---

### 3.2 Logique d’usage

Le PDF devient :

- le support principal
- le système de navigation
- la structure du travail

👉 L’application sert uniquement de support.

---

## 4. Architecture technique

### 4.1 core/

Contient les briques fondamentales :

- config : paramètres globaux
- geometry : coordonnées
- grid : dimensions
- draw : primitives graphiques
- text : gestion du texte

👉 Toute la logique graphique est centralisée ici.

### 4.1.1 Règles techniques stables

Le projet repose sur quelques règles strictes :

- alignement sur une **grille 5 mm**
- aucune coordonnée libre hors système de grille
- usage systématique de `gx()` et `gy()` pour les placements
- dessin via `draw_dots()`, `hline()`, `vline()`
- helpers texte `text()` et `text_right()`

Les helpers texte acceptent désormais un paramètre optionnel `font_name`, ce qui permet de conserver une API simple tout en autorisant des variations typographiques localisées.

---

### 4.2 pages/

Chaque page est un module indépendant :

- dots
- mois gauche
- mois droite
- daily

👉 Chaque page est testable séparément.

---

### 4.3 assembleurs

- build_demo : test rapide
- build_month : mois complet
- build_year : carnet complet

👉 Les assembleurs orchestrent les pages.

---

### 4.4 Grille

Principe fondamental :

- grille 5 mm
- alignement strict
- aucune approximation

👉 garantit cohérence et lisibilité.

---

## 5. Daily page actuelle

La daily page actuellement retenue suit la logique suivante :

- zone **PRIORITÉS** en haut avec **4 cases**
- colonne **TEMPS** à gauche
- colonne **TÂCHES** à droite avec **5 cases**
- zone **NOTES** positionnée dans la partie droite basse
- zone **REPORT / À MIGRER** remontée dans la partie gauche basse
- page pointillée libre en seconde page du couple daily

👉 Cette structure correspond à la version ajustée après relecture visuelle et annotations sur PDF.

---

## 6. Hyperliens PDF

Le système utilise :

- bookmarkPage → ancrages
- linkRect → zones cliquables

👉 Permet une navigation rapide dans le carnet.

---

## 7. État actuel

Le projet permet déjà :

- génération des pages validées
- génération d’un mois complet
- génération d’un carnet annuel (démo)
- navigation interne fonctionnelle
- daily layout mis à jour selon les derniers retours visuels

---

## 8. Évolutions prévues

- navigation vers le mois courant
- index enrichi
- génération 365 jours
- amélioration ergonomique tablette

---

## 9. Principe fondamental

👉 on ne génère pas un PDF
👉 on construit un système

---

## 10. Utilisation

```bash
pip install reportlab
python build_year.py
```

Sortie :

```bash
output/year_demo.pdf
```

---

## 11. Conclusion

Ce projet transforme le bullet journal en :

- système structuré
- outil navigable
- support de travail quotidien

👉 objectif : simplicité, stabilité, efficacité
