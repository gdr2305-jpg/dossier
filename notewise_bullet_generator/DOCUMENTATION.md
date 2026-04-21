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

## 5. Hyperliens PDF

Le système utilise :

- bookmarkPage → ancrages
- linkRect → zones cliquables

👉 permet une navigation interne

---

## 6. État actuel

Le projet permet :

- génération complète du carnet (démo)
- navigation interne
- pages validées visuellement

---

## 7. Roadmap

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

## 8. Principe fondamental

👉 On ne génère pas un PDF  
👉 On construit un système

---

## 9. Usage

```bash
pip install reportlab
python build_year.py
```

Sortie :

```bash
output/year_demo.pdf
```

---

## 10. Conclusion

Ce projet transforme un bullet journal en :

- outil structuré
- système navigable
- support de réflexion

👉 Objectif final : un outil simple, stable, puissant.
