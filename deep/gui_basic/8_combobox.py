import tkinter.ttk as ttk

from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

values = [i for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values) # values: set the possible list of the combobox
combobox.pack()
combobox.set("payment date") # original title of the combobox

readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
readonly_combobox.current(0) # select the 1st index
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text = "select", command = btncmd)
btn.pack()

root.mainloop() # keep window opening