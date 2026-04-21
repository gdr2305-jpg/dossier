from reportlab.pdfgen.canvas import Canvas
from .config import FONT, FONT_SIZE


def text(c: Canvas, x: float, y: float, value: str, size: int = FONT_SIZE) -> None:
    c.setFont(FONT, size)
    c.drawString(x, y, value)


def text_right(c: Canvas, x: float, y: float, value: str, size: int = FONT_SIZE) -> None:
    c.setFont(FONT, size)
    c.drawRightString(x, y, value)
