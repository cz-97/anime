import os
import random
import xml.etree.ElementTree as ET

from config import colors

# 定义要处理的文件夹路径
folder_path = input("请输入文件夹路径：")

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
        file_path = os.path.join(folder_path, filename)
        # 解析XML文件
        tree = ET.parse(file_path)
        # 遍历所有d标签
        for d in tree.getroot().iter("d"):
            p = d.get("p")
            if p:
                p_list = p.split(",")
                if len(p_list) > 4:
                    # 将第3个和第4个逗号之间的值改为随机颜色
                    p_list[3] = random.choice(colors)
                    # 更新p属性
                    d.set("p", ",".join(p_list))
        # 写回XML文件
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
print("处理完成！")
