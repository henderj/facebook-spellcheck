import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import N, W, E, S

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
        page_selection = ttk.Combobox(mainframe,
            textvariable=page_selection_text, 
            values=["Santiago", "Puerto Plata", "La Vega", "Navarrete"])
        page_selection.state(["readonly"])
        page_selection.bind("<<ComboboxSelected>>", self.page_changed)
        page_selection.grid(column=0, columnspan=2, row=0)
        self.page_selection = page_selection

        tk.Button(mainframe, text="load posts", command=self.paste_post)\
            .grid(column=2, row=0)

        text_box = tk.Text(mainframe, undo=True)
        text_box.grid(column=0, columnspan=3, row=1)
        self._post_text_box = text_box


        tk.Button(mainframe, text="previous", command=self.paste_post)\
            .grid(column=0, row=2)
        tk.Button(mainframe, text="update", command=self.paste_post)\
            .grid(column=1, row=2)            
        tk.Button(mainframe, text="next", command=self.paste_post)\
            .grid(column=2, row=2)

        root.mainloop()

    def page_changed(self, arg1):
        self.page_selection.selection_clear()

    def paste_post(self):
        self._post_text_box.delete("1.0", tk.END)
        self._post_text_box.insert(
            "1.0",
            "this is a test, it should be in the text box.\nwith a new line here :)",
        )


if __name__ == "__main__":
    sp = SpellcheckUI([])
    sp.display()
