from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

chkvar = IntVar() # Save ~ in the chkvar as the type "int"
chkbox = Checkbutton(root, text = "Do not show this message today", variable = chkvar)
# chkbox.select() # Check the checkbox automatically
# chkbox.deselect() # Uncheck the checkbox automatically
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "Do not show this message for a week", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: check X, 1: check
    print(chkvar2.get())

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop() # keep window opening