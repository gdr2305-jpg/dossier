# Documentation – Notewise Bullet Generator

---

## 1. Vision du projet

Ce projet ne vise pas à générer un simple PDF.

👉 Il vise à construire un **système de travail quotidien**.

Un bullet journal numérique qui :
- structure la pensée
- réduit la friction
- accélère la prise de décision

---

## 2. Philosophie du bullet journal

### 2.1 Stabilité absolue

Dans un bullet papier :
- les pages changent
- l’organisation dérive

Ici :
- tout est fixé
- tout est stable
- tout est mémorisable

👉 Résultat : navigation instinctive

---

### 2.2 Structure vs usage

Le système sépare :

#### Structure (générée)
- index
- mois
- collections

#### Usage (écrit)
- daily
- notes
- décisions

👉 On ne perd plus de temps à organiser  
👉 On utilise directement

---

### 2.3 Navigation = cœur du système

Chaque page contient des liens vers :
- INDEX
- MOIS
- PARKING
- PRIÈRES

👉 Le carnet devient une **interface**

---

### 2.4 Minimalisme radical

Le design :
- grille 5 mm
- peu de texte
- pas d’ornement

👉 objectif :
- écrire vite
- lire vite
- décider vite

---

## 3. Pourquoi Notewise

### 3.1 Critères de choix

Notewise a été choisi pour :

- écriture fluide au stylet
- bonne gestion des PDF volumineux
- support des hyperliens
- navigation rapide

---

### 3.2 Positionnement

Notewise n’est pas :
👉 un outil de structuration

C’est :
👉 un moteur d’affichage et d’écriture

👉 Toute la structure est dans le PDF

---

### 3.3 Conséquence majeure

👉 Le PDF devient le système

Pas l’application.

---

## 4. Architecture technique

### 4.1 Core

Contient toute la logique :

- config : paramètres
- geometry : coordonnées
- grid : dimensions
- draw : primitives
- text : texte

👉 règle : aucun calcul graphique ailleurs

### 4.1.1 Conventions graphiques et techniques

Le projet repose sur des conventions stables :

- toute la géométrie passe par `gx()` et `gy()`
- la grille 5 mm est la référence unique
- les traits passent par `hline()` et `vline()`
- le fond pointillé passe par `draw_dots()`
- le texte passe par `text()` et `text_right()`

Les helpers texte acceptent désormais un paramètre optionnel `font_name`, afin de permettre des variations locales de police sans casser l’API commune.

---

### 4.2 Pages

Chaque page est indépendante :

- daily
- mois gauche
- mois droite
- dots

👉 testable isolément

---

### 4.3 Assembleurs

- build_demo → test
- build_month → mois
- build_year → carnet complet

---

### 4.4 Grille

Principe fondamental :

👉 tout est aligné sur une grille 5 mm

- aucune approximation
- aucune coordonnée libre

---

## 5. Daily page — état courant

La daily actuellement retenue est la version corrigée après plusieurs itérations visuelles.

### 5.1 Structure générale

La page daily se compose désormais de :

- une zone **PRIORITÉS** avec **4 cases**
- une colonne **TEMPS** à gauche
- une colonne **TÂCHES** à droite avec **5 cases**
- une zone **NOTES** dans la partie basse droite
- une zone **REPORT / À MIGRER** remontée dans la partie basse gauche
- une seconde page daily laissée volontairement pointillée et libre

### 5.2 Doctrine de correction visuelle

Les ajustements récents ont été validés à partir d’annotations directement sur PDF.

Règle d’interprétation retenue :

- annotations rouges : suppression
- annotations jaunes : ajout ou déplacement

Cette convention a servi à stabiliser la mise en page actuelle de la daily.

---

## 6. Hyperliens PDF

Le système utilise :

- bookmarkPage → ancrages
- linkRect → zones cliquables

👉 permet une navigation interne

---

## 7. État actuel

Le projet permet :

- génération complète du carnet (démo)
- navigation interne
- pages validées visuellement
- daily layout mis à jour selon les derniers retours
- cohérence rétablie entre layout daily et helpers texte

---

## 8. Roadmap

### Court terme

- navigation vers mois courant
- index enrichi

### Moyen terme

- génération 365 jours
- année dynamique

### Long terme

- système totalement paramétrable
- variantes de mise en page

---

## 9. Principe fondamental

👉 On ne génère pas un PDF  
👉 On construit un système

---

## 10. Usage

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

Ce projet transforme un bullet journal en :

- outil structuré
- système navigable
- support de réflexion

👉 Objectif final : un outil simple, stable, puissant.
