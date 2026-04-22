from reportlab.pdfgen.canvas import Canvas
from .config import PAGE_WIDTH, PAGE_HEIGHT, MARGIN, GRID_STEP, DOT_RADIUS, LINE_WIDTH


def draw_dots(c: Canvas) -> None:
    c.saveState()
    c.setFillGray(0.45)
    x = MARGIN
    while x <= PAGE_WIDTH - MARGIN + 0.1:
        y = MARGIN
        while y <= PAGE_HEIGHT - MARGIN + 0.1:
            c.circle(x, y, DOT_RADIUS, fill=1, stroke=0)
            y += GRID_STEP
        x += GRID_STEP
    c.restoreState()


def hline(c: Canvas, x1: float, y: float, x2: float) -> None:
    c.setLineWidth(LINE_WIDTH)
    c.line(x1, y, x2, y)


def vline(c: Canvas, x: float, y1: float, y2: float) -> None:
    c.setLineWidth(LINE_WIDTH)
    c.line(x, y1, x, y2)
