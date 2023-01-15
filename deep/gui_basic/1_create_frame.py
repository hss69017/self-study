from tkinter import *

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480+300+100") # size(width * height), place(x, y coordinate)

root.resizable(False, False) # disallow change of the window's size(width, height)

root.mainloop() # keep window opening