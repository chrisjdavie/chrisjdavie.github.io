from contextlib import contextmanager
from pathlib import Path
import os

from invoke import task

PYTHON_VERSION = "python3.8"


class Venv:
    """Misc. commands for handling virtual envs"""

    _cur_dir = os.path.dirname(os.path.abspath(__file__))
    _venv_dir = os.path.join(_cur_dir, ".venv")
    _activate_path = os.path.join(_venv_dir, "bin", "activate")
    _activate = ". {}".format(_activate_path)
    _build = f"virtualenv --python={PYTHON_VERSION} {_venv_dir}"

    @classmethod
    @contextmanager
    def _virtualenv(cls, c):
        with c.cd(cls._cur_dir), c.prefix(cls._activate):
            yield

    @classmethod
    def _setup_venv(cls, c):
        if not os.path.exists(cls._venv_dir):
            c.run(cls._build)

        with cls._virtualenv(c):
            c.run("pip install --upgrade pip")
            c.run("pip install -r requirements.txt", hide=False, echo=True)

    @classmethod
    @contextmanager
    def virtualenv(cls, c):
        cls._setup_venv(c)
        with cls._virtualenv(c):
            yield


@task
def clean_html(c):
    index_page = Path("index.html")
    if index_page.exists():
        index_page.unlink()

    portfolio_dir = Path("portfolio")

    for html_file in portfolio_dir.iterdir():
        if html_file.suffix == ".html":
            html_file.unlink()


@task(clean_html)
def render(c):

    with Venv.virtualenv(c):
        c.run("python renderer.py")
        print("Rendered website")
