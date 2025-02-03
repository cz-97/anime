import requests
from opencc import OpenCC
from utils import save_d_to_file


# Search anime by name
def search_tvseries(anime_name):
    response = requests.get(
        f"https://api.dandanplay.net/api/v2/search/anime?keyword={anime_name}&type=tvseries"
    )

    if response.status_code == 200:
        return response.json()["animes"]
    else:
        print(f"Failed to search anime. Status code: {response.status_code}")
        return None

def get_episodes(bangumi_id):
    response = requests.get(
        f"https://api.dandanplay.net/api/v2/bangumi/{bangumi_id}"
    )
    if response.status_code == 200:
        return response.json()["bangumi"]["episodes"]
    else:
        print(f"Failed to get episodes. Status code: {response.status_code}")
        return None


# Get danmaku data for a specific episode
def get_danmaku(episode_id):
    response = requests.get(
        f"https://api.dandanplay.net/api/v2/comment/{episode_id}?withRelated=true"
    )
    if response.status_code == 200:
        return response.json()["comments"]
    else:
        print(f"Failed to retrieve comments. Status code: {response.status_code}")
        return None


# Save danmaku data to an XML file
def save_danmaku_to_file(comments, file_path):
    converter = OpenCC("t2s")
    save_d_to_file([(comment["p"].split(",")[0],converter.convert(comment["m"])) for comment in comments], file_path)
