import time
import tkinter.ttk as ttk
from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# indeterminate: undecided about end time, bar is keep moving / determinate: decided about end time, bar is moving until full
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# progressbar.start(10) # move every 10ms
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text = "stop", command = btncmd)
# btn.pack()

p_var2 = DoubleVar() # It should be not only int, but also real number 
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2) # length: length of the bar
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # wait for 0.01 sec

        p_var2.set(i) # set the value of the bar
        progressbar2.update() # update the ui
        print(p_var2.get())

btn = Button(root, text = "start", command = btncmd2)
btn.pack()

root.mainloop() # keep window opening