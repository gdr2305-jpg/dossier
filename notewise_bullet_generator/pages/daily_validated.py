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
    hline(c, gx(0), gy(prio_top), gx(cols))
    text(c, gx(0), gy(prio_top) + 3, "PRIORITÉS")

    priority_line_rows = [prio_top - 1, prio_top - 3, prio_top - 5, prio_top - 7]
    priority_box_rows = [r - 1 for r in priority_line_rows]
    prio_bottom_line = prio_top - 9
    for line_r, box_r in zip(priority_line_rows, priority_box_rows):
        c.rect(gx(0), gy(box_r) - 4, 10, 10)
        hline(c, gx(2), gy(line_r), gx(cols))
    hline(c, gx(0), gy(prio_bottom_line), gx(cols))

    sep_row = prio_bottom_line - 2
    mid_col = 11
    hline(c, gx(0), gy(sep_row), gx(cols))
    text(c, gx(0), gy(sep_row) + 3, "TEMPS")
    text(c, gx(mid_col + 1), gy(sep_row) + 3, "TÂCHES")

    time_hours = list(range(8, 23))
    time_start_row = sep_row - 2
    for i, h in enumerate(time_hours):
        r = time_start_row - i
        text(c, gx(0), gy(r) - 3, f"{h:02d}h")
        hline(c, gx(3), gy(r), gx(mid_col - 1))

    task_line_rows = [sep_row - 1, sep_row - 3, sep_row - 5, sep_row - 7, sep_row - 9]
    task_box_rows = [r - 1 for r in task_line_rows]
    for line_r, box_r in zip(task_line_rows, task_box_rows):
        c.rect(gx(mid_col + 2), gy(box_r) - 4, 10, 10)
        hline(c, gx(mid_col + 4), gy(line_r), gx(cols))

    notes_divider_row = task_line_rows[-1] - 3
    notes_label_row = notes_divider_row + 1
    report_label_row = notes_divider_row - 5
    bottom_split_row = 2

    vline(c, gx(mid_col), gy(sep_row), gy(bottom_split_row))
    hline(c, gx(mid_col), gy(notes_divider_row), gx(cols))

    text(c, gx(mid_col + 1), gy(notes_label_row) + 3, "NOTES")
    text(c, gx(0), gy(report_label_row) + 3, "REPORT / À MIGRER")

    text(c, gx(0), gy(1), "INDEXER ? [ ] oui")
    text(c, gx(8), gy(1), "Entrée index : ____________________")

    c.showPage()

    draw_dots(c)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX  MOIS  PARKING  PRIÈRES")

    c.showPage()
    c.save()
