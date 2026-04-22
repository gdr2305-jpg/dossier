from __future__ import annotations

from calendar import monthrange
from datetime import date, timedelta
from pathlib import Path

from reportlab.pdfgen import canvas

from core.config import MARGIN, PAGE_HEIGHT, PAGE_SIZE, PAGE_WIDTH
from core.draw import draw_dots, hline, vline
from core.geometry import gx, gy
from core.grid import grid_size
from core.text import text, text_right


MONTH_NAMES = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre",
]

DAY_NAMES = [
    "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
]

HEADER_LINKS = [
    ("INDEX", "INDEX"),
    ("MOIS", "MONTHS"),
    ("PARKING", "PARKING"),
    ("PRIÈRES", "PRAYERS"),
    ("LIBRE", "LIBRE"),
]

SIDE_TABS = [
    ("INDEX", "INDEX"),
    ("MOIS", "MONTHS"),
    ("PARKING", "PARKING"),
    ("PRIÈRES", "PRAYERS"),
    ("LIBRE", "LIBRE"),
]

FREE_PAGES_COUNT = 6
DEFAULT_TEST_DAILY_COUNT = 14


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


def draw_side_tabs(c) -> None:
    """Dessine des onglets latéraux sobres sur le côté droit."""
    cols, rows = grid_size()
    tab_left = gx(cols - 2.2)
    tab_right = PAGE_WIDTH
    tab_height = gy(2.2) - gy(0)
    top_start = gy(rows) - tab_height
    gap = gy(0.3) - gy(0)

    for idx, (label, target) in enumerate(SIDE_TABS):
        top = top_start - idx * (tab_height + gap)
        bottom = top - tab_height
        c.rect(tab_left, bottom, tab_right - tab_left, tab_height, stroke=1, fill=0)
        text(c, tab_left + 3, bottom + tab_height / 2 - 3, label)
        c.linkRect("", target, (tab_left, bottom, tab_right, top), relative=0, thickness=0)


def draw_page_number(c, page_number: int) -> None:
    text_right(c, PAGE_WIDTH - MARGIN, gy(0) - 8, f"p. {page_number}")


def add_index_entry(c, label: str, row: int, target: str) -> None:
    y = gy(row) - 3
    x1 = gx(0)
    x2 = gx(14)
    text(c, x1, y, label)
    c.linkRect("", target, (x1, y - 2, x2, y + 9), relative=0, thickness=0)



def render_simple_index_page(c, page_number: int, title: str = "INDEX") -> None:
    cols, rows = grid_size()
    c.bookmarkPage("INDEX")

    draw_dots(c)
    draw_side_tabs(c)
    text(c, gx(0), gy(rows) + 3, title)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX")

    lines = [
        ("Année / Semestres", "SEM1"),
        ("Mois", "MONTHS"),
        ("Parking", "PARKING"),
        ("Achats", "ACHATS"),
        ("Grandes idées", "IDEAS"),
        ("Prières", "PRAYERS"),
        ("Libre", "LIBRE"),
    ]
    start_row = rows - 4
    for i, (value, target) in enumerate(lines):
        add_index_entry(c, value, start_row - 2 * i, target)

    draw_page_number(c, page_number)



def render_months_index_page(c, page_number: int) -> None:
    cols, rows = grid_size()
    c.bookmarkPage("MONTHS")

    draw_dots(c)
    draw_side_tabs(c)
    text(c, gx(0), gy(rows) + 3, "MOIS")
    draw_header_links(c, rows)

    start_row = rows - 4
    left_targets = MONTH_NAMES[:6]
    right_targets = MONTH_NAMES[6:]

    for i, month_name in enumerate(left_targets):
        row = start_row - 2 * i
        target = f"MONTH_{i + 1:02d}_L"
        text(c, gx(0), gy(row) - 3, month_name)
        c.linkRect("", target, (gx(0), gy(row) - 5, gx(8), gy(row) + 8), relative=0, thickness=0)

    for i, month_name in enumerate(right_targets):
        row = start_row - 2 * i
        month_index = i + 7
        target = f"MONTH_{month_index:02d}_L"
        text(c, gx(9), gy(row) - 3, month_name)
        c.linkRect("", target, (gx(9), gy(row) - 5, gx(18), gy(row) + 8), relative=0, thickness=0)

    draw_page_number(c, page_number)



def render_simple_notes_page(c, page_number: int, header_left: str, bookmark: str | None = None) -> None:
    cols, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)
    draw_dots(c)
    draw_side_tabs(c)
    text(c, gx(0), gy(rows) + 3, header_left)
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX")
    c.linkRect("", "INDEX", (PAGE_WIDTH - MARGIN - 26, gy(rows) + 1, PAGE_WIDTH - MARGIN, gy(rows) + 11), relative=0, thickness=0)
    draw_page_number(c, page_number)



def render_month_page(
    c,
    page_number: int,
    month_name: str,
    start_day: int,
    day_count: int,
    bookmark: str | None = None,
) -> None:
    cols, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)

    draw_dots(c)
    draw_side_tabs(c)

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

    draw_page_number(c, page_number)



def render_daily(
    c,
    page_number_1: int,
    page_number_2: int,
    page1_bookmark: str | None = None,
    page2_bookmark: str | None = None,
    date_label: str | None = None,
    day_label: str | None = None,
) -> None:
    cols, rows = grid_size()

    # page 1
    if page1_bookmark:
        c.bookmarkPage(page1_bookmark)
    draw_dots(c)
    draw_side_tabs(c)

    top = rows
    date_value = date_label if date_label is not None else "____________________"
    day_value = day_label if day_label is not None else "____________________"
    text(c, gx(0), gy(top) + 3, f"Date : {date_value}")
    text(c, gx(10), gy(top) + 3, "Page : ____")
    text(c, gx(0), gy(top - 2) + 3, f"Jour : {day_value}")
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
    draw_page_number(c, page_number_1)

    c.showPage()

    # page 2
    if page2_bookmark:
        c.bookmarkPage(page2_bookmark)
    draw_dots(c)
    draw_side_tabs(c)
    draw_header_links(c, rows)
    draw_page_number(c, page_number_2)



def month_day_counts_for_year(year: int | None) -> list[int]:
    if year is None:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return [monthrange(year, month)[1] for month in range(1, 13)]



def split_month_day_count(day_count: int) -> tuple[int, int]:
    left = day_count // 2
    right = day_count - left
    return left, right



def iter_daily_labels(year: int | None, daily_count: int):
    if year is None:
        for _ in range(daily_count):
            yield None, None
        return

    current_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    produced = 0
    while current_date <= end_date and produced < daily_count:
        yield current_date.strftime("%d/%m/%Y"), DAY_NAMES[current_date.weekday()]
        current_date += timedelta(days=1)
        produced += 1



def build(
    output_path: str | Path,
    daily_count: int = DEFAULT_TEST_DAILY_COUNT,
    year: int | None = None,
    free_pages_count: int = FREE_PAGES_COUNT,
) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)
    page_number = 1

    # ---- Pages fixes ----
    render_simple_index_page(c, page_number, "INDEX")
    c.showPage()
    page_number += 1

    render_simple_notes_page(c, page_number, "Abréviations / Conventions")
    c.showPage()
    page_number += 1

    render_simple_notes_page(c, page_number, "Semestre 1", bookmark="SEM1")
    c.showPage()
    page_number += 1

    render_simple_notes_page(c, page_number, "Semestre 2", bookmark="SEM2")
    c.showPage()
    page_number += 1

    render_months_index_page(c, page_number)
    c.showPage()
    page_number += 1

    # ---- 12 mois ----
    month_day_counts = month_day_counts_for_year(year)
    for idx, (month_name, month_day_count) in enumerate(zip(MONTH_NAMES, month_day_counts), start=1):
        bookmark_left = f"MONTH_{idx:02d}_L"
        bookmark_right = f"MONTH_{idx:02d}_R"
        left_days, right_days = split_month_day_count(month_day_count)

        render_month_page(
            c,
            page_number,
            month_name,
            start_day=1,
            day_count=left_days,
            bookmark=bookmark_left,
        )
        c.showPage()
        page_number += 1

        render_month_page(
            c,
            page_number,
            month_name,
            start_day=left_days + 1,
            day_count=right_days,
            bookmark=bookmark_right,
        )
        c.showPage()
        page_number += 1

    # ---- Collections fixes ----
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
        render_simple_notes_page(c, page_number, name, bookmark=bookmark)
        c.showPage()
        page_number += 1

    # ---- Section libre ----
    for free_idx in range(free_pages_count):
        render_simple_notes_page(
            c,
            page_number,
            f"Libre {free_idx + 1}",
            bookmark="LIBRE" if free_idx == 0 else None,
        )
        c.showPage()
        page_number += 1

    # ---- Dailies de test ----
    for i, (date_label, day_label) in enumerate(iter_daily_labels(year, daily_count), start=1):
        render_daily(
            c,
            page_number,
            page_number + 1,
            page1_bookmark=f"DAILY_{i:03d}_A",
            page2_bookmark=f"DAILY_{i:03d}_B",
            date_label=date_label,
            day_label=day_label,
        )
        c.showPage()
        page_number += 2

    c.save()


if __name__ == "__main__":
    output = Path("output")
    output.mkdir(exist_ok=True)

    build(output / "year_generic_test.pdf", daily_count=DEFAULT_TEST_DAILY_COUNT, year=None)
    build(output / "year_2026_test.pdf", daily_count=DEFAULT_TEST_DAILY_COUNT, year=2026)

    print("PDF générique de test généré dans ./output/year_generic_test.pdf")
    print("PDF 2026 de test généré dans ./output/year_2026_test.pdf")
