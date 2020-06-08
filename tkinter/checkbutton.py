from tkinter import *


def get_selected():
    order = ""
    if milk.get():
        order += "With milk "
    else:
        order += "Without milk "
    if sugar.get():
        order += "and sugar"
    else:
        order += "and without sugar"
    monitor.config(text=order)


root = Tk()
root.title("Coffee Shop")
root.resizable(1, 1)

milk = IntVar()
sugar = IntVar()

image = PhotoImage(file="hello.gif")
Label(root, image=image).pack(side="left")

frame = Frame(root)
frame.pack(side="right")

Label(frame, text="How do you want your coffee?").pack(anchor="w")
Checkbutton(frame, text="With milk", variable=milk, onvalue=1, offvalue=0, command=get_selected).pack(anchor="w")
Checkbutton(frame, text="With sugar", variable=sugar, onvalue=1, offvalue=0, command=get_selected).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()
