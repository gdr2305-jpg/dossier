# Clôture provisoire – Notewise Bullet Generator

Date de clôture provisoire : 2026-04-24

Ce document sert de **point de reprise rapide** si le projet est rouvert dans plusieurs mois.

---

## 1. Statut général

Le projet est considéré comme **clos provisoirement**.

La version actuelle est une **V1 stable de bullet journal numérique généré en Python + ReportLab**, pensée pour une utilisation dans Notewise sur tablette avec stylet.

Le système est suffisamment avancé pour être utilisé comme base réelle :

- format A5 ;
- grille 5 mm ;
- pages pointillées ;
- index ;
- pages semestres ;
- page MOIS ;
- section JOURS trimestrielle ;
- pages mensuelles ;
- collections ;
- pages daily ;
- onglets latéraux cliquables ;
- PDF hyperlié.

---

## 2. Fichier principal à relire en premier

Le fichier principal du générateur annuel est :

```text
notewise_bullet_generator/build_year.py
```

C’est actuellement le fichier le plus important du projet.

Il contient :

- les constantes de navigation ;
- les couleurs principales ;
- le rendu des onglets latéraux ;
- la page INDEX ;
- la page MOIS ;
- les pages JOURS ;
- les pages mensuelles ;
- les collections ;
- les pages daily ;
- le calcul de la carte des pages ;
- la fonction `build()` ;
- le bloc `if __name__ == "__main__"`.

---

## 3. Commande principale

Depuis le dossier :

```text
notewise_bullet_generator/
```

installer la dépendance :

```bash
pip install reportlab
```

puis lancer :

```bash
python build_year.py
```

Sorties générées actuellement :

```text
output/year_generic_test.pdf
output/year_2026_test.pdf
```

---

## 4. État du mode test

La constante actuelle est :

```python
DEFAULT_TEST_DAILY_COUNT = 14
```

Conséquence :

- les pages fixes de l’année sont générées ;
- les 4 pages JOURS couvrent toute l’année 2026 ;
- seules les 14 premières daily existent réellement ;
- les jours au-delà de ces 14 daily sont visuellement présents dans JOURS, mais ne pointent pas vers une daily existante.

Ce choix est volontaire pour le mode test.

Pour générer une version annuelle complète, il faudra passer à 365 daily, après test de performance dans Notewise.

---

## 5. Structure du PDF annuel de test

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
48-75. 14 couples daily, soit 2 pages par jour.

---

## 6. Choix validés fonctionnellement

### 6.1 Navigation

La navigation fixe validée contient :

- INDEX ;
- MOIS ;
- JOURS ;
- PARKING ;
- PRIÈRES ;
- LIBRE.

Les onglets sont présents sur les pages pertinentes et utilisent `linkRect()`.

L’onglet actif est mis en évidence selon la section :

- INDEX actif sur l’index ;
- MOIS actif sur la page MOIS ;
- JOURS actif sur les pages JOURS et daily ;
- PARKING actif sur les pages Parking ;
- PRIÈRES actif sur les pages Prières ;
- LIBRE actif sur les pages libres.

Les pages Achats et Grandes idées n’ont pas d’onglet dédié : elles restent accessibles depuis l’index.

### 6.2 Section JOURS

La section JOURS est validée.

Elle est organisée en 4 pages trimestrielles :

- Janvier à Mars ;
- Avril à Juin ;
- Juillet à Septembre ;
- Octobre à Décembre.

Chaque mois est affiché comme mini-calendrier.

Chaque case de jour contient :

- le numéro du jour ;
- l’abréviation du jour de semaine.

Les cases samedi et dimanche ont un fond gris discret.

### 6.3 Daily page

La page daily actuelle est validée dans son principe.

Elle contient :

- Date ;
- Jour ;
- PRIORITÉS ;
- TEMPS ;
- TÂCHES ;
- NOTES ;
- REPORT / À MIGRER ;
- INDEXER ? ;
- Entrée index.

Le libellé `NOTES` a été abaissé visuellement pour ne plus être trop proche du dernier carré de tâches.

Dans `build_year.py`, la position actuelle est :

```python
text(c, gx(mid_col + 1), gy(notes_label_row) + 1 - 3 * mm, "NOTES")
```

### 6.4 Collections

Collections actuellement prévues :

- Parking ;
- Parking — suite ;
- Achats ;
- Grandes idées ;
- Prières 1 ;
- Prières 2 ;
- Prières 3 ;
- Prières 4 ;
- Libre 1 à Libre 6.

Ces pages restent volontairement sobres : titre + grille pointillée.

---

## 7. Choix esthétiques validés

Le style est volontairement minimaliste :

- pas de décoration inutile ;
- fond pointillé régulier ;
- titres sobres ;
- couleurs faibles ;
- bleu-grisé pour la section JOURS ;
- gris discret pour les week-ends ;
- onglets arrondis avec fond actif.

Les onglets latéraux ont été améliorés selon cinq critères :

1. contraste légèrement augmenté ;
2. fond discret ;
3. coins arrondis ;
4. texte mieux centré ;
5. onglet courant mis en évidence.

---

## 8. Architecture du dépôt

Structure utile actuelle :

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

Remarque importante :

- `build_year.py` est aujourd’hui le générateur le plus complet ;
- les fichiers dans `pages/` correspondent à des briques ou versions validées antérieures ;
- la daily réellement utilisée dans le PDF annuel est celle codée dans `build_year.py`, pas directement `pages/daily_validated.py`.

---

## 9. Points de vigilance pour une reprise

### 9.1 Ne pas refactorer brutalement

Le fichier `build_year.py` est long, mais il fonctionne comme fichier consolidé.

Si le projet reprend, il faudra éviter un refactor global immédiat.

Doctrine recommandée :

1. corriger localement ;
2. tester visuellement ;
3. seulement ensuite extraire progressivement des modules si nécessaire.

### 9.2 Tester dans Notewise

Avant toute génération annuelle complète :

- générer un PDF de taille intermédiaire ;
- l’ouvrir dans Notewise ;
- tester la fluidité ;
- tester les liens ;
- tester l’écriture au stylet ;
- tester la navigation depuis les onglets.

### 9.3 Passage à 365 daily

Le passage à une vraie année complète impliquera environ :

- 47 pages fixes ;
- 365 × 2 pages daily ;
- soit environ 777 pages.

Ce n’est pas forcément problématique, mais cela doit être testé dans Notewise avant validation.

### 9.4 Cohérence des sorties

La documentation précédente mentionnait parfois `year_demo.pdf`.

L’état actuel réel de `build_year.py` produit :

```text
output/year_generic_test.pdf
output/year_2026_test.pdf
```

---

## 10. Prochaines actions possibles si reprise

Ordre recommandé :

1. lancer `python build_year.py` ;
2. ouvrir `output/year_2026_test.pdf` dans Notewise ;
3. vérifier les onglets ;
4. vérifier les pages JOURS ;
5. vérifier une daily ;
6. décider seulement ensuite si l’on passe à plus de daily.

Améliorations possibles, non prioritaires :

- génération complète 365 jours ;
- paramétrage de l’année ;
- paramétrage du nombre de daily ;
- amélioration de la page MOIS ;
- structuration légère de certaines collections ;
- extraction progressive de `build_year.py` en modules plus petits ;
- ajout de tests automatiques simples : génération sans erreur, nombre de pages, existence de bookmarks.

---

## 11. Principe à conserver

Le projet a été construit selon cette règle :

> Le PDF porte la structure. Notewise sert à écrire, annoter et naviguer.

Il ne faut donc pas dépendre de fonctions spécifiques ou fragiles d’une application de notes.

Le PDF doit rester autonome, stable et hyperlié.

---

## 12. Conclusion de clôture

Le projet est laissé dans un état cohérent et reprenable.

La priorité, lors d’une reprise, ne sera pas d’ajouter immédiatement des fonctionnalités, mais de :

1. regénérer le PDF ;
2. vérifier l’usage réel dans Notewise ;
3. décider si la V1 doit devenir une version annuelle complète.
