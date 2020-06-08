from tkinter import *


def get_selected():
    monitor.config(text="{}".format(option.get()))


def reset():
    option.set(None)
    monitor.config(text="")


root = Tk()
root.title("Radiobutton")
root.resizable(1, 1)

option = IntVar()

Radiobutton(root, text="Option 1", variable=option, value=1, command=get_selected).pack()
Radiobutton(root, text="Option 2", variable=option, value=2, command=get_selected).pack()
Radiobutton(root, text="Option 3", variable=option, value=3, command=get_selected).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reset", command=reset).pack()

root.mainloop()
