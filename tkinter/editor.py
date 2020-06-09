from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

route = ""


def new():
    global route
    message.set("New File")
    route = ""
    text_box.delete(1.0, END)


def open_file():
    global route
    message.set("Open File")
    route = FileDialog.askopenfilename(
        initialdir=".",
        filetypes=(("File Text", "*.txt"),),
        title="Open a file text"
    )
    if route != "":
        file = open(route, "r")
        content = file.read()
        text_box.delete(1.0, END)
        text_box.insert("insert", content)
        file.close()
        root.title(route + " - Super Editor")


def save():
    global route
    message.set("Save File")
    if route != "":
        content = text_box.get(1.0, 'end-1c')
        file = open(route, "w+")
        file.write(content)
        file.close()
        message.set("Saved Successfully")
    else:
        save_as()


def save_as():
    global route
    message.set("Save As File")
    file = FileDialog.asksaveasfile(title="Save File", mode="w", defaultextension=".txt")
    if file is not None:
        route = file.name
        content = text_box.get(1.0, 'end-1c')
        file = open(route, "w+")
        file.write(content)
        file.close()
        message.set("Saved Successfully")
    else:
        message.set("Cancelled")
        route = ""

# root config


root = Tk()
root.title("Editor")

# Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Text Box
text_box = Text(root)
text_box.pack(fill="both", expand=1)
text_box.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor
message = StringVar()
message.set("Welcome to your editor")
monitor = Label(root, textvar=message, justify="left")
monitor.pack(side="left")

root.mainloop()
