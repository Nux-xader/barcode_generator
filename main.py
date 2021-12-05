import sys, os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from barcode import EAN13
import tkinter.messagebox as msg_box
from barcode.writer import ImageWriter


root = Tk()
root.resizable(False, False)
root.title("EAN - 13 | Barcode generator")
lb3, lb4, lb5 = None, None, None


def clr():
    global view
    for x in [view, lb3, lb4, lb5]:
        try: x.pack_forget()
        except: pass

def checkdigit(code):
    x, y = 0, 0
    for i, z in enumerate(code):
        if (i+1)%2 == 0:
            x+=int(z)
        else:
            y+=int(z)
    result = ((y*3)+x)%10
    if result != 0: return 10-result
    return result


def generate():
    global root, lb3, lb4, lb5
    code_input = code.get()
    saveto_input = saveto.get()
    if len(code_input) == 12:
        if (".eps" in saveto_input) and (len(saveto_input) > 4):
            with open(f"{saveto_input.split('.eps')[0]}.jpeg", 'wb') as f:
                EAN13(code_input, writer=ImageWriter()).write(f)
            img = Image.open(f"{saveto_input.split('.eps')[0]}.jpeg")
            fig = img.convert('RGB')
            fig.save(saveto_input, "EPS")
            clr()
            print(f"{saveto_input.split('.eps')[0]}.png")
            lb3 = Label(root, text="EAN-13 Barcode:", font=('Helvetica', 12, 'bold'))
            lb4 = Label(root, image=ImageTk.PhotoImage(Image.open(f"{saveto_input.split('.eps')[0]}.png")))
            lb5 = Label(root, text=f"Check Digit: {checkdigit(code_input)}", fg="orange" ,font=('Helvetica', 12, 'bold'))
            lb3.pack(pady=5)
            lb4.pack(pady=5)
            lb5.pack(pady=5)
        else:
            msg_box.showinfo("Wrong input!", "Please enter correct file name.")
    else:
        msg_box.showinfo("Wrong input!", "Please enter correct input code.")


# declarate var
lb1 = Label(root, text="Save barcode to PS file [eg: EAN13.eps]:", font=('Helvetica', 12, 'bold'))
saveto = Entry(root)
lb2 = Label(root, text="Enter code (first 12 decimal digits):", font=('Helvetica', 12, 'bold'))
code = Entry(root)
submit = Button(root, text="Submit", command=lambda: generate())
view = Canvas(root, bg="white", height="250", width="275")


# packing
lb1.pack()
saveto.pack()
lb2.pack()
code.pack()
submit.pack(pady=5)
view.pack(pady=5, fill="both", expand=True)

root.mainloop()