from tkinter import *

x = Tk()
Label(x, text="Enter your name:").grid(row=0, column=0)
Entry(x).grid(row=0, column=1)
Label(x, text="Enter your name:").grid(row=1, column=0)
Entry(x).grid(row=1, column=1)
Button(x, text="Submit Information", fg="red").grid(row=4, column=0)
x.mainloop()
