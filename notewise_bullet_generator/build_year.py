from pathlib import Path
from reportlab.pdfgen import canvas

from core.config import PAGE_SIZE
from core.draw import draw_dots, hline, vline
from core.geometry import gx, gy
from core.grid import grid_size
from core.text import text, text_right
from core.config import PAGE_WIDTH, MARGIN


MONTH_NAMES = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre",
]


def render_simple_index_page(c, title: str = "INDEX") -> None:
    cols, rows = grid_size()
    draw_dots(c)
    text(c, gx(0), gy(rows) + 3, title)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX")

    # repères simples, à affiner ensuite
    lines = [
        "Année / Semestres",
        "Mois",
        "Parking",
        "Achats",
        "Grandes idées",
        "Prières",
    ]
    start_row = rows - 4
    for i, value in enumerate(lines):
        text(c, gx(0), gy(start_row - 2 * i) - 3, value)



def render_simple_notes_page(c, header_left: str, header_right: str = "INDEX") -> None:
    cols, rows = grid_size()
    draw_dots(c)
    text(c, gx(0), gy(rows) + 3, header_left)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, header_right)



def render_month_page(c, month_name: str, start_day: int, day_count: int) -> None:
    cols, rows = grid_size()

    draw_dots(c)

    text(c, gx(0), gy(rows) + 3, f"Mois de : {month_name}")
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX  MOIS  PARKING  PRIÈRES")

    top_content_row = rows - 2
    bottom_boundary_row = top_content_row - day_count * 2

    for k in range(day_count + 1):
        r = top_content_row - 2 * k
        hline(c, gx(0), gy(r), gx(cols))

    hour_cols = [2 + i * 3 for i in range(7)]
    hours = ["8h", "10h", "12h", "14h", "16h", "18h", "20h"]

    for col, hour in zip(hour_cols, hours):
        vline(c, gx(col), gy(bottom_boundary_row), gy(top_content_row))
        text(c, gx(col) - 6, gy(top_content_row) + 6, hour)

    for i in range(day_count):
        number_row = top_content_row - 1 - 2 * i
        text(c, gx(0), gy(number_row) - 3, str(start_day + i))



def render_daily(c) -> None:
    cols, rows = grid_size()

    # page 1
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

    # page 2
    draw_dots(c)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX  MOIS  PARKING  PRIÈRES")



def build(output_path: str | Path, daily_count: int = 14) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)

    # ---- Pages fixes minimales provisoires ----
    render_simple_index_page(c, "INDEX")
    c.showPage()

    render_simple_notes_page(c, "Abréviations / Conventions")
    c.showPage()

    render_simple_notes_page(c, "Semestre 1")
    c.showPage()

    render_simple_notes_page(c, "Semestre 2")
    c.showPage()

    # ---- 12 mois ----
    for month_name in MONTH_NAMES:
        render_month_page(c, month_name, start_day=1, day_count=15)
        c.showPage()
        render_month_page(c, month_name, start_day=16, day_count=16)
        c.showPage()

    # ---- Collections fixes provisoires ----
    for name in ["Parking", "Achats", "Grandes idées", "Prières 1", "Prières 2", "Prières 3", "Prières 4"]:
        render_simple_notes_page(c, name)
        c.showPage()

    # ---- Dailies de démonstration ----
    for _ in range(daily_count):
        render_daily(c)
        c.showPage()
        c.showPage()

    c.save()


if __name__ == "__main__":
    output = Path("output")
    output.mkdir(exist_ok=True)
    build(output / "year_demo.pdf", daily_count=14)
    print("Carnet annuel de démonstration généré dans ./output/year_demo.pdf")
