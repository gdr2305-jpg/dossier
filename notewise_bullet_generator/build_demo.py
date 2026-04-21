from pathlib import Path

from pages.dots_page import build as build_dots
from pages.month_left_validated import build as build_month_left
from pages.daily_validated import build as build_daily

output = Path("output")
output.mkdir(exist_ok=True)

build_dots(output / "dots_page.pdf")
build_month_left(output / "month_left_validated.pdf")
build_daily(output / "daily_validated.pdf")

print("Fichiers générés dans ./output")
