from tkinter import *

SUDO = Tk()
SUDO.title('CALCULATOR using GUI')


def addition():
    ans = int(num1.get()) + int(num2.get())
    blank.insert(0, ans)


def subtract():
    ans = int(num1.get()) - int(num2.get())
    blank.insert(0, ans)


def multiply():
    ans = int(num1.get()) * int(num2.get())
    blank.insert(0, ans)


def division():
    ans = int(num1.get()) / int(num2.get())
    blank.insert(0, ans)


def clear():
    blank.delete(0, END)
    num2.delete(0, END)
    num1.delete(0, END)


def power():
    ans = int(num1.get()) ** int(num2.get())
    blank.insert(0, ans)


def modulo():
    ans = int(num1.get()) % (int(num2.get()))
    blank.insert(0, ans)


SUDO.geometry('550x100')
Label(SUDO, text="Enter Num 1:").grid(row=0)
Label(SUDO, text="Enter Num 2:").grid(row=1)
Label(SUDO, text="The Answer is:").grid(row=2)

num1 = Entry(SUDO)
num2 = Entry(SUDO)
blank = Entry(SUDO)

num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)

Button(SUDO, text='Add', command=addition).grid(row=0, column=3)
Button(SUDO, text='Subtract', command=subtract).grid(row=0, column=4)
Button(SUDO, text='Multiply', command=multiply).grid(row=0, column=5)
Button(SUDO, text='Divide', command=division).grid(row=0, column=6)
Button(SUDO, text='POW', command=power).grid(row=0, column=7)
Button(SUDO, text='Modulo', command=modulo).grid(row=0, column=8)
Button(SUDO, text='Clear', command=clear).grid(row=0, column=9)

SUDO.mainloop()
