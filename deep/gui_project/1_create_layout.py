import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("500x600")

# file frame(file add, delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx= 5, pady = 5, width = 12, text = "file add")
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx= 5, pady = 5, width = 12, text = "selection delete")
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

btn_dest_path = Button(path_frame, text = "finding out", width = 10)
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

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12)
btn_start.pack(side = "right", padx = 5, pady = 5)

root.mainloop() # keep window opening