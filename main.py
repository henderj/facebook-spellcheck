import json
from json import encoder
from typing import Dict, Any
from facebook import GraphAPI
import requests
from secrets import accessToken
from spellcheck import put_text_into_spellboy
from ui import SpellcheckUI

# santiago
page_id = 112473910504378


def retrive_posts() -> Dict:
    graph = GraphAPI(access_token=accessToken, version=2.12)
    posts = graph.request(f"{page_id}/posts")
    return posts


def save_posts_to_file(posts: Dict) -> None:
    js_text = json.dumps(posts, indent=2)
    with open("posts.json", "w", encoding="utf-8") as f:
        f.write(js_text)


def retrive_posts_from_file() -> Dict:
    with open("posts.json") as f:
        data = f.read()
    js = json.loads(data)
    return js


def update_post(post_id: int, message: str) -> Any:
    payload = {
        "message": message,
    }
    graph = GraphAPI(access_token=accessToken, version=2.12)
    result = graph.request(f"{post_id}/", post_args=payload)
    return result


def main():
    data = retrive_posts_from_file()
    posts = data["data"]
    ui = SpellcheckUI(posts)
    ui.display()
    # first_post = posts[0]
    # first_m = first_post["message"]
    # print(first_m)
    # post_id = first_post["id"]
    # print(post_id)
    # new_text = put_text_into_spellboy(first_m)
    # result = update_post(post_id, new_text)
    # print(result)


if __name__ == "__main__":
    main()
