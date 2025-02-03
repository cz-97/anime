from collections import defaultdict
import os
from config import dandanplay, danmaku_box, danmaku
from utils import get_comments_from_xml, save_d_to_file

for filename in set(os.listdir(dandanplay)) & set(os.listdir(danmaku_box)):
    if filename.endswith(".xml"):

        print(filename)
        comments = []
        text_dict = defaultdict(set)

        for index, folder in enumerate([dandanplay, danmaku_box]):
            file_path = os.path.join(folder, filename)
            for comment in get_comments_from_xml(file_path):
                time_accurate = comment.get("p").split(",")[0]
                time = int(float(time_accurate))
                text = comment.text
                if index == 1 and text in text_dict[time]:
                    continue
                comments.append((time_accurate, text))
                text_dict[time].add(text)
            os.remove(file_path)
        save_d_to_file(comments, os.path.join(danmaku, filename))
