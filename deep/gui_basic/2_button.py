from tkinter import *
from tkmacosx import Button # pip3 install tkmacosx, if it doesn't work, check the version. (Button background, fg)

root = Tk()
root.title("GJ GUI") # title of the program

btn1 = Button(root, text = "button 1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "button 222222222") # padx, pady = excluding text, secureing the place of the button
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "button 3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = "button 4444444444") # size of the button
btn4.pack()

btn5 = Button(root, fg = "blue", bg = "pink", text = "button 5") # fg = text color, bg = background color
btn5.pack()

photo = PhotoImage(file = "/Users/gunju/Desktop/self study/python/deep/gui_basic/img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("The button is clicked.")
btn7 = Button(root, text = "active button", command = btncmd)
btn7.pack()

root.mainloop() # keep window opening