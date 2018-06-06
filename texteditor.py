import tkinter
from tkinter import filedialog
import sys

root = tkinter.Tk("Text Editor")
text = tkinter.Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = tkinter.Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font = tkinter.Menubutton(root, text="Font")
font.grid()
font.menu = tkinter.Menu(font, tearoff=0)
font["menu"] = font.menu
helvetica = tkinter.IntVar()
courier = tkinter.IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)

root.mainloop()
