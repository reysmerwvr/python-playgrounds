import sqlite3
from tkinter import *

root = Tk()
root.title("Super Restaurant")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")

Label(root, text="   Super restaurant   ", fg="darkgreen", font=("Consolas", 28, "bold italic")).pack()
Label(root, text="Menu", fg="green", font=("Consolas", 24, "bold italic")).pack()

Label(root, text="").pack()

connexion = sqlite3.connect("../database/restaurant.db")
pointer = connexion.cursor()

categories = pointer.execute("SELECT * FROM category").fetchall()
for category in categories:
    Label(root, text=category[1], fg="black", font=("Consolas", 20, "bold italic")).pack()
    dishes = pointer.execute("SELECT * FROM dish WHERE category_id={}".format(category[0])).fetchall()
    for dish in dishes:
        Label(root, text=dish[1], fg="grey", font=("Consolas", 15, "italic")).pack()
    Label(root, text="").pack()

connexion.close()

Label(root, text="$15 (Tax included)", fg="darkgreen", font=("Consolas", 20, "italic")).pack(side="right")

root.mainloop()
