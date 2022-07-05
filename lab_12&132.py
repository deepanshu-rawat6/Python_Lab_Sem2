from tkinter import *
from tkinter import messagebox

SUDO = Tk()
entry = Entry(SUDO)
SUDO.title("GUI Window")

def show_name():
    username = entry.get()
    label = Label(SUDO, text=username)
    label.grid(row=6, column=1)


def func():
    messagebox.showinfo('INFO', f'You have clicked {str(var.get())}st')


var = IntVar()
RB1 = Radiobutton(SUDO, text="first choice", value=1, command=func, variable=var)
RB1.grid(row=1, column=0)
RB2 = Radiobutton(SUDO, text="second choice", value=2, command=func, variable=var)
RB2.grid(row=1, column=1)
RB3 = Radiobutton(SUDO, text="third choice", value=3, command=func, variable=var)
RB3.grid(row=1, column=2)
btn1 = Button(SUDO, text="Show", command=show_name)
btn1.grid()
entry.grid(row=2, column=1)
SUDO.mainloop()
