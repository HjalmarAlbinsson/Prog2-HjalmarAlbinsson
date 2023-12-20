import sweet_home_alabama
from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

b = Button(root, text ="Make a new Baby!")

def click_handler(self):
    b.config(text="Parent")
    lbl["text"] = "Du skrev: " + e.get()

b.bind("<Button-1>", click_handler)
b.pack()

lbl = Label(root)
lbl.pack()
root.geometry("500x500")
root.mainloop()