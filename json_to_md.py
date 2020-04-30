from pprint import pprint
import json

fname = "property_pipeline"

portfolio_json_path = "portfolio/data/" + fname + ".json"
portfolio_md_path = "portfolio/markdown/" + fname + ".md"

with open(portfolio_json_path, "rb") as portfolio_json_fh:
    data = json.load(portfolio_json_fh)

document_md = ""

document_md += "# " + data["title"] + "\n"
document_md += "## <small>" + data["subtitle"] + "</small>\n\n"

document_md += data["tldr"] + "\n\n"

document_md += "**Skills employed:** " + data["skills_employed"] + "\n\n"

document_md += (
    "![" + data["image"]["alt_text"] + "](" + data["image"]["link"] + ")" + "\n\n")

document_md += "*" + data["image"]["caption"] + "*" + "\n\n"

for sec in data["sections"]:
    document_md += "## " + sec["title"] + "\n\n"

    for para in sec.get("paragraphs", []):
        document_md += para + "\n\n"

    for subsec in sec.get("subsections", []):
        document_md += "### " + subsec["title"] + "\n\n"

        for para in subsec.get("paragraphs", []):
            document_md += para + "\n\n"

with open(portfolio_md_path, "w") as portfolio_md_fh:
    portfolio_md_fh.write(document_md)
