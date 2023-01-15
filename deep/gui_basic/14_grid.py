from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image # pip3 install pillow (image)

root = Tk()
root.title("GJ GUI") # title of the program
root.geometry("640x480")

# btn1 = Button(root, text = "button 1")
# btn2 = Button(root, text = "button 2")

# btn1.pack()
# btn2.pack()

# btn1.pack(side = "left")
# btn2.pack(side = "left")

# btn1.grid(row = 0, column = 0)
# btn2.grid(row = 1, column = 1)

btn_f16 = Button(root, text = "F16", padx = 10, pady = 10)
# padx, y: 글자 제외 여백주기, 글자에 따라 버튼 크기가 달라지기 때문에 같게 만드려면 width, height를 쓰자
btn_f17 = Button(root, text = "F17", padx = 10, pady = 10)
btn_f18 = Button(root, text = "F18", padx = 10, pady = 10)
btn_f19 = Button(root, text = "F19", padx = 10, pady = 10)

btn_f16.grid(row = 0, column = 0, sticky = N + E + W + S, padx = 3, pady = 3)
# sticky: 지정한 방향으로 칸을 붙여라 / padx, y: 버튼 간 공간
btn_f17.grid(row = 0, column = 1, sticky = N + E + W + S, padx = 3, pady = 3)
btn_f18.grid(row = 0, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_f19.grid(row = 0, column = 3, sticky = N + E + W + S, padx = 3, pady = 3)

btn_clear = Button(root, text = "clear", padx = 10, pady = 10)
btn_equal = Button(root, text = "=", padx = 10, pady = 10)
btn_div = Button(root, text = "/", padx = 10, pady = 10)
btn_mul = Button(root, text = "*", padx = 10, pady = 10)

btn_clear.grid(row = 1, column = 0, sticky = N + E + W + S, padx = 3, pady = 3)
btn_equal.grid(row = 1, column = 1, sticky = N + E + W + S, padx = 3, pady = 3)
btn_div.grid(row = 1, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_mul.grid(row = 1, column = 3, sticky = N + E + W + S, padx = 3, pady = 3)

btn_7 = Button(root, text = "7", padx = 10, pady = 10)
btn_8 = Button(root, text = "8", padx = 10, pady = 10)
btn_9 = Button(root, text = "9", padx = 10, pady = 10)
btn_sub = Button(root, text = "-", padx = 10, pady = 10)

btn_7.grid(row = 2, column = 0, sticky = N + E + W + S, padx = 3, pady = 3)
btn_8.grid(row = 2, column = 1, sticky = N + E + W + S, padx = 3, pady = 3)
btn_9.grid(row = 2, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_sub.grid(row = 2, column = 3, sticky = N + E + W + S, padx = 3, pady = 3)

btn_4 = Button(root, text = "4", padx = 10, pady = 10)
btn_5 = Button(root, text = "5", padx = 10, pady = 10)
btn_6 = Button(root, text = "6", padx = 10, pady = 10)
btn_add = Button(root, text = "+", padx = 10, pady = 10)

btn_4.grid(row = 3, column = 0, sticky = N + E + W + S, padx = 3, pady = 3)
btn_5.grid(row = 3, column = 1, sticky = N + E + W + S, padx = 3, pady = 3)
btn_6.grid(row = 3, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_add.grid(row = 3, column = 3, sticky = N + E + W + S, padx = 3, pady = 3)

btn_1 = Button(root, text = "1", padx = 10, pady = 10)
btn_2 = Button(root, text = "2", padx = 10, pady = 10)
btn_3 = Button(root, text = "3", padx = 10, pady = 10)
btn_enter = Button(root, text = "enter", padx = 10, pady = 10)

btn_1.grid(row = 4, column = 0, sticky = N + E + W + S, padx = 3, pady = 3)
btn_2.grid(row = 4, column = 1, sticky = N + E + W + S, padx = 3, pady = 3)
btn_3.grid(row = 4, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_enter.grid(row = 4, column = 3, rowspan = 2, sticky = N + E + W + S, padx = 3, pady = 3) # rowspan: combine x ~ # row 

btn_0 = Button(root, text = "0", padx = 10, pady = 10)
btn_point = Button(root, text = ".", padx = 10, pady = 10)

btn_0.grid(row = 5, column = 0, columnspan = 2, sticky = N + E + W + S, padx = 3, pady = 3)
btn_point.grid(row = 5, column = 2, sticky = N + E + W + S, padx = 3, pady = 3)

root.mainloop() # keep window opening