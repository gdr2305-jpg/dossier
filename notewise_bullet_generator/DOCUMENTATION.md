# Documentation – Notewise Bullet Generator

## Statut documentaire

Projet considéré comme **clos provisoirement**.

Document de reprise prioritaire :

```text
PROJECT_CLOSURE.md
```

Le présent fichier décrit la logique fonctionnelle et technique du projet.

---

## 1. Vision du projet

Ce projet ne vise pas à générer un simple PDF.

Il vise à construire un **système de travail quotidien** : un bullet journal numérique qui structure la pensée, réduit la friction et permet de retrouver rapidement les pages utiles.

Le principe central est le suivant :

> Le PDF porte la structure. Notewise sert à écrire, annoter et naviguer.

L’objectif est donc de produire un PDF autonome, stable et hyperlié.

---

## 2. Philosophie du bullet journal

### 2.1 Stabilité absolue

Dans un bullet papier :

- les pages changent ;
- l’organisation dérive ;
- l’index demande un entretien manuel ;
- la navigation dépend du feuilletage.

Ici :

- les pages fixes sont générées ;
- les emplacements sont stables ;
- les sections principales sont accessibles par liens ;
- l’utilisateur écrit au lieu de reconstruire la structure.

### 2.2 Structure vs usage

Le système sépare :

#### Structure générée

- index ;
- pages semestres ;
- page MOIS ;
- pages JOURS ;
- pages mensuelles ;
- collections ;
- onglets latéraux ;
- hyperliens.

#### Usage écrit

- daily ;
- notes ;
- décisions ;
- reports ;
- pages libres ;
- contenus personnels.

### 2.3 Navigation comme cœur du système

La navigation fixe contient :

- INDEX ;
- MOIS ;
- JOURS ;
- PARKING ;
- PRIÈRES ;
- LIBRE.

Les onglets latéraux ont été stabilisés :

- fond discret ;
- coins arrondis ;
- contraste légèrement renforcé ;
- texte mieux centré ;
- onglet actif selon la section courante.

### 2.4 Minimalisme fonctionnel

Le design repose sur :

- une grille 5 mm ;
- peu de texte ;
- pas d’ornement inutile ;
- couleur uniquement quand elle aide la navigation ou la lecture.

Objectif : écrire vite, lire vite, décider vite.

---

## 3. Pourquoi Notewise

Notewise a été choisi pour :

- écriture fluide au stylet ;
- bonne gestion des PDF ;
- support des hyperliens internes ;
- navigation rapide.

Notewise n’est pas utilisé comme outil de structuration.

La structure est dans le PDF.

---

## 4. Architecture technique

### 4.1 Structure du dossier

```text
notewise_bullet_generator/
├── core/
│   ├── config.py
│   ├── geometry.py
│   ├── grid.py
│   ├── draw.py
│   └── text.py
├── pages/
│   ├── dots_page.py
│   ├── month_left_validated.py
│   ├── month_right_validated.py
│   └── daily_validated.py
├── build_demo.py
├── build_month.py
├── build_year.py
├── README.md
├── DOCUMENTATION.md
└── PROJECT_CLOSURE.md
```

### 4.2 Core

Le dossier `core/` contient les briques communes :

- `config.py` : format, marges, grille, police ;
- `geometry.py` : fonctions `gx()` et `gy()` ;
- `grid.py` : calcul du nombre de colonnes et lignes ;
- `draw.py` : fond pointillé et traits ;
- `text.py` : helpers texte.

Constantes graphiques principales :

```python
PAGE_SIZE = A5
MARGIN_MM = 10
GRID_STEP_MM = 5
DOT_RADIUS = 0.5
LINE_WIDTH = 0.8
FONT = "Helvetica"
FONT_SIZE = 8
```

### 4.3 Pages

Le dossier `pages/` contient des pages ou briques validées antérieurement :

- page pointillée ;
- page mensuelle gauche ;
- page mensuelle droite ;
- daily validée initiale.

Point important : la daily actuellement utilisée dans le PDF annuel est celle codée dans `build_year.py`, car elle a été ajustée après les derniers retours visuels.

### 4.4 Assembleurs

- `build_demo.py` génère quelques fichiers de test isolés ;
- `build_month.py` génère un mois validé ;
- `build_year.py` génère le carnet annuel de test.

`build_year.py` est actuellement le fichier central du projet.

Il orchestre :

- l’index ;
- les pages semestres ;
- la page MOIS ;
- la section JOURS ;
- les pages mensuelles ;
- les collections ;
- les pages daily ;
- les onglets ;
- les bookmarks ;
- les liens.

---

## 5. Générateur annuel `build_year.py`

### 5.1 Constantes importantes

Constantes principales :

```python
FREE_PAGES_COUNT = 6
DEFAULT_TEST_DAILY_COUNT = 14
```

Constantes de navigation :

```python
SIDE_TABS = [
    ("INDEX", "INDEX"),
    ("MOIS", "MONTHS"),
    ("JOURS", "DAYS"),
    ("PARKING", "PARKING"),
    ("PRIÈRES", "PRAYERS"),
    ("LIBRE", "LIBRE"),
]
```

Trimestres JOURS :

```python
QUARTERS = [
    ("JOURS_T1", [1, 2, 3], "Janvier à Mars"),
    ("JOURS_T2", [4, 5, 6], "Avril à Juin"),
    ("JOURS_T3", [7, 8, 9], "Juillet à Septembre"),
    ("JOURS_T4", [10, 11, 12], "Octobre à Décembre"),
]
```

### 5.2 Fonctions structurantes

Fonctions importantes :

- `draw_side_tabs()` : dessine les onglets latéraux ;
- `active_tab_for_notes_page()` : détermine l’onglet actif sur les pages de collection ;
- `render_simple_index_page()` : page INDEX ;
- `render_months_index_page()` : page MOIS ;
- `render_days_quarter_page()` : pages JOURS ;
- `render_month_page()` : pages mensuelles ;
- `render_daily()` : couple daily ;
- `compute_page_map()` : calcul des pages et bookmarks ;
- `build()` : orchestration générale.

---

## 6. Structure du PDF annuel de test

Avec `DEFAULT_TEST_DAILY_COUNT = 14`, le PDF annuel de test comporte 75 pages.

Structure :

1. INDEX ;
2. Abréviations / Conventions ;
3. Semestre 1 ;
4. Semestre 2 ;
5. MOIS ;
6-9. JOURS, en 4 pages trimestrielles ;
10-33. pages mensuelles, 2 pages par mois ;
34-35. Parking ;
36. Achats ;
37. Grandes idées ;
38-41. Prières ;
42-47. pages libres ;
48-75. 14 couples daily.

---

## 7. Daily page – état courant

### 7.1 Structure générale

La page daily contient :

- Date ;
- Jour ;
- PRIORITÉS avec 4 cases ;
- TEMPS ;
- TÂCHES avec 5 cases ;
- NOTES ;
- REPORT / À MIGRER ;
- INDEXER ? ;
- Entrée index.

Chaque daily est un couple de pages :

1. page structurée ;
2. page pointillée libre.

### 7.2 Position finale du libellé NOTES

Le libellé `NOTES` a été abaissé pour ne pas être trop proche du dernier carré de tâches.

Position actuelle dans `build_year.py` :

```python
text(c, gx(mid_col + 1), gy(notes_label_row) + 1 - 3 * mm, "NOTES")
```

Cette position est le dernier ajustement visuel validé.

### 7.3 Doctrine de correction visuelle

Les ajustements de la daily ont été faits à partir de tests PDF.

Doctrine à conserver :

- ne pas modifier plusieurs zones à la fois ;
- générer une page daily seule si possible ;
- valider visuellement ;
- seulement ensuite appliquer au dépôt.

---

## 8. Section JOURS

### 8.1 Problème traité

La section JOURS sert à retrouver rapidement une daily après avoir quitté la page courante.

C’est un hub de navigation stable.

### 8.2 Structure retenue

La section JOURS est composée de 4 pages trimestrielles :

- Janvier à Mars ;
- Avril à Juin ;
- Juillet à Septembre ;
- Octobre à Décembre.

Chaque page affiche 3 mois.

Chaque mois est représenté sous forme de mini-calendrier.

Chaque case affiche :

- numéro du jour ;
- jour de semaine abrégé.

La case entière est cliquable quand la daily existe.

### 8.3 Style validé

Style retenu :

- panneaux légèrement teintés ;
- titre bleu-grisé ;
- en-têtes différenciés ;
- week-ends grisés ;
- lisibilité prioritaire.

---

## 9. Collections

Collections actuelles :

- Parking ;
- Parking — suite ;
- Achats ;
- Grandes idées ;
- Prières 1 ;
- Prières 2 ;
- Prières 3 ;
- Prières 4 ;
- Libre 1 à Libre 6.

Les collections sont volontairement peu structurées.

Raison : éviter d’enfermer l’usage avant test réel.

---

## 10. Hyperliens PDF

Le système utilise ReportLab :

```python
bookmarkPage(...)
linkRect(...)
```

`bookmarkPage()` crée les cibles internes.

`linkRect()` crée les zones cliquables.

Dans la section JOURS, `linkRect()` est appliqué à la totalité de la case de jour, pas seulement au texte.

---

## 11. Usage

Depuis le dossier :

```text
notewise_bullet_generator/
```

installer ReportLab :

```bash
pip install reportlab
```

lancer :

```bash
python build_year.py
```

Sorties actuelles :

```text
output/year_generic_test.pdf
output/year_2026_test.pdf
```

---

## 12. État actuel et limites

Le projet permet :

- génération du carnet annuel de test ;
- navigation interne ;
- onglets actifs ;
- section JOURS ;
- pages mensuelles ;
- collections ;
- daily layout ajusté.

Limite actuelle :

```python
DEFAULT_TEST_DAILY_COUNT = 14
```

Donc seules les 14 premières daily existent dans la génération de test.

Pour une génération annuelle complète, il faudra générer 365 daily.

Estimation :

- environ 47 pages fixes ;
- 730 pages daily ;
- environ 777 pages au total.

À tester dans Notewise avant validation.

---

## 13. Reprise future recommandée

Ordre recommandé :

1. lire `PROJECT_CLOSURE.md` ;
2. lire `README.md` ;
3. ouvrir `build_year.py` ;
4. lancer `python build_year.py` ;
5. ouvrir `output/year_2026_test.pdf` dans Notewise ;
6. vérifier les onglets ;
7. vérifier JOURS ;
8. vérifier une daily ;
9. décider ou non du passage à 365 daily.

---

## 14. Refactor éventuel

Ne pas refactorer globalement au redémarrage.

Si le projet reprend, extractions possibles mais seulement progressivement :

- `pages/days_index.py` ;
- `pages/year_daily.py` ;
- `core/theme.py` ;
- `core/navigation.py` ;
- module dédié au calcul `page_map`.

Chaque extraction doit être suivie d’un test PDF.

---

## 15. Tests utiles à ajouter un jour

Tests automatiques possibles :

- génération sans exception ;
- nombre de pages attendu ;
- existence des bookmarks principaux ;
- cohérence de `compute_page_map()` ;
- présence des 12 mois ;
- nombre de daily générées ;
- absence de liens vers des bookmarks inexistants dans la version complète.

---

## 16. Roadmap non prioritaire

Pistes futures :

- génération complète 365 jours ;
- année paramétrable ;
- nombre de daily paramétrable ;
- amélioration de la page MOIS ;
- structuration légère des collections ;
- tests automatiques ;
- extraction progressive de `build_year.py`.

---

## 17. Conclusion

Le projet est dans un état cohérent, stable et reprenable.

La priorité, lors d’une reprise, sera de tester l’usage réel dans Notewise avant d’ajouter des fonctionnalités.

Le principe à conserver :

> simplicité, stabilité, navigation, écriture au stylet.
