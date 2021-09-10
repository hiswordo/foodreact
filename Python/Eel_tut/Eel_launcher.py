# https://gist.github.com/Proladon/6b485c43828882f56d8fe7e5f802d590
from tkinter import *
from tkinter import font
import os, time

win = Tk()
win.minsize(200, 40)
win.maxsize(200, 40)
win.attributes('-topmost', 1)

font = font.Font(family="Eras Bold ITC", size=30) #字型

def start_py():
	os.system("python app.py") #開啟檔案
	return

btn = Button(win, text='START', command=start_py)
btn.config(width=100, font=font, relief=FLAT, activebackground='#f02468', activeforeground='white', bg='#3df2a4', fg='#323232')
btn.pack()

win.mainloop()