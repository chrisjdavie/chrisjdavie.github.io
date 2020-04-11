import json
from datetime import date
from pathlib import Path
from pprint import pprint

from jinja2 import Environment, PackageLoader, select_autoescape


def render_portfolio_items(env):
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


def render_index_page(env):

    cols_in_a_row = 3

    template = env.get_template("index.html.jinja")

    portfolio_data_dir = Path("portfolio_data")

    all_portfolio_data = []
    # load data
    for portfolio_data_path in portfolio_data_dir.iterdir():
        if portfolio_data_path.suffix != ".json":
            continue

        with portfolio_data_path.open("rb") as portfolio_data_fh:
            all_portfolio_data.append(json.load(portfolio_data_fh))

    all_portfolio_data.sort(
        key=lambda x: date.fromisoformat(x["created_date"]), reverse=True)

    rows = []
    # split in 3s
    for i, portfolio_data in enumerate(all_portfolio_data):
        if not i % cols_in_a_row:
            rows.append([])
        rows[-1].append(portfolio_data)

    page_src = template.render(all_rows=rows)

    with open("index.html", "w") as index_fh:
        index_fh.write(page_src)


env = Environment(
    loader=PackageLoader('personalwebsite', 'templates'),
    autoescape=select_autoescape(['html'])
)

render_index_page(env)
