#フォルダー選択後固定間隔で表示
import tkinter.filedialog
from tkinter import filedialog as tkFileDialog
import os
import sys
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
def view_image():
    global item, canvas
 
    root = tkinter.Tk()
    root.title('test')
    root.geometry("450x350")
    root.mainloop()
def jpg_select():
    ini_dir = 'C:'
    ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
    print(str(ret))
    os.chdir(str(ret))
    files = []
    files = glob.glob('*.jpg')
    print(files)
    for n in files:
        img2 = Image.open(n)
        img2 = img2.resize((400,300),Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        canvas = tkinter.Canvas(bg = "white", width=400, height=300)
        canvas.place(x=0, y=0)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        time.sleep(1) 
        canvas.itemconfig(item,image=img2)
 
thread1 = threading.Thread(target=view_image)
thread1.start()
 
thread2 = threading.Thread(target=jpg_select)
thread2.start()

