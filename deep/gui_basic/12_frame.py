from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

Label(root, text = "Select your food").pack(side = "top")

Button(root, text = "order").pack(side = "bottom")

frame_burger = Frame(root, relief = "solid", bd = 1) # relief: shape of the boundary, bd = thickness of the boundary
frame_burger.pack(side = "left", fill = "both", expand = True) # fill: side가 왼쪽이기 때문에 위아래로 꽉참, expand: 창을 꽉 채움

Button(frame_burger, text = "hamburger").pack()
Button(frame_burger, text = "cheeseburger").pack()
Button(frame_burger, text = "chickenburger").pack()

frame_drink = LabelFrame(root, text = "drink") # frame with title
frame_drink.pack(side = "right", fill = "both", expand = True)
Button(frame_drink, text = "cola").pack()
Button(frame_drink, text = "cider").pack()

root.mainloop() # keep window opening