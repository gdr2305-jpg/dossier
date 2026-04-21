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


HEADER_LINKS = [
    ("INDEX", "INDEX"),
    ("MOIS", "MONTHS"),
    ("PARKING", "PARKING"),
    ("PRIÈRES", "PRAYERS"),
]


def draw_header_links(c, rows: int, right_x: float | None = None) -> None:
    """Dessine des liens en haut à droite, avec zones cliquables simples."""
    y = gy(rows) + 3
    x = right_x if right_x is not None else PAGE_WIDTH - MARGIN

    # On dessine de droite à gauche pour garder un alignement robuste.
    for label, target in reversed(HEADER_LINKS):
        width_guess = max(26, len(label) * 4.8)
        left = x - width_guess
        text(c, left, y, label)
        c.linkRect("", target, (left, y - 2, x, y + 9), relative=0, thickness=0)
        x = left - 6


def add_index_entry(c, label: str, row: int, target: str) -> None:
    y = gy(row) - 3
    x1 = gx(0)
    x2 = gx(14)
    text(c, x1, y, label)
    c.linkRect("", target, (x1, y - 2, x2, y + 9), relative=0, thickness=0)



def render_simple_index_page(c, title: str = "INDEX") -> None:
    cols, rows = grid_size()
    c.bookmarkPage("INDEX")

    draw_dots(c)
    text(c, gx(0), gy(rows) + 3, title)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX")

    lines = [
        ("Année / Semestres", "SEM1"),
        ("Mois", "MONTHS"),
        ("Parking", "PARKING"),
        ("Achats", "ACHATS"),
        ("Grandes idées", "IDEAS"),
        ("Prières", "PRAYERS"),
    ]
    start_row = rows - 4
    for i, (value, target) in enumerate(lines):
        add_index_entry(c, value, start_row - 2 * i, target)



def render_simple_notes_page(c, header_left: str, bookmark: str | None = None) -> None:
    cols, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)
    draw_dots(c)
    text(c, gx(0), gy(rows) + 3, header_left)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX")
    c.linkRect("", "INDEX", (PAGE_WIDTH - MARGIN - 26, gy(rows) + 1, PAGE_WIDTH - MARGIN, gy(rows) + 11), relative=0, thickness=0)



def render_month_page(c, month_name: str, start_day: int, day_count: int, bookmark: str | None = None, include_months_bookmark: bool = False) -> None:
    cols, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)
    if include_months_bookmark:
        c.bookmarkPage("MONTHS")

    draw_dots(c)

    text(c, gx(0), gy(rows) + 3, f"Mois de : {month_name}")
    draw_header_links(c, rows)

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



def render_daily(c, page1_bookmark: str | None = None, page2_bookmark: str | None = None) -> None:
    cols, rows = grid_size()

    # page 1
    if page1_bookmark:
        c.bookmarkPage(page1_bookmark)
    draw_dots(c)

    top = rows
    text(c, gx(0), gy(top) + 3, "Date : ____________________")
    text(c, gx(10), gy(top) + 3, "Page : ____")
    text(c, gx(0), gy(top - 2) + 3, "Jour : ____________________")
    draw_header_links(c, rows)

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
    if page2_bookmark:
        c.bookmarkPage(page2_bookmark)
    draw_dots(c)
    draw_header_links(c, rows)



def build(output_path: str | Path, daily_count: int = 14) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)

    # ---- Pages fixes minimales provisoires ----
    render_simple_index_page(c, "INDEX")
    c.showPage()

    render_simple_notes_page(c, "Abréviations / Conventions")
    c.showPage()

    render_simple_notes_page(c, "Semestre 1", bookmark="SEM1")
    c.showPage()

    render_simple_notes_page(c, "Semestre 2", bookmark="SEM2")
    c.showPage()

    # ---- 12 mois ----
    for idx, month_name in enumerate(MONTH_NAMES):
        bookmark_left = f"MONTH_{idx+1:02d}_L"
        bookmark_right = f"MONTH_{idx+1:02d}_R"
        render_month_page(
            c,
            month_name,
            start_day=1,
            day_count=15,
            bookmark=bookmark_left,
            include_months_bookmark=(idx == 0),
        )
        c.showPage()
        render_month_page(c, month_name, start_day=16, day_count=16, bookmark=bookmark_right)
        c.showPage()

    # ---- Collections fixes provisoires ----
    collections = [
        ("Parking", "PARKING"),
        ("Achats", "ACHATS"),
        ("Grandes idées", "IDEAS"),
        ("Prières 1", "PRAYERS"),
        ("Prières 2", None),
        ("Prières 3", None),
        ("Prières 4", None),
    ]
    for name, bookmark in collections:
        render_simple_notes_page(c, name, bookmark=bookmark)
        c.showPage()

    # ---- Dailies de démonstration ----
    for i in range(daily_count):
        render_daily(c, page1_bookmark=f"DAILY_{i+1:03d}_A", page2_bookmark=f"DAILY_{i+1:03d}_B")
        c.showPage()
        c.showPage()

    c.save()


if __name__ == "__main__":
    output = Path("output")
    output.mkdir(exist_ok=True)
    build(output / "year_demo.pdf", daily_count=14)
    print("Carnet annuel de démonstration généré dans ./output/year_demo.pdf")
