from reportlab.pdfgen import canvas
from pathlib import Path

from core.config import PAGE_SIZE, PAGE_WIDTH, MARGIN
from core.draw import draw_dots, hline, vline
from core.geometry import gx, gy
from core.grid import grid_size
from core.text import text, text_right


def build(output_path: str | Path) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)
    cols, rows = grid_size()

    draw_dots(c)

    top = rows
    text(c, gx(0), gy(top) + 3, "Date : ____________________")
    text(c, gx(10), gy(top) + 3, "Page : ____")
    text(c, gx(0), gy(top - 2) + 3, "Jour : ____________________")
    text_right(c, PAGE_WIDTH - MARGIN, gy(top) + 3, "INDEX  MOIS  PARKING  PRIÈRES")

    prio_top = top - 4
    prio_bottom = prio_top - 6
    hline(c, gx(0), gy(prio_top), gx(cols))
    text(c, gx(0), gy(prio_top) + 3, "PRIORITÉS")

    for r in [prio_top - 2, prio_top - 4]:
        c.rect(gx(0), gy(r) - 4, 10, 10)
        hline(c, gx(2), gy(r), gx(cols))

    sep_row = prio_bottom - 2
    mid_col = 11
    hline(c, gx(0), gy(sep_row), gx(cols))
    text(c, gx(0), gy(sep_row) + 3, "TEMPS")
    text(c, gx(mid_col + 1), gy(sep_row) + 3, "TÂCHES")

    time_hours = list(range(8, 23))
    time_start_row = sep_row - 2
    last_time_row = time_start_row - (len(time_hours) - 1)

    for i, h in enumerate(time_hours):
        r = time_start_row - i
        text(c, gx(0), gy(r) - 3, f"{h:02d}h")
        hline(c, gx(3), gy(r), gx(mid_col - 1))

    task_rows = [sep_row - 2, sep_row - 6, sep_row - 10, sep_row - 14]
    for r in task_rows:
        c.rect(gx(mid_col + 2), gy(r) - 4, 10, 10)
        hline(c, gx(mid_col + 4), gy(r), gx(cols))

    notes_top = last_time_row - 2
    vline(c, gx(mid_col), gy(sep_row), gy(notes_top))
    hline(c, gx(0), gy(notes_top), gx(cols))
    text(c, gx(0), gy(notes_top) + 3, "NOTES")

    report_row = notes_top - 3
    hline(c, gx(0), gy(report_row), gx(cols))
    text(c, gx(0), gy(report_row) + 3, "REPORT / À MIGRER")

    text(c, gx(0), gy(1), "INDEXER ? [ ] oui")
    text(c, gx(8), gy(1), "Entrée index : ____________________")

    c.showPage()

    draw_dots(c)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX  MOIS  PARKING  PRIÈRES")

    c.showPage()
    c.save()
