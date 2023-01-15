from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "Type") # default text, I can't use 0 instead of END

e = Entry(root, width = 30) # the difference from the text is that there is no key 'enter'
e.pack()
e.insert(0, "Type only 1 line.")

def btncmd():
    print(txt.get("1.0", END)) # 1 means line 1, 0 means 1st thing in a column, from first to END(end)
    print(e.get()) # I don't need to write "1.0", END

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop() # keep window opening