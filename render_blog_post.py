from jinja2 import Environment, FileSystemLoader, select_autoescape

from renderer import render_markdown


def render_blog_page(env, navbar, headers):

    blog_data = {
        "name": "fix_code_base_not_dev_exp",
        "page_title": "Fixed code base, not dev experience",
        "title": "Fixed code base, not dev experience",
        "subtitle": "Increased productivity, didn't make us happy",
        # "image_social_media_link": "http://chrisjdavie.github.io/blog/fix_code_base_not_dev_exp/actual.svg",
        # "index": {
        #     "image_link": "blog/fix_code_base_not_dev_exp/actual.svg",
        #     "tldr": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        # },
        "created_date": "2021-01-16",
        "relative_link": "blog/fix_code_base_not_dev_exp.html",
        "github_repo_link": ""
    }

    template = env.get_template("portfolio_page.html.jinja")
    template.blocks["navbar"] = navbar.render
    template.blocks["headers"] = headers.render

    blog_md_path = "blog/fix_code_base_not_dev_exp/contents.md"
    blog_html_path = blog_data["relative_link"]

    contents = render_markdown(blog_md_path)

    page_src = template.render(
        **blog_data, relative_position="../", contents=contents
    )

    with open(blog_html_path, "w") as page_fh:
        page_fh.write(page_src)


if __name__ == "__main__":

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )
    navbar = env.get_template("navbar.html.jinja")
    headers = env.get_template("headers.html.jinja")

    render_blog_page(env, navbar, headers)
