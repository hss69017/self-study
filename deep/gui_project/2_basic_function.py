import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # __all__에 없기 때문

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("500x600")

# add file
def add_file():
    files = filedialog.askopenfilenames(title = "Choose your image file(s).", filetypes = (("PNG file", "*.png"), ("all file", "*.*")), \
        initialdir = "/Users/gunju/Desktop/self study/python/deep/pygame_project/images") # initial file path
    
    # file list chosen by user
    for file in files:
        list_file.insert(END, file)

# delete file / 뒤에서 지워야 함. 앞에서부터 지우면 index가 달라지기 때문
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()): # reverse()는 원래 값을 바꾸지만, reversed()는 새로운 값을 return
        list_file.delete(index)

# saving path (directory)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == None: # when user select cancel
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# start
def start():
    # check each option
    print("width: ", cmb_width.get())
    print("interval: ", cmb_interval.get())
    print("format: ", cmb_format.get())

    # check whether it has the file in the list
    if list_file.size() == 0:
        msgbox.showwarning("warning", "Add your image file(s).")
        return

    # check whether it has the saving path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("warning", "Select the saving path.")
        return

# file frame(file add, delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx= 5, pady = 5, width = 12, text = "file add", command = add_file)
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx= 5, pady = 5, width = 12, text = "selection delete", command = del_file)
btn_del_file.pack(side = "right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill = "both", padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = list_file.yview)

# saving path frame
path_frame = LabelFrame(root, text = "saving path", relief = "solid")
path_frame.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 4) # ipady: change height

btn_dest_path = Button(path_frame, text = "finding out", width = 10, command = browse_dest_path)
btn_dest_path.pack(side = "right", padx = 5, pady = 5)

# option frame
frame_option = LabelFrame(root, text = "option")
frame_option.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

# 1. width option
# width label
lbl_width = Label(frame_option, text = "width", width = 4)
lbl_width.pack(side = "left", expand = True, padx = 5, pady = 5)

# width combobox
opt_width = ["original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = "left", expand = True, padx = 5, pady = 5)

# 2. interval option
# interval option label
lbl_interval = Label(frame_option, text = "interval", width = 5)
lbl_interval.pack(side = "left", expand = True, padx = 5, pady = 5)

# interval option combobox
opt_interval = ["none", "narrow", "normal", "wide"]
cmb_interval = ttk.Combobox(frame_option, state = "readonly", values = opt_interval, width = 10)
cmb_interval.current(0)
cmb_interval.pack(side = "left", expand = True, padx = 5, pady = 5)

# 3. file format option
# file format option label
lbl_format = Label(frame_option, text = "format", width = 5)
lbl_format.pack(side = "left", expand = True, padx = 5, pady = 5)

# file format option combobox
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values = opt_format, width = 10)
cmb_format.current(0)
cmb_format.pack(side = "left", expand = True, padx = 5, pady = 5)

# progress bar
frame_progress = LabelFrame(root, text = "progress state")
frame_progress.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = "x", padx = 5, pady = 5)

# execution frame
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "close", width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12, command = start)
btn_start.pack(side = "right", padx = 5, pady = 5)

root.mainloop() # keep window opening