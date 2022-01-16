from collections import namedtuple
import json
from typing import Dict, Any
from facebook import GraphAPI 
from ui import SpellcheckUI
from pages import Page, pages
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import N, W, E, S
import webbrowser
from enum import Enum
from secrets import (
    pageToken_santiago,
    pageToken_la_vega,
    pageToken_navarrete,
    pageToken_puerto_plata,
)


class Page(Enum):
    SANTIAGO = "Santiago"
    LA_VEGA = "La Vega"
    NAVARRETE = "Navarrete"
    PUERTO_PLATA = "Puerto Plata"


PageTuple = namedtuple("PageTuple", ["id", "token"])

pages: dict[Page, PageTuple] = {
    Page.SANTIAGO: PageTuple(112473910504378, pageToken_santiago),
    Page.LA_VEGA: PageTuple(107755494333905, pageToken_la_vega),
    Page.NAVARRETE: PageTuple(107764137669344, pageToken_navarrete),
    Page.PUERTO_PLATA: PageTuple(101398454989145, pageToken_puerto_plata),
}


def retrive_posts(page: Page) -> Dict:
    page_data = pages[page]
    token = page_data.token
    id = page_data.id
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
    token = pages[page].token
    print(post_id)
    payload = {
        "message": message,
    }
    graph = GraphAPI(access_token=token, version=2.12)
    result = graph.request(f"{post_id}/", post_args=payload)
    return result


class SpellcheckUI:
    def __init__(self, posts) -> None:
        self._posts = posts

    def display(self):
        root = tk.Tk()
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=0)

        page_selection_text = StringVar(value="Select a page...")
        page_selection = ttk.Combobox(
            mainframe,
            textvariable=page_selection_text,
            values=[Page.__members__.values],
        )
        page_selection.state(["readonly"])
        page_selection.bind("<<ComboboxSelected>>", self.page_changed)
        page_selection.grid(column=0, row=0)
        self.page_selection = page_selection

        tk.Button(mainframe, text="load posts", command=self.load_posts).grid(
            column=1, row=0
        )
        tk.Button(mainframe, text="open spellboy", command=self.open_spellboy).grid(
            column=2, row=0
        )

        text_box = tk.Text(mainframe, undo=True)
        text_box.grid(column=0, columnspan=3, row=1)
        self._post_text_box = text_box

        tk.Button(mainframe, text="previous", command=self.previous_post).grid(
            column=0, row=2
        )
        tk.Button(mainframe, text="update", command=self.update_current_post).grid(
            column=1, row=2
        )
        tk.Button(mainframe, text="next", command=self.next_post).grid(column=2, row=2)

        root.mainloop()

    def page_changed(self, arg1):
        self.page_selection.selection_clear()

    def open_spellboy(self):
        webbrowser.open("www.spellboy.com", new=2)

    def load_posts(self):
        self._current_post = 0
        self.paste_post()

    def next_post(self):
        self._current_post += 1
        self.paste_post()

    def previous_post(self):
        self._current_post -= 1
        self.paste_post()

    def update_current_post(self):
        message = self._post_text_box.get("1.0", tk.END)
        post_id = self._posts[self._current_post]["id"]
        self._update_post_callback(Page.LA_VEGA, post_id, message)

    def paste_post(self):
        post = self._posts[self._current_post]
        message = post["message"]
        self._post_text_box.delete("1.0", tk.END)
        self._post_text_box.insert("1.0", message)


def main():
    data = retrive_posts(Page.LA_VEGA)
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
