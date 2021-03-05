from collections import deque
from pathlib import Path
from pprint import pprint
import json

REPLACE_STR_0 = "REDACTED"
REPLACE_STR_1 = "REDACTED"

root_dir = Path("roam_graph")

blog_post_graph = {}
visited = set()
to_explore = deque(["Blog post ideas"])

while to_explore:

    this_post = to_explore.pop()

    if this_post not in visited:

        visited.add(this_post)

        post_path = root_dir / Path(this_post + ".md")

        children = set()

        with post_path.open("r") as post_fh:

            for line in post_fh:

                if "[[" in line:
                    next_post = line.split("[[")[1].split("]]")[0]
                    children.add(next_post)
                    to_explore.append(next_post)

        blog_post_graph[this_post] = list(children)

cleaned_blog_post_graph = {}
for key, many_values in blog_post_graph.items():

    def clean(dirty):
        return dirty.replace(
            REPLACE_STR_0, "<YouTube personality>"
        ).replace(
            REPLACE_STR_1, "<YouTube personality>"
        )

    cleaned_blog_post_graph[clean(key)] = [
        clean(value) for value in many_values
    ]

pprint(cleaned_blog_post_graph, indent=4)

with open("blog_post_idea_graph.json", "w") as output_fh:
    json.dump(cleaned_blog_post_graph, output_fh, indent=4)
    # save data
