from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 0)
# extended: can select many things, single: can select only 1 thing
# if height is 0 then show everything in the list, if height is # then show # things in the list
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon") # insert ~ at the end of the list
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(0) # #: delete the #th thing in the list, END: delete the last thing in the list

    # print("In the list, there is(are)", listbox.size(), "thing(s).")

    # print("The 1st ~ 3rd things in the list:", listbox.get(0, 2))

    print("the selected thing(s):", listbox.curselection()) # return the place(s)(index) of the selected thing(s)

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop() # keep window opening