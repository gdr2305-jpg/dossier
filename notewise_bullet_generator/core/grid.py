from .config import PAGE_WIDTH, PAGE_HEIGHT, MARGIN, GRID_STEP


def grid_size() -> tuple[int, int]:
    cols = int((PAGE_WIDTH - 2 * MARGIN) // GRID_STEP)
    rows = int((PAGE_HEIGHT - 2 * MARGIN) // GRID_STEP)
    return cols, rows
