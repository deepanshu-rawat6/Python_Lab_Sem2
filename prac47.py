from tkinter import *
from tkinter import messagebox

x = Tk()
x.geometry("300x100")


def sum1():
    a = 10
    b = 20
    c = a + b
    messagebox.showinfo("SUM", c)


btn1 = Button(x, text="Print sum", command=sum1, pady=10)
btn1.pack()
x.mainloop()
