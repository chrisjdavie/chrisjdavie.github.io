from pathlib import Path
from shutil import copy2
from os import mkdir
from typing import List


old_portfolio_dir = Path("portfolio_old")
old_md_dir = old_portfolio_dir/"markdown"
old_data_dir = old_portfolio_dir/"data"
old_images_dir = old_portfolio_dir/"images"

new_portfolio_dir = Path("portfolio")


class BlogPost:

    def __init__(self, old_md_path: Path):

        self.stem: str = old_md_path.stem

        self.new_dir: Path = new_portfolio_dir/self.stem

        self.old_md_path: Path = old_md_path
        self.new_md_path: Path = self.new_dir/"contents.md"
        self.old_data_path: Path = old_data_dir / (self.stem + ".json")
        self.new_data_path: Path = self.new_dir/"data.json"
        self.old_list_images: List[Path] = []
        self.get_images()

    def get_images(self):

        for image in old_images_dir.iterdir():
            if self.stem in image.stem:
                self.old_list_images.append(image)

    def create_new_file_structure(self):

        mkdir(self.new_dir)
        self.repoint_image_links()
        for image_path in self.old_list_images:
            copy2(image_path, self.new_dir/image_path.name)

    def repoint_image_links(self):

        with self.old_md_path.open("r") as old_md_fh:
            file_data = old_md_fh.read()

        file_data = file_data.replace("images/", str(self.stem) + "/")

        with self.new_md_path.open("w") as new_md_fh:
            new_md_fh.write(file_data)

        with self.old_data_path.open("r") as old_md_fh:
            file_data = old_md_fh.read()

        file_data = file_data.replace("images/", str(self.stem) + "/")

        with self.new_data_path.open("w") as new_md_fh:
            new_md_fh.write(file_data)


# x restructure the folder
# x substitute the strings
# do for all
# change path for default image
# modify the renderer
# check each page worked
# delete the old
for old_md_path in old_md_dir.iterdir():
    # if "targeted" in old_md_path.stem:
    blog_post = BlogPost(old_md_path)
    blog_post.create_new_file_structure()
    print(blog_post.old_list_images)
