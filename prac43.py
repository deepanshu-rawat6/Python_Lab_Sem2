from tkinter import *
from tkinter import messagebox

x = Tk()
x.geometry("450x250")


def fun():
    messagebox.showinfo("Alret!", "Your clicked button")


btn1 = Button(x, text="Click Me!!", command=fun, activeforeground="green", activebackground="red", pady=10)
btn1.pack()
x.mainloop()
