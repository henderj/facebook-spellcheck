import json
from typing import Dict
from facebook import GraphAPI
import pprint
from pprint import pp
from secrets import accessToken

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

def main_facebook_sdk():
    posts = retrive_posts_from_file()
    first_m = posts["data"][0]["message"]
    print(''.join(first_m))


def main():
    main_facebook_sdk()


if __name__ == "__main__":
    main()
