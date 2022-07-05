from tkinter import *
from tkinter import messagebox

SUDO = Tk()
SUDO.title("PYTHON GUI")
SUDO.geometry('400x250')


def PRINT():
    messagebox.showinfo("INFO", f'Button was clicked')


label = Label(SUDO, text="HELLO!", width=40).place(x=54, y=50)
btn1 = Button(SUDO, text="BUTTON", fg='red', bg='white', command=PRINT)
btn1.pack(side=TOP)
SUDO.mainloop()
