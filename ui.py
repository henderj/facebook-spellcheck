import tkinter as tk

class SpellcheckUI:
    def display(self):
        self.window = tk.Tk()
        text_box = tk.Text()
        text_box.pack()
        self.window.mainloop()
        

if __name__ == "__main__":
    sp = SpellcheckUI()
    sp.display()