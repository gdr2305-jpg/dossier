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
- pages de navigation dédiées

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
- JOURS
- PARKING
- PRIÈRES

👉 Le carnet devient une **interface**

---

### 2.4 Minimalisme radical

Le design :
- grille 5 mm
- peu de texte
- pas d’ornement inutile
- couleur utilisée seulement quand elle aide vraiment la navigation

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

`build_year.py` orchestre désormais aussi les pages **JOURS** trimestrielles.

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

## 6. Section JOURS — choix retenu

### 6.1 Problème traité

La section **JOURS** répond à un besoin précis :

👉 retrouver rapidement une daily après avoir quitté la page courante, par exemple pour aller sur **Parking**.

Le système ne cherche pas à reproduire un “retour contextuel automatique” dépendant du lecteur PDF. Il met en place un **hub de navigation stable** vers les daily pages.

### 6.2 Structure retenue

Le choix validé est une adaptation du **prototype B** :

- **4 pages trimestrielles**
- blocs mensuels sous forme de mini-calendriers
- chaque case affiche :
  - le **numéro du jour**
  - le **jour de semaine abrégé**
- la **case entière** est cliquable
- chaque jour renvoie vers la **daily correspondante** lorsqu’elle existe

Trimestres retenus :

- Janvier à Mars
- Avril à Juin
- Juillet à Septembre
- Octobre à Décembre

### 6.3 Direction visuelle

La direction visuelle retenue est :

- sobre
- compacte mais confortable
- pensée pour un usage fréquent
- avec une **couleur bleu grisé discrète**

Utilisation de la couleur :

- titre de section **JOURS**
- panneaux de mois légèrement teintés
- en-têtes de blocs et zones de lecture légèrement différenciés
- sans surcharge décorative

### 6.4 Position dans le système

La navigation fixe contient désormais :

- INDEX
- MOIS
- JOURS
- PARKING
- PRIÈRES
- LIBRE

La section **JOURS** est donc une nouvelle composante centrale du système de navigation.

---

## 7. Hyperliens PDF

Le système utilise :

- `bookmarkPage` → ancrages
- `linkRect` → zones cliquables

👉 permet une navigation interne

Dans la section **JOURS**, `linkRect` est appliqué à la totalité de chaque case de jour, et non seulement au texte.

---

## 8. État actuel

Le projet permet :

- génération complète du carnet (démo)
- navigation interne
- pages validées visuellement
- daily layout mis à jour selon les derniers retours
- cohérence rétablie entre layout daily et helpers texte
- section **JOURS** trimestrielle codée dans `build_year.py`

### Point de vigilance actuel

Le code des pages **JOURS** est en place, mais l’état par défaut reste un état de test tant que :

- `DEFAULT_TEST_DAILY_COUNT = 14`

Dans cette configuration, seules les premières daily existent réellement dans la génération de démonstration. La structure annuelle des pages **JOURS** est prête, mais la couverture intégrale demande ensuite la génération des **365 daily**.

---

## 9. Roadmap

### Court terme

- navigation vers mois courant
- index enrichi
- test réel de confort des pages **JOURS** dans Notewise

### Moyen terme

- génération 365 jours
- année dynamique
- affinement visuel éventuel des pages **JOURS** après usage réel

### Long terme

- système totalement paramétrable
- variantes de mise en page

---

## 10. Principe fondamental

👉 On ne génère pas un PDF  
👉 On construit un système

---

## 11. Usage

```bash
pip install reportlab
python build_year.py
```

Sortie :

```bash
output/year_demo.pdf
```

---

## 12. Conclusion

Ce projet transforme un bullet journal en :

- outil structuré
- système navigable
- support de réflexion

👉 Objectif final : un outil simple, stable, puissant.
