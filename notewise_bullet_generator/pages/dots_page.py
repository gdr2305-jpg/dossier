from reportlab.pdfgen import canvas
from pathlib import Path

from core.config import PAGE_SIZE
from core.draw import draw_dots


def build(output_path: str | Path) -> None:
    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)
    draw_dots(c)
    c.showPage()
    c.save()
