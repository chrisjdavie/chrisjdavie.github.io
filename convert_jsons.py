import json
from pathlib import Path

old_dir = Path("portfolio_data_old")
new_dir = Path("portfolio_data")

for data_json in old_dir.iterdir():
    with data_json.open("r") as old_fh:
        data = json.load(old_fh)

    data["github_repo_link"] = ""

    with open(new_dir/data_json.name, "w") as new_fh:
        json.dump(data, new_fh, indent=4)
