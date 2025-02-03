import os
import re
from concurrent.futures import ThreadPoolExecutor
from dandanplay_api import search_tvseries, get_danmaku, save_danmaku_to_file, get_episodes
from config import dandanplay


def process_episode(episode_info):
    episode_number, episode_id = episode_info
    danmaku_data = get_danmaku(episode_id)

    if danmaku_data and len(danmaku_data) > 0:
        output_file = os.path.join(dandanplay, f"{episode_number}.xml")
        save_danmaku_to_file(danmaku_data, output_file)
        print(f"弹幕已保存到 {output_file}")
    else:
        print(f"第{episode_number}话未找到弹幕")


while True:
    animes = search_tvseries(input("请输入番剧名称: "))
    if animes and len(animes) > 0:
        break
    else:
        print("未找到相关番剧，请重新输入。")

# 循环读取用户输入，直到用户输入有效的索引
while True:
    for index, anime in enumerate(animes):
        print(f"{index + 1}. {anime['animeTitle']}")
    selected_index = input("请选择番剧: ")
    try:
        selected_index = int(selected_index) - 1
        if 0 <= selected_index < len(animes):
            break
    except ValueError:
        pass

# 提取 episode_number 和 episode_id
episodes_info = []
pattern = re.compile(r"第(\d+)话")
for episode in get_episodes(animes[selected_index]["bangumiId"]):
    episode_id = episode["episodeId"]
    episode_title = episode["episodeTitle"]
    match = pattern.match(episode_title)
    if match:
        episodes_info.append((match.group(1).zfill(2), episode_id))
    else:
        print(f"跳过剧集: id={episode_id}, 标题={episode_title}")


with ThreadPoolExecutor(max_workers=8) as executor:
    for episode_info in episodes_info:
        executor.submit(process_episode, episode_info)
