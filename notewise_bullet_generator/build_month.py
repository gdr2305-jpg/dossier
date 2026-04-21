from pathlib import Path
from reportlab.pdfgen import canvas

from core.config import PAGE_SIZE
from core.draw import draw_dots, hline, vline
from core.geometry import gx, gy
from core.grid import grid_size
from core.text import text, text_right
from core.config import PAGE_WIDTH, MARGIN


def render_month_page(c, start_day: int, day_count: int) -> None:
    cols, rows = grid_size()

    draw_dots(c)

    text(c, gx(0), gy(rows) + 3, "Mois de :")
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


def build(output_path: str | Path) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)

    render_month_page(c, start_day=1, day_count=15)
    c.showPage()

    render_month_page(c, start_day=16, day_count=16)
    c.showPage()

    c.save()


if __name__ == "__main__":
    output = Path("output")
    output.mkdir(exist_ok=True)
    build(output / "month_validated.pdf")
    print("PDF mensuel généré dans ./output/month_validated.pdf")
