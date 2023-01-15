from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

def create_new_file():
    print("create a new file")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "New File", command = create_new_file)
menu_file.add_command(label = "New Window")
menu_file.add_separator()
menu_file.add_command(label = "Open File...")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state = "disable") # deactivated
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit)
menu.add_cascade(label = "File", menu = menu_file)

menu_edit = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = menu_edit) # empty menu

menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu = menu_lang)

menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view)

root.config(menu = menu)
root.mainloop() # keep window opening