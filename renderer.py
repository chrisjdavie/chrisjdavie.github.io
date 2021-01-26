import codecs
import json
import re
from datetime import date
from pathlib import Path
from pprint import pprint

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape


PORTFOLIO_DIR = Path("portfolio")


def render_markdown(portfolio_md_path):

    with codecs.open(portfolio_md_path) as md_fh:
        text = md_fh.read()

    html = markdown.markdown(text)

    html = html.replace("<h1>", '<h1 class="blog-post-title">')
    html = html.replace("<h2>", '<h2 class="blog-post-subtitle">')
    html = html.replace('<h2 class="blog-post-subtitle">',
                        '<h2 class="text-muted">', 1)
    html = html.replace("<img ", '<img class="img-fluid portfolio-image " ')

    html = html.replace("<plot-title>", "<center><plot-title>")
    html = html.replace("</plot-title>", "</plot-title></center>")

    # svgs need a special class 'style-bust-svg' so this uses regex to do that
    html = re.sub(
        '(img class="[a-z\- ]*)"( .*images/[a-z_]*\.svg")',
        r'\1 style-bust-svg"\2',
        html
    )

    return html


def render_portfolio_items(env, navbar, headers):
    template = env.get_template("portfolio_page.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    all_portfolio_data = []

    for item_dir in PORTFOLIO_DIR.iterdir():

        if item_dir.is_dir():

            portfolio_data_path = item_dir/"data.json"
            with portfolio_data_path.open("r") as pd_fh:
                portfolio_data = json.load(pd_fh)
            all_portfolio_data.append(portfolio_data)

            portfolio_md_path = item_dir / "contents.md"
            portfolio_html_path = portfolio_data["portfolio_link"]

            contents = render_markdown(portfolio_md_path)

            page_src = template.render(
                **portfolio_data, relative_position="../", contents=contents
            )

            with open(portfolio_html_path, "w") as page_fh:
                page_fh.write(page_src)

    return all_portfolio_data


def setup_portfolio_data(all_portfolio_data):
    """
    data format specified by

    templates/portfolio.html.jinja
    """
    cols_in_a_row = 3

    categories = [
        {
            "category": "commercial",
            "title": "Commercial Projects",
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

    categories = [
        {
            "category": "commercial",
            "title": "Commercial Projects",
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

    return categories


def load_setup_testimonial_data():
    """
    data format specified by

    templates/testimonials.html.jinja
    """

    cols_in_a_row = 2

    with open("testimonials.json", "r") as testimonials_fh:
        data = json.load(testimonials_fh)

    data.sort(key=lambda x: date.fromisoformat(x["date"]), reverse=True)

    formatted_data = []
    for i, giver in enumerate(data):
        if not i % cols_in_a_row:
            formatted_data.append([])
        formatted_data[-1].append(giver)

    return formatted_data


def render_portfolio(env, navbar, headers, all_portfolio_data):

    all_portfolio_data.sort(
        key=lambda x: date.fromisoformat(x["created_date"]), reverse=True)

    template = env.get_template("portfolio.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    about = env.get_template("about.html.jinja")
    template.blocks["about"] = about.render
    testimonials_page = env.get_template("testimonials.html.jinja")
    template.blocks["testimonials"] = testimonials_page.render

    name_porfolio_link = {
        p_data["name"]: p_data["portfolio_link"]
        for p_data in all_portfolio_data
    }

    categories = setup_portfolio_data(all_portfolio_data)
    testimonials = load_setup_testimonial_data()

    page_src = template.render(
        categories=categories,
        name_porfolio_link=name_porfolio_link,
        testimonials_data=testimonials
    )

    with open("portfolio.html", "w") as portfolio_fh:
        portfolio_fh.write(page_src)


if __name__ == "__main__":

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )
    navbar = env.get_template("navbar.html.jinja")
    headers = env.get_template("headers.html.jinja")

    all_portfolio_data = render_portfolio_items(env, navbar, headers)
    render_portfolio(env, navbar, headers, all_portfolio_data)
