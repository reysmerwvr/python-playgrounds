from tkinter import *

root = Tk()
root.title("Menu")
root.resizable(1, 1)

option = IntVar()

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Close")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help")
help_menu.add_separator()
help_menu.add_command(label="Updates")

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
