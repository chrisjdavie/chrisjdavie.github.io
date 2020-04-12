from datetime import date
from pathlib import Path
from shutil import copy
import json

old_image_dir = Path("old_images")
new_image_dir = Path("images")

for old_image_path in old_image_dir.iterdir():
    new_name = old_image_path.name.replace("-", "_")
    new_image_path = new_image_dir/new_name
    copy(old_image_path, new_image_path)


# old_portfolio_data_dir = Path("portfolio_data_bkp")
# new_portfolio_data_dir = Path("portfolio_data")
# image_dir = Path("images")

# keys_to_replace = [
#     ("name",),
#     ("image_social_media_link",),
#     ("image", "link",),
#     ("index", "image_link",),
#     ("portfolio_link",),
# ]

# for old_portfolio_data_path in old_portfolio_data_dir.iterdir():
#     if old_portfolio_data_path.suffix != ".json":
#         continue

#     with old_portfolio_data_path.open("rb") as portfolio_data_fh:
#         portfolio_data = json.load(portfolio_data_fh)

#     for keys_nested in keys_to_replace:
#         data_to_rename = portfolio_data
#         for key in keys_nested[:-1]:
#             data_to_rename = data_to_rename[key]

#         key = keys_nested[-1]
#         if key in data_to_rename:
#             data_to_rename[key] = data_to_rename[key].replace("-", "_")

#     new_name = old_portfolio_data_path.name.replace("-", "_")
#     new_portfolio_data_path = new_portfolio_data_dir / new_name

#     with new_portfolio_data_path.open("w") as portfolio_data_fh:
#         json.dump(portfolio_data, portfolio_data_fh, indent=4)
