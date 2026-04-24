# Notewise Bullet Generator

## Statut du projet

Projet considéré comme **clos provisoirement**.

Pour reprendre le projet dans plusieurs mois, lire d’abord :

```text
PROJECT_CLOSURE.md
```

Puis, si nécessaire :

```text
DOCUMENTATION.md
build_year.py
```

---

## 1. Objectif du projet

Ce projet vise à construire un **bullet journal numérique complet**, optimisé pour une utilisation sur tablette avec stylet, en particulier dans Notewise.

L’objectif n’est pas simplement de produire un PDF, mais de créer un **outil de travail quotidien structuré, rapide, robuste et navigable**, équivalent ou supérieur à un bullet journal papier.

Le PDF porte la structure. Notewise sert à écrire, annoter et naviguer.

---

## 2. Philosophie du bullet journal

### 2.1 Stabilité des repères

Contrairement à un bullet papier :

- les pages fixes ne bougent jamais ;
- les emplacements sont constants ;
- la navigation devient réflexe ;
- l’utilisateur ne redessine pas la structure.

Cela réduit fortement la charge cognitive.

### 2.2 Séparation structure / contenu

**Structure fixe générée :**

- index ;
- pages semestres ;
- page MOIS ;
- section JOURS ;
- pages mensuelles ;
- collections ;
- onglets latéraux ;
- hyperliens internes.

**Zone vivante écrite au stylet :**

- daily ;
- notes ;
- reports ;
- réflexions ;
- contenus libres.

### 2.3 Navigation rapide

Chaque page importante donne accès aux sections principales :

- INDEX ;
- MOIS ;
- JOURS ;
- PARKING ;
- PRIÈRES ;
- LIBRE.

Les onglets latéraux sont maintenant stabilisés visuellement :

- fond discret ;
- coins arrondis ;
- contraste légèrement renforcé ;
- texte mieux centré ;
- onglet actif mis en évidence selon la section courante.

---

## 3. Choix de Notewise

Notewise a été retenu pour :

- la qualité de l’écriture au stylet ;
- la fluidité ;
- la bonne gestion de PDF volumineux ;
- le support des hyperliens internes.

Le projet ne dépend pas d’une logique interne de Notewise : le PDF doit rester autonome.

---

## 4. Architecture technique

Structure actuelle :

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

### Fichier principal

Le générateur annuel complet est actuellement :

```text
build_year.py
```

C’est le fichier à relire en priorité pour comprendre l’état réel du générateur annuel.

Les fichiers dans `pages/` correspondent à des briques ou versions validées antérieures. La daily réellement utilisée par le PDF annuel est celle codée dans `build_year.py`.

---

## 5. Conventions graphiques

Le projet repose sur :

- format A5 ;
- marge 10 mm ;
- grille 5 mm ;
- fond pointillé ;
- usage de `gx()` et `gy()` ;
- helpers `draw_dots()`, `hline()`, `vline()` ;
- helpers texte `text()` et `text_right()` ;
- ReportLab pour la génération PDF.

Constantes principales dans `core/config.py` :

```python
PAGE_SIZE = A5
MARGIN_MM = 10
GRID_STEP_MM = 5
FONT = "Helvetica"
FONT_SIZE = 8
```

---

## 6. État fonctionnel validé

### 6.1 Section JOURS

La section **JOURS** est validée.

Elle comprend 4 pages trimestrielles :

- Janvier à Mars ;
- Avril à Juin ;
- Juillet à Septembre ;
- Octobre à Décembre.

Chaque mois est affiché comme mini-calendrier.

Chaque case contient :

- le numéro du jour ;
- le jour de semaine abrégé.

Les samedis et dimanches ont un fond gris discret.

Quand la daily existe, la case entière du jour est cliquable.

### 6.2 Daily page

La daily actuelle contient :

- Date ;
- Jour ;
- PRIORITÉS avec 4 cases ;
- TEMPS ;
- TÂCHES avec 5 cases ;
- NOTES ;
- REPORT / À MIGRER ;
- INDEXER ? ;
- Entrée index ;
- une seconde page pointillée libre.

Le libellé `NOTES` a été abaissé pour l’éloigner du dernier carré de tâches.

Position actuelle dans `build_year.py` :

```python
text(c, gx(mid_col + 1), gy(notes_label_row) + 1 - 3 * mm, "NOTES")
```

### 6.3 Collections

Collections prévues :

- Parking ;
- Parking — suite ;
- Achats ;
- Grandes idées ;
- Prières 1 à 4 ;
- Libre 1 à 6.

Les collections restent volontairement sobres.

---

## 7. Utilisation

Depuis le dossier :

```text
notewise_bullet_generator/
```

installer la dépendance :

```bash
pip install reportlab
```

lancer le générateur annuel :

```bash
python build_year.py
```

Sorties actuelles :

```text
output/year_generic_test.pdf
output/year_2026_test.pdf
```

---

## 8. Mode test actuel

Le projet est encore configuré en mode test annuel :

```python
DEFAULT_TEST_DAILY_COUNT = 14
```

Conséquence :

- les pages fixes sont générées ;
- les pages JOURS couvrent toute l’année ;
- seules les 14 premières daily existent ;
- une génération annuelle complète nécessitera ensuite 365 daily.

Avec 14 daily, le PDF annuel de test comporte 75 pages.

Une version complète avec 365 daily ferait environ 777 pages.

---

## 9. Points de vigilance

Avant toute reprise :

1. lire `PROJECT_CLOSURE.md` ;
2. lancer `python build_year.py` ;
3. ouvrir `output/year_2026_test.pdf` dans Notewise ;
4. tester les liens ;
5. tester la fluidité ;
6. tester l’écriture au stylet ;
7. décider seulement ensuite d’une éventuelle génération 365 jours.

Ne pas refactorer brutalement `build_year.py`. Le fichier est long, mais il représente l’état consolidé validé.

---

## 10. Pistes futures non prioritaires

- génération complète 365 jours ;
- année paramétrable ;
- nombre de daily paramétrable ;
- amélioration de la page MOIS ;
- structuration légère de certaines collections ;
- extraction progressive de `build_year.py` en modules ;
- tests automatiques simples : génération sans erreur, nombre de pages, existence de bookmarks.

---

## 11. Principe fondamental

On ne génère pas seulement un PDF.

On construit un système de travail quotidien :

- stable ;
- sobre ;
- navigable ;
- adapté au stylet ;
- suffisamment simple pour être utilisé réellement.
