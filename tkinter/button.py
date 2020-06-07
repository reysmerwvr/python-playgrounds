from tkinter import *


# def hello():
#     print("Hello world")
#
#
# def create_label():
#     Label(root, text="Label Created Dynamically").pack()

def sum_two_numbers():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())
        result.set(number1 + number2)
        clear()
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def sub_two_numbers():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())
        result.set(number1 - number2)
        clear()
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def times_two_numbers():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())
        result.set(number1 * number2)
        clear()
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def clear():
    num1.set("")
    num2.set("")


root = Tk()
root.config(bd=15)

num1 = StringVar()
num1.set("0")
num2 = StringVar()
num2.set("0")
result = StringVar()
result.set("0")

root.title("Button")
root.resizable(1, 1)

Label(root, text="Number 1").pack()
Entry(root, justify="center", textvariable=num1).pack()
Label(root, text="Number 2").pack()
Entry(root, justify="center", textvariable=num2).pack()
Label(root, text="").pack()
Label(root, text="Result").pack()
Entry(root, justify="center", textvariable=result, state="disabled").pack()
Button(root, text="+", command=sum_two_numbers).pack(side="left")
Button(root, text="-", command=sub_two_numbers).pack(side="left")
Button(root, text="*", command=times_two_numbers).pack(side="left")


root.mainloop()
