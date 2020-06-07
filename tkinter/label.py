from tkinter import *

root = Tk()
"""
root.title("Label")
root.resizable(1, 1)

text = StringVar()
text.set("New text")

# Label(root, text="Hello World!").pack(side="left")
# Label(root, text="Line 2!").pack()
# Label(root, text="Line 3!").pack(side="right")
Label(root, text="Hello World!").pack(anchor="nw")
label = Label(root, text="Line 2!")
label.pack(anchor="center")
Label(root, text="Line 3!").pack(anchor="se")


label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable=text)
"""
image = PhotoImage(file="hello.gif")
Label(root, image=image).pack(side="left")
root.mainloop()
