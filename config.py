import os

# 定义全局变量
res_dir = "test_resource"

danmaku = os.path.join(res_dir, "danmaku")
if not os.path.exists(danmaku):
    os.makedirs(danmaku)

dandanplay = os.path.join(danmaku, "dandanplay")
if not os.path.exists(dandanplay):
    os.makedirs(dandanplay)

danmaku_box = os.path.join(danmaku, "danmaku_box")
if not os.path.exists(danmaku_box):
    os.makedirs(danmaku_box)


# 定义随机颜色列表
colors = [
    "16711680",  # 红色 (R=255, G=0, B=0)
    "65280",  # 绿色 (R=0, G=255, B=0)
    "49151",  # 蓝色 (R=0, G=0, B=255)
    "16776960",  # 黄色 (R=255, G=255, B=0)
    "16738740",  # 品红色 (R=255, G=0, B=255)
    "65535",  # 青色 (R=0, G=255, B=255)
]
