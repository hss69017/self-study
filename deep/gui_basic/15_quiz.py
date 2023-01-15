from tkinter import *

root = Tk()
root.title("No Title - Windows Notepad")
root.geometry("640x480")

scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = txt.yview)

menu = Menu(root)

def open_file():
    mynote_txt = open("/Users/gunju/Desktop/self study/python/deep/gui_basic/mynote.txt", "r", encoding = "utf8")
    txt.delete("1.0", END)
    txt.insert(END, mynote_txt.read())
    mynote_txt.close()

def save_file():
    mynote_txt = open("/Users/gunju/Desktop/self study/python/deep/gui_basic/mynote.txt", "w", encoding = "utf8")
    print(txt.get("1.0", END), file = mynote_txt)
    mynote_txt.close()

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "Open", command = open_file)
menu_file.add_command(label = "Save", command = save_file)
menu_file.add_command(label = "Terminate", command = root.quit)
menu.add_cascade(label = "File", menu = menu_file)

menu_edit = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = menu_edit)

menu_form = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Form", menu = menu_form)

menu_view = Menu(menu, tearoff = 0)
menu.add_cascade(label = "View", menu = menu_view)

menu_help = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Help", menu = menu_help)

root.config(menu = menu)
root.mainloop()