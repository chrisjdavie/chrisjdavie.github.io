import json
import re
from html.parser import HTMLParser
from pprint import pprint

fname = "website_old/RTI.html"
output_fname = "portfolio_data/rti.json"

class OldPortfolioParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._is_h1 = False
        self._in_img = False
        self._in_page_title = True
        self._in_tldr = False
        self._in_ref = False
        self._in_footer = False
        self._in_para = False
        self._tldr = ""
        self._new_para = False
        self.reformatted = {
            "image": {},
            "sections": [
                {
                    "subsections": []
                }
            ],
            "footnotes": []
        }
        self._in_sections = False
        self._first_header = True
        self._current_paragraphs = []

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self._is_h1 = True
        if tag == "p":
            self._new_para = True
            self._in_para = True
        if tag == "img":
            for attr in attrs:
                if attr[0] == "alt":
                    self.reformatted["image"]["alt_text"] = attr[1]
                if attr[0] == "src":
                    self.reformatted["image"]["link"] = attr[1]
            self._in_img = True
        if tag == "meta":
            is_sm_image = False
            sm_image_link = ""

            for attr in attrs:
                if attr[1] == "og:image":
                    is_sm_image = True
                if attr[0] == "content":
                    sm_image_link = attr[1]
            if is_sm_image:
                self.reformatted["image_social_media_link"] = sm_image_link

    def handle_endtag(self, tag):
        if tag == "h1":
            self._is_h1 = False
        if tag == "p":
            self._new_para = False
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

        if not strip_data or "Copyright" in strip_data:
            pass
        elif self._is_h1:
            if not self.reformatted.get("title"):
                self.reformatted["title"] = strip_data
            elif not self.reformatted.get("subtitle"):
                self.reformatted["subtitle"] = strip_data
                self._in_tldr = True
            else:
                self._in_sections = True

                self._current_paragraphs = []
                if self._first_header:
                    self.reformatted["sections"][-1]["title"] = strip_data
                    self.reformatted["sections"][-1]["paragraphs"] = self._current_paragraphs
                    self._first_header = False
                else:
                    self.reformatted["sections"][-1]["subsections"].append(
                        {
                            "title": strip_data,
                            "paragraphs": self._current_paragraphs
                        }
                    )
        elif self._in_sections:
            if self._new_para:
                self._current_paragraphs.append(
                    "")
                self._new_para = False
            else:
                strip_data = " " + strip_data

            old_text = self._current_paragraphs[-1]
            new_text = old_text + strip_data
            new_text = self._fix_punctuation(new_text)
            self._current_paragraphs[-1] = new_text
        elif self._in_img:
            self.reformatted["image"]["caption"] = strip_data
            self._in_img = False
        elif "skills employed" in strip_data.lower():
            self._in_tldr = False
            self.reformatted["skills_employed"] = strip_data.split(": ")[1]
        elif self._in_tldr:
            self._tldr += self._fix_punctuation(" " + strip_data)
            self.reformatted["tldr"] = self._tldr.strip()
        elif self._in_page_title:
            self.reformatted["page_title"] = strip_data
            self._in_page_title = False


parser = OldPortfolioParser()

with open(fname, "r") as old_portfolio_page:
    parser.feed(old_portfolio_page.read())

key_order = [
    "name", "page_title", "title", "subtitle", "company_name", "tldr",
    "skills_employed", "image", "image_social_media_link", "sections"]

reformatted_ordered = {}
for key in key_order:
    reformatted_ordered[key] = parser.reformatted.get(key, "")
for key, item in parser.reformatted.items():
    if key not in key_order:
        reformatted_ordered[key] = item

with open(output_fname, "w") as portfolio_json_fh:
    json.dump(reformatted_ordered, portfolio_json_fh, indent=4)

# pprint(parser.reformatted)
