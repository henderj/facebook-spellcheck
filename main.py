import json
from json import encoder
from typing import Dict, Any
from facebook import GraphAPI
import requests
from spellcheck import put_text_into_spellboy
from ui import SpellcheckUI
from pages import Page, pages
  

def retrive_posts(page: Page) -> Dict:
    page_data = pages[page.value]
    token = page_data["token"]
    id = page_data["id"]
    graph = GraphAPI(access_token=token, version=2.12)
    posts = graph.request(f"{id}/posts")
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


def update_post(page: Page, post_id: int, message: str) -> Any:
    token = pages[page.value]["token"]
    print(post_id)
    payload = {
        "message": message,
    }
    graph = GraphAPI(access_token=token, version=2.12)
    result = graph.request(f"{post_id}/", post_args=payload)
    return result


def main():
    data = retrive_posts(Page.LA_VEGA)
    posts = data["data"]
    ui = SpellcheckUI(posts, update_post)
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
