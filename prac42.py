from tkinter import *

x = Tk()
x.geometry("800x400")
Label(x, text="Enter your name:", width=40).place(x=30, y=50)
Label(x, text="Enter your age:", width=40).place(x=30, y=90)
Entry(x).place(x=240, y=50)
Entry(x).place(x=240, y=90)
x.mainloop()
