import codecs
import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown

def render_markdown(portfolio_md_path, company_name):

    with codecs.open(portfolio_md_path) as md_fh:
        text = md_fh.read()

    html = markdown.markdown(text)

    html = html.replace("<h1>", '<h1 class="blog-post-title">')
    html = html.replace("<h2>", '<h2 class="blog-post-subtitle">')
    html = html.replace('<h2 class="blog-post-subtitle">',
                        '<h2 class="text-muted">', 1)
    html = html.replace("<img ", '<img class="img-fluid portfolio-image " ')
    if company_name:
        html = html.replace(company_name, "<i>" + company_name + "</i>")
    print(html)
    return html


def render_portfolio_items(env, navbar, headers, all_portfolio_data):
    template = env.get_template("portfolio_page_md.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    for portfolio_data in all_portfolio_data:

        fprefix = portfolio_data["name"]

        portfolio_md_path = "portfolio/markdown/" + fprefix + ".md"
        portfolio_html_path = "portfolio/" + fprefix + ".md"

        contents = render_markdown(
            portfolio_md_path, portfolio_data["company_name"]
        )

        page_src = template.render(
            **portfolio_data, relative_position="../", contents=contents
        )

        with open(portfolio_html_path, "w") as page_fh:
            page_fh.write(page_src)


fname = "property_pipeline"

portfolio_json_path = "portfolio/data/" + fname + ".json"
portfolio_md_path = "portfolio/markdown/" + fname + ".md"

with open(portfolio_json_path, "rb") as portfolio_json_fh:
    data = json.load(portfolio_json_fh)

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html'])
)
navbar = env.get_template("navbar.html.jinja")
headers = env.get_template("headers.html.jinja")

all_portfolio_data = [data]

render_portfolio_items(env, navbar, headers, all_portfolio_data)
