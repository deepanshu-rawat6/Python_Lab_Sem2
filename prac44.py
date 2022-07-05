from tkinter import *
from tkinter import messagebox

x = Tk()
x.geometry("450x200")


def add(addition):
    messagebox.showinfo("Sum", "Sum of the numbers:", addition)


n = int(input("Enter no 1:"))
m = int(input("Enter no 2:"))

addition = n + m

btn1 = Button(x, text="Compute Sum", command=add)
btn1.pack()
x.mainloop()
