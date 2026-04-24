from __future__ import annotations

from calendar import monthcalendar, monthrange
from datetime import date, timedelta
from pathlib import Path

from reportlab.lib.colors import Color
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from core.config import MARGIN, PAGE_SIZE, PAGE_WIDTH
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

DAY_INITIALS = ["L", "M", "M", "J", "V", "S", "D"]
DAY_SHORT_NAMES = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

SIDE_TABS = [
    ("INDEX", "INDEX"),
    ("MOIS", "MONTHS"),
    ("JOURS", "DAYS"),
    ("PARKING", "PARKING"),
    ("PRIÈRES", "PRAYERS"),
    ("LIBRE", "LIBRE"),
]

FREE_PAGES_COUNT = 6
DEFAULT_TEST_DAILY_COUNT = 14
TITLE_COLOR = (0.18, 0.24, 0.42)
MONTH_TITLE_COLOR = (0.24, 0.18, 0.38)
DAYS_TITLE_COLOR = (0.30, 0.40, 0.50)
DAYS_HEADER_FILL = Color(0.87, 0.91, 0.94)
DAYS_PANEL_FILL = Color(0.96, 0.97, 0.98)
DAYS_WEEKDAY_FILL = Color(0.93, 0.95, 0.97)
DAYS_WEEKEND_FILL = Color(0.90, 0.90, 0.90)
DAYS_BORDER_COLOR = Color(0.55, 0.63, 0.70)
TAB_FILL = Color(0.97, 0.98, 0.99)
TAB_ACTIVE_FILL = Color(0.87, 0.91, 0.94)
TAB_BORDER_COLOR = Color(0.45, 0.50, 0.55)
TAB_ACTIVE_BORDER_COLOR = Color(0.25, 0.35, 0.45)
SECTION_TITLE_COLORS = {
    "Parking": (0.34, 0.25, 0.18),
    "Achats": (0.14, 0.35, 0.32),
    "Grandes idées": (0.28, 0.17, 0.34),
    "Prières": (0.34, 0.20, 0.20),
}


QUARTERS = [
    ("JOURS_T1", [1, 2, 3], "Janvier à Mars"),
    ("JOURS_T2", [4, 5, 6], "Avril à Juin"),
    ("JOURS_T3", [7, 8, 9], "Juillet à Septembre"),
    ("JOURS_T4", [10, 11, 12], "Octobre à Décembre"),
]


def content_right_x() -> float:
    cols, _ = grid_size()
    return gx(cols - 2.4)


def draw_title(c, y: float, value: str, size: int = 20, color: tuple[float, float, float] = TITLE_COLOR) -> None:
    c.saveState()
    c.setFillColorRGB(*color)
    c.setFont("Times-BoldItalic", size)
    c.drawCentredString(PAGE_WIDTH / 2, y, value)
    c.restoreState()


def draw_section_title(c, y: float, value: str) -> None:
    base_value = value
    if value.startswith("Prières"):
        base_value = "Prières"
    elif value.startswith("Parking"):
        base_value = "Parking"
    elif value.startswith("Achats"):
        base_value = "Achats"
    elif value.startswith("Grandes idées"):
        base_value = "Grandes idées"
    color = SECTION_TITLE_COLORS.get(base_value, TITLE_COLOR)
    draw_title(c, y, value, size=18, color=color)


def draw_header_links(c, rows: int, right_x: float | None = None) -> None:
    y = gy(rows) + 3
    x = right_x if right_x is not None else content_right_x()
    for label, target in reversed(SIDE_TABS):
        width_guess = max(24, len(label) * 4.5)
        left = x - width_guess
        text(c, left, y, label)
        c.linkRect("", target, (left, y - 2, x, y + 9), relative=0, thickness=0)
        x = left - 6


def draw_side_tabs(c, active_target: str | None = None) -> None:
    cols, rows = grid_size()
    tab_left = gx(cols - 1.65)
    tab_right = PAGE_WIDTH
    tab_width = tab_right - tab_left
    tab_height = gy(1.7) - gy(0)
    top_start = gy(rows) - tab_height - 1
    gap = gy(0.2) - gy(0)

    c.saveState()
    for idx, (label, target) in enumerate(SIDE_TABS):
        top = top_start - idx * (tab_height + gap)
        bottom = top - tab_height
        is_active = target == active_target

        c.setLineWidth(0.8 if is_active else 0.55)
        c.setFillColor(TAB_ACTIVE_FILL if is_active else TAB_FILL)
        c.setStrokeColor(TAB_ACTIVE_BORDER_COLOR if is_active else TAB_BORDER_COLOR)
        c.roundRect(tab_left, bottom, tab_width, tab_height, 1.4 * mm, stroke=1, fill=1)

        c.setFillColorRGB(0.08, 0.10, 0.12)
        c.setFont("Helvetica-Bold" if is_active else "Helvetica", 6)
        c.drawString(tab_left + 2.2, bottom + tab_height / 2 - 2.1, label)
        c.linkRect("", target, (tab_left, bottom, tab_right, top), relative=0, thickness=0)
    c.restoreState()


def active_tab_for_notes_page(header_left: str, bookmark: str | None) -> str | None:
    side_tab_targets = {target for _, target in SIDE_TABS}
    if bookmark in side_tab_targets:
        return bookmark
    if header_left.startswith("Parking"):
        return "PARKING"
    if header_left.startswith("Prières"):
        return "PRAYERS"
    if header_left.startswith("Libre"):
        return "LIBRE"
    return None


def draw_page_number(c, page_number: int) -> None:
    text_right(c, PAGE_WIDTH - MARGIN, gy(0) - 8, f"p. {page_number}")


def draw_month_mini_calendar(c, x: float, top_y: float, year: int, month: int) -> None:
    weeks = monthcalendar(year, month)
    cell_w = 9
    cell_h = 8

    c.saveState()
    c.setFont("Helvetica", 5)
    for idx, initial in enumerate(DAY_INITIALS):
        c.drawCentredString(x + idx * cell_w + cell_w / 2, top_y, initial)

    for week_idx, week in enumerate(weeks):
        y = top_y - (week_idx + 1) * cell_h
        for day_idx, day_number in enumerate(week):
            if day_number:
                c.drawCentredString(x + day_idx * cell_w + cell_w / 2, y, str(day_number))
    c.restoreState()


def add_index_entry(c, label: str, row: int, target: str, page_number: int) -> None:
    y = gy(row) - 3
    left = gx(2)
    right = content_right_x() - 4
    text(c, left, y, label, size=10)
    text_right(c, right, y, str(page_number), size=10, font_name="Helvetica-Bold")
    hline(c, left, y - 3, right)
    c.linkRect("", target, (left, y - 6, right, y + 10), relative=0, thickness=0)


def render_simple_index_page(c, page_number: int, page_map: dict[str, int], title: str = "INDEX") -> None:
    _, rows = grid_size()
    c.bookmarkPage("INDEX")
    draw_dots(c)
    draw_side_tabs(c, active_target="INDEX")
    draw_title(c, gy(rows) + 2, title, size=22)
    text(c, gx(2), gy(rows - 2) + 2, "Navigation générale", size=9, font_name="Helvetica-Oblique")
    lines = [
        ("Année / Semestres", "SEM1"),
        ("Mois", "MONTHS"),
        ("Jours", "DAYS"),
        ("Parking", "PARKING"),
        ("Achats", "ACHATS"),
        ("Grandes idées", "IDEAS"),
        ("Prières", "PRAYERS"),
        ("Libre", "LIBRE"),
    ]
    start_row = rows - 5
    for i, (value, target) in enumerate(lines):
        add_index_entry(c, value, start_row - 3 * i, target, page_map[target])
    draw_page_number(c, page_number)


def render_months_index_page(c, page_number: int, page_map: dict[str, int], year: int | None = None) -> None:
    _, rows = grid_size()
    c.bookmarkPage("MONTHS")
    draw_dots(c)
    draw_side_tabs(c, active_target="MONTHS")
    draw_title(c, gy(rows) + 2, "MOIS", size=20)
    left_x = gx(1)
    right_x = gx(10)
    start_y = gy(rows - 4)
    block_gap = gy(5) - gy(0)
    for idx, month_name in enumerate(MONTH_NAMES[:6], start=1):
        y = start_y - (idx - 1) * block_gap
        text(c, left_x, y, month_name, size=10, font_name="Helvetica-Bold")
        text_right(c, gx(8.5), y, str(page_map[f"MONTH_{idx:02d}_L"]), size=9)
        if year is not None:
            draw_month_mini_calendar(c, left_x, y - 10, year, idx)
        c.linkRect("", f"MONTH_{idx:02d}_L", (left_x, y - 38, gx(8.5), y + 10), relative=0, thickness=0)
    for idx, month_name in enumerate(MONTH_NAMES[6:], start=7):
        y = start_y - (idx - 7) * block_gap
        text(c, right_x, y, month_name, size=10, font_name="Helvetica-Bold")
        text_right(c, gx(17.5), y, str(page_map[f"MONTH_{idx:02d}_L"]), size=9)
        if year is not None:
            draw_month_mini_calendar(c, right_x, y - 10, year, idx)
        c.linkRect("", f"MONTH_{idx:02d}_L", (right_x, y - 38, gx(17.5), y + 10), relative=0, thickness=0)
    draw_page_number(c, page_number)


def render_simple_notes_page(c, page_number: int, header_left: str, bookmark: str | None = None) -> None:
    _, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)
    draw_dots(c)
    draw_side_tabs(c, active_target=active_tab_for_notes_page(header_left, bookmark))
    if header_left.startswith(("Parking", "Achats", "Grandes idées", "Prières")):
        draw_section_title(c, gy(rows) + 2, header_left)
    else:
        text(c, gx(0), gy(rows) + 3, header_left)
    draw_page_number(c, page_number)


def daily_bookmark_for_date(current_date: date, daily_count: int) -> str | None:
    day_of_year = current_date.timetuple().tm_yday
    if day_of_year > daily_count:
        return None
    return f"DAILY_{day_of_year:03d}_A"


def render_days_quarter_page(
    c,
    page_number: int,
    page_map: dict[str, int],
    daily_count: int,
    year: int | None,
    months: list[int],
    bookmark: str,
    subtitle: str,
) -> None:
    _, rows = grid_size()
    c.bookmarkPage(bookmark)
    if bookmark == "JOURS_T1":
        c.bookmarkPage("DAYS")
    draw_dots(c)
    draw_side_tabs(c, active_target="DAYS")
    draw_title(c, gy(rows) + 2, "JOURS", size=21, color=DAYS_TITLE_COLOR)
    text(c, gx(1), gy(rows - 1.7) + 2, subtitle, size=9, font_name="Helvetica-Oblique")

    if year is None:
        text(c, gx(1), gy(rows - 5), "Les pages JOURS nécessitent une année renseignée.", size=10)
        draw_page_number(c, page_number)
        return

    panel_left = gx(0.8)
    panel_width = content_right_x() - panel_left
    panel_height = 56 * mm
    top_y = gy(rows - 3.1)
    header_height = 8 * mm
    weekday_height = 6 * mm
    calendar_bottom_margin = 2.5 * mm

    for idx, month in enumerate(months):
        panel_top = top_y - idx * (panel_height + 4 * mm)
        panel_bottom = panel_top - panel_height

        c.saveState()
        c.setFillColor(DAYS_PANEL_FILL)
        c.setStrokeColor(DAYS_BORDER_COLOR)
        c.roundRect(panel_left, panel_bottom, panel_width, panel_height, 4 * mm, stroke=1, fill=1)
        c.setFillColor(DAYS_HEADER_FILL)
        c.roundRect(panel_left, panel_top - header_height, panel_width, header_height, 4 * mm, stroke=0, fill=1)
        c.restoreState()

        text(c, panel_left + 4 * mm, panel_top - 5.4 * mm, MONTH_NAMES[month - 1], size=11, font_name="Helvetica-Bold")
        text_right(c, panel_left + panel_width - 4 * mm, panel_top - 5.4 * mm, str(year), size=8, font_name="Helvetica")

        weeks = monthcalendar(year, month)
        cell_left = panel_left + 3 * mm
        cell_right = panel_left + panel_width - 3 * mm
        cell_top = panel_top - header_height - weekday_height
        cell_bottom = panel_bottom + calendar_bottom_margin
        cell_width = (cell_right - cell_left) / 7
        cell_height = (cell_top - cell_bottom) / len(weeks)

        c.saveState()
        c.setFillColor(DAYS_WEEKDAY_FILL)
        c.rect(cell_left, panel_top - header_height - weekday_height, cell_right - cell_left, weekday_height, stroke=0, fill=1)
        c.restoreState()

        for day_idx, short_name in enumerate(DAY_SHORT_NAMES):
            x_center = cell_left + day_idx * cell_width + cell_width / 2
            c.setFont("Helvetica", 6)
            c.drawCentredString(x_center, panel_top - header_height - 4.3 * mm, short_name)

        for week_idx, week in enumerate(weeks):
            for day_idx, day_number in enumerate(week):
                x = cell_left + day_idx * cell_width
                y = cell_top - (week_idx + 1) * cell_height
                c.saveState()
                if day_idx >= 5:
                    c.setFillColor(DAYS_WEEKEND_FILL)
                    c.rect(x, y, cell_width, cell_height, stroke=0, fill=1)
                c.setStrokeColor(DAYS_BORDER_COLOR)
                c.rect(x, y, cell_width, cell_height, stroke=1, fill=0)
                c.restoreState()
                if not day_number:
                    continue
                current_date = date(year, month, day_number)
                bookmark_target = daily_bookmark_for_date(current_date, daily_count)
                day_label = DAY_SHORT_NAMES[current_date.weekday()]
                text(c, x + 1.3 * mm, y + cell_height - 5 * mm, f"{day_number:02d}", size=8, font_name="Helvetica-Bold")
                text(c, x + cell_width - 1.2 * mm - 10, y + 2.2 * mm, day_label, size=5)
                if bookmark_target is not None:
                    c.linkRect("", bookmark_target, (x, y, x + cell_width, y + cell_height), relative=0, thickness=0)
                else:
                    c.saveState()
                    c.setFillGray(0.80)
                    c.rect(x + 0.7 * mm, y + 0.7 * mm, cell_width - 1.4 * mm, cell_height - 1.4 * mm, stroke=0, fill=1)
                    c.restoreState()
                    text(c, x + 1.3 * mm, y + cell_height - 5 * mm, f"{day_number:02d}", size=8, font_name="Helvetica-Bold")
                    text(c, x + cell_width - 1.2 * mm - 10, y + 2.2 * mm, day_label, size=5)

    draw_page_number(c, page_number)


def render_month_page(c, page_number: int, month_name: str, month_index: int, start_day: int, day_count: int, year: int | None = None, bookmark: str | None = None) -> None:
    cols, rows = grid_size()
    if bookmark:
        c.bookmarkPage(bookmark)
    draw_dots(c)
    c.saveState()
    c.setFillColorRGB(*MONTH_TITLE_COLOR)
    c.setFont("Times-BoldItalic", 18)
    c.drawString(gx(0), gy(rows) + 2, f"Mois de : {month_name}")
    c.restoreState()
    draw_header_links(c, rows, right_x=PAGE_WIDTH - MARGIN)
    top_content_row = rows - 2
    right_x = PAGE_WIDTH - MARGIN
    bottom_boundary_row = top_content_row - day_count * 2
    for k in range(day_count + 1):
        r = top_content_row - 2 * k
        hline(c, gx(0), gy(r), right_x)
    hour_cols = [2 + i * 3 for i in range(7)]
    hours = ["8h", "10h", "12h", "14h", "16h", "18h", "20h"]
    for col, hour in zip(hour_cols, hours):
        vline(c, gx(col), gy(bottom_boundary_row), gy(top_content_row))
        text(c, gx(col) - 6, gy(top_content_row) + 6, hour)
    for i in range(day_count):
        day_number = start_day + i
        number_row = top_content_row - 1 - 2 * i
        if year is not None:
            initial = DAY_INITIALS[date(year, month_index, day_number).weekday()]
            text(c, gx(0), gy(number_row) - 3, str(day_number), size=8)
            text(c, gx(0.8), gy(number_row) - 3, initial, size=8, font_name="Helvetica-Oblique")
        else:
            text(c, gx(0), gy(number_row) - 3, str(day_number), size=8)
    draw_page_number(c, page_number)


def render_daily(c, page_number_1: int, page_number_2: int, page1_bookmark: str | None = None, page2_bookmark: str | None = None, date_label: str | None = None, day_label: str | None = None) -> None:
    rows = grid_size()[1]
    right_x = content_right_x()
    if page1_bookmark:
        c.bookmarkPage(page1_bookmark)
    draw_dots(c)
    draw_side_tabs(c, active_target="DAYS")
    top = rows
    date_value = date_label if date_label is not None else ""
    day_value = day_label if day_label is not None else ""
    text(c, gx(0), gy(top) + 3, f"Date : {date_value}", size=11, font_name="Helvetica-Bold")
    text(c, gx(0), gy(top - 2) + 3, f"Jour : {day_value}", size=11, font_name="Helvetica-Bold")
    prio_top = top - 4
    priority_line_rows = [prio_top - 1, prio_top - 3, prio_top - 5, prio_top - 7]
    priority_box_rows = [r - 1 for r in priority_line_rows]
    prio_bottom_line = prio_top - 9
    hline(c, gx(0), gy(prio_top), right_x)
    text(c, gx(0), gy(prio_top) + 3, "PRIORITÉS")
    for line_r, box_r in zip(priority_line_rows, priority_box_rows):
        c.rect(gx(0.1), gy(box_r) - 4, 10, 10)
        hline(c, gx(1.8), gy(line_r), right_x)
    hline(c, gx(0), gy(prio_bottom_line), right_x)
    sep_row = prio_bottom_line - 2
    mid_col = 11
    hline(c, gx(0), gy(sep_row), right_x)
    text(c, gx(0), gy(sep_row) + 3, "TEMPS")
    text(c, gx(mid_col + 1), gy(sep_row) + 3, "TÂCHES")
    time_hours = list(range(8, 23))
    time_start_row = sep_row - 2
    for i, h in enumerate(time_hours):
        r = time_start_row - i
        text(c, gx(0), gy(r) - 3, f"{h:02d}h")
        hline(c, gx(2.2), gy(r), gx(mid_col - 1))
    task_line_rows = [sep_row - 1, sep_row - 3, sep_row - 5, sep_row - 7, sep_row - 9]
    task_box_rows = [r - 1 for r in task_line_rows]
    for line_r, box_r in zip(task_line_rows, task_box_rows):
        c.rect(gx(mid_col + 2.1), gy(box_r) - 4, 10, 10)
        hline(c, gx(mid_col + 4.1), gy(line_r), right_x)

    notes_divider_row = task_line_rows[-1] - 3
    notes_label_row = notes_divider_row + 1
    report_label_row = notes_divider_row - 5
    bottom_split_row = 2

    vline(c, gx(mid_col), gy(sep_row), gy(bottom_split_row))
    hline(c, gx(mid_col), gy(notes_divider_row), right_x)

    text(c, gx(mid_col + 1), gy(notes_label_row) + 3, "NOTES")
    text(c, gx(0), gy(report_label_row) + 3, "REPORT / À MIGRER")
    text(c, gx(0), gy(1), "INDEXER ? [ ] oui")
    text(c, gx(8), gy(1), "Entrée index :")
    draw_page_number(c, page_number_1)
    c.showPage()
    if page2_bookmark:
        c.bookmarkPage(page2_bookmark)
    draw_dots(c)
    draw_side_tabs(c, active_target="DAYS")
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


def compute_page_map(daily_count: int, free_pages_count: int) -> dict[str, int]:
    page = 1
    page_map: dict[str, int] = {}
    page_map["INDEX"] = page
    page += 1
    page += 1
    page_map["SEM1"] = page
    page += 1
    page += 1
    page_map["MONTHS"] = page
    page += 1
    page_map["DAYS"] = page
    for bookmark, _, _ in QUARTERS:
        page_map[bookmark] = page
        page += 1
    for month_idx in range(1, 13):
        page_map[f"MONTH_{month_idx:02d}_L"] = page
        page += 1
        page_map[f"MONTH_{month_idx:02d}_R"] = page
        page += 1
    page_map["PARKING"] = page
    page += 2
    page_map["ACHATS"] = page
    page += 1
    page_map["IDEAS"] = page
    page += 1
    page_map["PRAYERS"] = page
    page += 4
    page_map["LIBRE"] = page
    page += free_pages_count
    for daily_idx in range(1, daily_count + 1):
        page_map[f"DAILY_{daily_idx:03d}_A"] = page
        page += 1
        page_map[f"DAILY_{daily_idx:03d}_B"] = page
        page += 1
    return page_map


def build(output_path: str | Path, daily_count: int = DEFAULT_TEST_DAILY_COUNT, year: int | None = None, free_pages_count: int = FREE_PAGES_COUNT) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)
    page_number = 1
    page_map = compute_page_map(daily_count, free_pages_count)
    render_simple_index_page(c, page_number, page_map, "INDEX")
    c.showPage(); page_number += 1
    render_simple_notes_page(c, page_number, "Abréviations / Conventions")
    c.showPage(); page_number += 1
    render_simple_notes_page(c, page_number, "Semestre 1", bookmark="SEM1")
    c.showPage(); page_number += 1
    render_simple_notes_page(c, page_number, "Semestre 2", bookmark="SEM2")
    c.showPage(); page_number += 1
    render_months_index_page(c, page_number, page_map, year=year)
    c.showPage(); page_number += 1
    for bookmark, months, subtitle in QUARTERS:
        render_days_quarter_page(c, page_number, page_map, daily_count, year, months, bookmark, subtitle)
        c.showPage(); page_number += 1
    month_day_counts = month_day_counts_for_year(year)
    for idx, (month_name, month_day_count) in enumerate(zip(MONTH_NAMES, month_day_counts), start=1):
        bookmark_left = f"MONTH_{idx:02d}_L"; bookmark_right = f"MONTH_{idx:02d}_R"; left_days, right_days = split_month_day_count(month_day_count)
        render_month_page(c, page_number, month_name, idx, start_day=1, day_count=left_days, year=year, bookmark=bookmark_left)
        c.showPage(); page_number += 1
        render_month_page(c, page_number, month_name, idx, start_day=left_days + 1, day_count=right_days, year=year, bookmark=bookmark_right)
        c.showPage(); page_number += 1
    collections = [("Parking", "PARKING"), ("Parking — suite", None), ("Achats", "ACHATS"), ("Grandes idées", "IDEAS"), ("Prières 1", "PRAYERS"), ("Prières 2", None), ("Prières 3", None), ("Prières 4", None)]
    for name, bookmark in collections:
        render_simple_notes_page(c, page_number, name, bookmark=bookmark)
        c.showPage(); page_number += 1
    for free_idx in range(free_pages_count):
        render_simple_notes_page(c, page_number, f"Libre {free_idx + 1}", bookmark="LIBRE" if free_idx == 0 else None)
        c.showPage(); page_number += 1
    for i, (date_label, day_label) in enumerate(iter_daily_labels(year, daily_count), start=1):
        render_daily(c, page_number, page_number + 1, page1_bookmark=f"DAILY_{i:03d}_A", page2_bookmark=f"DAILY_{i:03d}_B", date_label=date_label, day_label=day_label)
        c.showPage(); page_number += 2
    c.save()


if __name__ == "__main__":
    output = Path("output")
    output.mkdir(exist_ok=True)
    build(output / "year_generic_test.pdf", daily_count=DEFAULT_TEST_DAILY_COUNT, year=None)
    build(output / "year_2026_test.pdf", daily_count=DEFAULT_TEST_DAILY_COUNT, year=2026)
