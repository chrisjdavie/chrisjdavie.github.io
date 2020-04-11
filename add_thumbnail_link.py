from datetime import date
from pathlib import Path
import json


portfolio_data_dir = Path("portfolio_data")
image_dir = Path("images")

for portfolio_data_path in portfolio_data_dir.iterdir():
    if portfolio_data_path.suffix != ".json":
        continue

    with portfolio_data_path.open("rb") as portfolio_data_fh:
        portfolio_data = json.load(portfolio_data_fh)

    portfolio_data["category"] = "commercial"

    with portfolio_data_path.open("w") as portfolio_data_fh:
        json.dump(portfolio_data, portfolio_data_fh, indent=4)
