from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

Label(root, text = "Select your food.").pack()

burger_var = IntVar()
# The things that have same variable are in the same group
btn_burger1 = Radiobutton(root, text = "hamburger", value = 1, variable = burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = "cheeseburger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "chickenburger", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "Select your drink.").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "cola", value = "cola", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "cider", value = "cider", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # The result starts from 1, not 0
    print(drink_var.get())

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop() # keep window opening