import tkinter as tk

class SpellcheckUI:
    def display(self):
        self.window = tk.Tk()
        text_box = tk.Text()
        text_box.pack()
        self.post_text_box = text_box
        tk.Button(text='paste post', command=self.paste_post).pack()

    def paste_post(self):
        self.post_text_box.delete("1.0", tk.END)
        self.post_text_box.insert("1.0", "this is a test, it should be in the text box.\nwith a new line here :)")

    def mainloop(self):
        self.window.mainloop()
        

if __name__ == "__main__":
    sp = SpellcheckUI()
    sp.display()
    sp.mainloop()