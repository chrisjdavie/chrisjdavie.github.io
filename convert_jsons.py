import json
from pathlib import Path

old_dir = Path("portfolio_data/old")
new_dir = Path("portfolio_data")

for data_json in old_dir.iterdir():
    with data_json.open("r") as old_fh:
        data = json.load(old_fh)
    rename = ["caption", "alt_text", "link", "embed_html"]
    data["image"] = {}
    for to_rename in rename:
        old_name = "image_" + to_rename
        if old_name in data:
            data["image"][to_rename] = data[old_name]
            data.pop(old_name)

    key_order = [
        "name", "page_title", "title", "subtitle", "company_name", "tldr",
        "skills_employed", "image", "image_social_media_link", "sections",
        "footnotes"]

    reordered_data = {}
    for key in key_order:
        reordered_data[key] = data.get(key, "")
    for key, item in data.items():
        if key not in key_order:
            reordered_data[key] = item

    with open(new_dir/data_json.name, "w") as new_fh:
        json.dump(reordered_data, new_fh, indent=4)
