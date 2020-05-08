import json
from pathlib import Path

json_dir = Path("portfolio/data")
md_dir = Path("portfolio/markdown")
new_md_dir = Path("portfolio/new_markdown")

for json_path in json_dir.iterdir():
    md_path = md_dir/(json_path.stem + ".md")
    new_md_path = new_md_dir/md_path.name

    with json_path.open("r") as json_fh:
        company_name = json.load(json_fh)["company_name"]

    with md_path.open("r") as md_fh:
        markdown = md_fh.readlines()

    new_md = markdown
    if company_name:
        new_md = [
            line.replace(company_name, "*" + company_name + "*")
            for line in markdown
        ]

    with new_md_path.open("w") as new_md_fh:
        new_md_fh.writelines(new_md)
