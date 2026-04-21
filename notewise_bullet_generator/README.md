# Notewise Bullet Generator

Générateur Python/ReportLab pour produire le carnet bullet journal numérique.

## État actuel

Socle prêt pour :
- fond en dots 5 mm
- page mensuelle gauche validée
- page daily validée
- page dots seule
- architecture modulaire

## Dépendance

```bash
pip install reportlab
```

## Lancement

```bash
python build_demo.py
```

Cela génère dans `output/` :
- `dots_page.pdf`
- `month_left_validated.pdf`
- `daily_validated.pdf`

## Architecture

- `core/` : géométrie, configuration, primitives de dessin
- `pages/` : générateurs de pages
- `build_demo.py` : démonstrateur

## Prochaine étape

Ajouter :
- page mensuelle droite
- semestres
- index
- collections fixes
- assembleur annuel complet
