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

    text(c, gx(0), gy(rows) + 3, "Mois de :")
    text_right(c, PAGE_WIDTH - MARGIN, gy(rows) + 3, "INDEX  MOIS  PARKING  PRIÈRES")

    top_content_row = rows - 2
    day_count = 16
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
        text(c, gx(0), gy(number_row) - 3, str(i + 16))

    c.showPage()
    c.save()
