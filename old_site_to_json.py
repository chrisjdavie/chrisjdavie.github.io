import json
import re
from html.parser import HTMLParser
from pathlib import Path
from pprint import pprint
from shutil import copy

fpath = Path("website_old/testimonials.html")
output_path = Path("testimonials.json")

class TestimonialsParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = []
        self._in_testimonials = False
        self._is_blockquote = False
        self._in_para = False

        self._current_giver = {
            "testimonials": []
        }
        self._current_testimonial = []

    def handle_starttag(self, tag, attrs):
        if tag == "blockquote":
            self._is_blockquote = True
            self._in_testimonials = True
        if tag == "p":
            self._in_para = True

    def handle_endtag(self, tag):
        if tag == "blockquote":
            self._current_giver["testimonials"].append(
                self._current_testimonial)
            self._current_testimonial = []
            self._is_blockquote = False
        if tag == "p":
            self._in_para = False

    def _fix_punctuation(self, text):
        return text.replace(
            " ,", ","
        ).replace(
            " .", "."
        ).replace(
            " '", "'"
        )

    def handle_data(self, data):
        strip_data = data.strip()
        strip_data = re.sub("\n *", " ", strip_data)

        if not strip_data:
            return

        if "Copyright" in strip_data:
            self._in_testimonials = False
        if self._is_blockquote:
            self._current_testimonial.append(strip_data)
        if self._in_para and self._in_testimonials:
            author, role = strip_data.split(", ")
            self._current_giver["author"] = author
            self._current_giver["role"] = role
            self._current_giver["date"] = "1970-01-01"
            self.data.append(self._current_giver)
            self._current_giver = {
                "testimonials": []
            }


parser = TestimonialsParser()

with fpath.open("r") as testimonials_page:
    parser.feed(testimonials_page.read())

with output_path.open("w") as testimonials_json_fh:
    json.dump(parser.data, testimonials_json_fh, indent=4)
