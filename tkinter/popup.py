from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


root = Tk()
root.title("Popup")
root.resizable(1, 1)


def test():
    # MessageBox.showinfo("Hello!", "Hello World")
    # MessageBox.showwarning("Warning!", "Admin section")
    # MessageBox.showerror("Error!", "ERROR")
    # result = MessageBox.askquestion("Exit", "Are you sure you want to quit?")
    # if result == "yes":
    #     root.destroy()
    # result = MessageBox.askokcancel("Overwrite", "Are you sure to overwrite the file?")
    # if result:
    #     root.destroy()
    # result = MessageBox.askyesno("Overwrite", "Are you sure to overwrite the file?")
    # if result:
    #     root.destroy()
    # result = MessageBox.askretrycancel("Retry", "It can not connect")
    # if result:
    #     root.destroy()
    # color = ColorChooser.askcolor(title="Choose a color")
    # print(color)
    # file = FileDialog.askopenfilename(title="Open a file", initialdir="/tmp",
    #                                   filetypes=(("File text", "*.txt"),
    #                                              ("Advanced File text", "*.txt2")))
    # print(file)
    file = FileDialog.asksaveasfile(title="Save a file", mode="a+", defaultextension="txt") # equals to open('path', 'w')
    if file is not None:
        file.write("Hi from python")
        file.close()


Button(root, text="Click Me", command=test).pack()

root.mainloop()
