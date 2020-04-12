import json
from datetime import date
from pathlib import Path
from pprint import pprint

from jinja2 import Environment, PackageLoader, select_autoescape


def load_portfolio_data():

    portfolio_data_dir = Path("portfolio_data")

    # load data
    all_portfolio_data = []
    for portfolio_data_path in portfolio_data_dir.iterdir():
        if portfolio_data_path.suffix != ".json":
            continue

        with portfolio_data_path.open("rb") as portfolio_data_fh:
            all_portfolio_data.append(json.load(portfolio_data_fh))

        all_portfolio_data.sort(
            key=lambda x: date.fromisoformat(x["created_date"]), reverse=True)

    return all_portfolio_data


def render_portfolio_items(env, navbar, headers, all_portfolio_data):
    template = env.get_template("portfolio.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    for portfolio_data in all_portfolio_data:

        page_src = template.render(
            **portfolio_data
        )
        if company_name := portfolio_data.get("company_name"):
            page_src = page_src.replace(
                company_name,
                "<i>" + company_name + "</i>")

        with open(portfolio_data["portfolio_link"], "w") as page_fh:
            page_fh.write(page_src)


def render_index_page(env, navbar, headers, all_portfolio_data):

    cols_in_a_row = 3

    template = env.get_template("index.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    about = env.get_template("about.html.jinja")
    template.blocks["about"] = about.render

    name_porfolio_link = {
        p_data["name"]: p_data["portfolio_link"]
        for p_data in all_portfolio_data
    }

    categories = [
        {
            "category": "commercial",
            "title": "Commerical Projects",
            "subtitle": "",
            "rows": []
        },
        {
            "category": "research",
            "title": "Research Projects",
            "subtitle": "My PhD work",
            "rows": []
        },
        {
            "category": "personal",
            "title": "Personal Projects",
            "subtitle": "For interest",
            "rows": []
        }
    ]

    for cat in categories:

        cat_data = [
            data for data in all_portfolio_data if data["category"] == cat["category"]
        ]

        rows = []
        # split in 3s
        for i, portfolio_data in enumerate(cat_data):
            if not i % cols_in_a_row:
                rows.append([])
            rows[-1].append(portfolio_data)

        cat["rows"] = rows

    page_src = template.render(
        categories=categories, name_porfolio_link=name_porfolio_link)

    with open("index.html", "w") as index_fh:
        index_fh.write(page_src)


env = Environment(
    loader=PackageLoader('personalwebsite', 'templates'),
    autoescape=select_autoescape(['html'])
)
navbar = env.get_template("navbar.html.jinja")
headers = env.get_template("headers.html.jinja")

all_portfolio_data = load_portfolio_data()

render_portfolio_items(env, navbar, headers, all_portfolio_data)
render_index_page(env, navbar, headers, all_portfolio_data)
