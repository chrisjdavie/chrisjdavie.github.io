import json
from pathlib import Path
from pprint import pprint

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('personalwebsite', 'templates'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template("portfolio.html.jinja")
navbar = env.get_template("navbar.html.jinja")
template.blocks["navbar"] = navbar.render

portfolio_data_dir = Path("portfolio_data")

for portfolio_data_path in portfolio_data_dir.iterdir():
    if portfolio_data_path.suffix != ".json":
        continue

    with portfolio_data_path.open("rb") as portfolio_data_fh:
        portfolio_data = json.load(portfolio_data_fh)

    page_src = template.render(
        **portfolio_data
    )
    if company_name := portfolio_data.get("company_name"):
        page_src = page_src.replace(
            company_name,
            "<i>" + company_name + "</i>")

    with open(portfolio_data["name"] + ".html", "w") as page_fh:
        page_fh.write(page_src)
