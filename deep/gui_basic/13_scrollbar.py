from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")

listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set)
# without set, scrollbar doesn't work
for i in range(1, 32):
    listbox.insert(END, str(i))
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview) # 이게 있어야 listbox랑 매칭이 됨

root.mainloop() # keep window opening