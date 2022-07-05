from tkinter import *

SUDO = Tk()
SUDO.title("GUI window using Tkinter Module")
label_name = Label(SUDO, text="Name").grid(row=0, column=0)
name = Text(SUDO, width=30, height=1, padx=10, pady=10)
name.grid(row=0, column=1, pady=30)
g = StringVar()
m = Radiobutton(SUDO, text="Male", variable=g, value="male")
f = Radiobutton(SUDO, text="Female", variable=g, value="female")
m.grid(row=6, column=0)
f.grid(row=6, column=1)
label1 = Label(SUDO, text="Qualifications:")
label1.grid(row=1, column=0)
qualifications = Listbox(SUDO, width=30, height=5)
qualifications.grid(row=1, column=1)
qualifications.insert(1, "MSc")
qualifications.insert(2, "BTech")
qualifications.insert(3, "BSc")
qualifications.insert(4, "MBA")
marks_Label = Label(SUDO, text="Marks:")
marks_Label.grid(row=2, column=0)
m1 = Text(SUDO, width=10, height=1, padx=5, pady=5)
m1.grid(row=3, column=0)
m2 = Text(SUDO, width=10, height=1, padx=5, pady=5)
m2.grid(row=3, column=1)
m3 = Text(SUDO, width=10, height=1, padx=5, pady=5)
m3.grid(row=3, column=2)


def calc():
    m1_value = m1.get("1.0", END)
    m2_value = m2.get("1.0", END)
    m3_value = m3.get("1.0", END)
    prcnt.delete(1.0, END)
    prcnt.insert(END, "Student's Name is: " + name.get("1.0", END) + "\n")
    if g.get() == "male":
        prcnt.insert(END, "He got " + str((int(m1_value) + int(m2_value) + int(m3_value)) / 3)+"%")
    elif g.get() == "female":
        prcnt.insert(END, "She got " + str((int(m1_value) + int(m2_value) + int(m3_value)) / 3)+"%")


my_button = Button(SUDO, text="Calculate", command=calc).grid(row=4, column=1)
prcnt = Text(SUDO, width=30, height=3, padx=5, pady=5)
prcnt.grid(row=5, column=1, pady=10)
SUDO.mainloop()
