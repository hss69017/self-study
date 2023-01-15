import tkinter.messagebox as msgbox
from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

def info():
    msgbox.showinfo("notice", "The reservation is completed successfully.") # title, body

def warn():
    msgbox.showwarning("warning", "That seat is full.")

def error():
    msgbox.showerror("error", "There is a payment error.")

def okcancel():
    msgbox.askokcancel("ok / cancel", "That seat is for person who is with kid. Will you make a reservation?")

def retrycancel():
    response = msgbox.askretrycancel("retry / cancel", "There is a temporary error. Will you try again?")
    print("response: ", response)
    if response == 1: # retry
        print("retry")
    elif response == 0: # cancel
        print("cancel")

def yesno():
    msgbox.askyesno("yes / no", "That seat is backward. Will you make a reservation?")

def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "The reservation is not saved. \n Will you terminate after saving?")
    print("response: ", response) # Yes: True / 1, No: False / 0, Cancel: None
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")

Button(root, command = info, text = "notice").pack()
Button(root, command = warn, text = "warning").pack()
Button(root, command = error, text = "error").pack()

Button(root, command = okcancel, text = "ok cancel").pack()
Button(root, command = retrycancel, text = "retry cancel").pack()
Button(root, command = yesno, text = "yes no").pack()
Button(root, command = yesnocancel, text = "yes no cancel").pack()

root.mainloop() # keep window opening