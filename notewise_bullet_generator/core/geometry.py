from .config import MARGIN, GRID_STEP


def gx(col: float) -> float:
    return MARGIN + col * GRID_STEP


def gy(row: float) -> float:
    return MARGIN + row * GRID_STEP
