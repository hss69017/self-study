from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

label1 = Label(root, text = "Hello")
label1.pack()

photo = PhotoImage(file = "/Users/gunju/Desktop/self study/python/deep/gui_basic/img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "Meet again.")

    global photo2 # in method, if I want to change the image in label, I should use 'global'
    photo2 = ImageTk.PhotoImage(Image.open("/Users/gunju/Desktop/self study/python/deep/gui_basic/img2.jpeg"))
    label2.config(image = photo2)

btn = Button(root, text = "click", command = change)
btn.pack()

root.mainloop() # keep window opening