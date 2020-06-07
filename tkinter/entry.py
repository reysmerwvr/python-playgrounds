from tkinter import *

root = Tk()
root.title("Entries")
root.resizable(1, 1)

label = Label(root, text="Name")
# label.grid(row=0, column=0, sticky="e")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Last Name")
# label2.grid(row=1, column=0, sticky="e")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*")

root.mainloop()
