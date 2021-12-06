from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def a():
	global lb, root
	lb.pack_forget()
	bg = PhotoImage(file="img.png")
	lb = Label(root)
	lb.imgtk = bg
	lb.configure(imgtk=bg)
	lb.pack()


Button(root, text="xx", command=lambda: a()).pack()
bg = PhotoImage(file="img.png")
lb = Label(root)
lb.imgtk = bg
lb.configure(imgtk=bg)
lb.pack()

root.mainloop()