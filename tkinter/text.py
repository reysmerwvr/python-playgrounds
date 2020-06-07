from tkinter import *

root = Tk()
root.title("Text")
root.resizable(1, 1)

text = Text(root)
text.pack()
text.config(width=30, height=10, font=("Consolas", 12), padx=15, pady=15, selectbackground="red")

root.mainloop()
