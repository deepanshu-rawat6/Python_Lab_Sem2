from tkinter import *

x = Tk()
btn1 = Button(x, text="Button 1", fg="red")
btn1.pack(side=LEFT)
btn2 = Button(x, text="Button 2", fg="blue")
btn2.pack(side=RIGHT)
x.mainloop()
