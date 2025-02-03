from config import danmaku_box
import os
import shutil
import re
from utils import save_d_to_file, get_comments_from_xml

pattern = re.compile(r"^p(\d+) (\d+) ")
for subfolder in os.scandir(danmaku_box):
    subfolder_path = subfolder.path
    if subfolder.is_dir():
        match = pattern.match(os.path.basename(subfolder_path))
        if match:
            d_elements = []
            for filename in os.listdir(subfolder_path):
                if filename.endswith(".xml"):
                    for comment in get_comments_from_xml(
                        os.path.join(subfolder_path, filename)
                    ):
                        p = comment.get("p")
                        parts = p.split(",")
                        d_elements.append((parts[0], comment.text))

            save_d_to_file(
                d_elements, os.path.join(danmaku_box, f"{match.group(2).zfill(2)}.xml")
            )

        shutil.rmtree(subfolder_path)
    else:
        os.remove(subfolder_path)
