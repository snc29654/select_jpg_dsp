#2021.06.03
import sys
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font


class image_gui():  
    imgs = []
    def __init__(self, main):  
        button1 = Button(root, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=670, y=12) 


        button2 = tk.Button(root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=770, y=12) 


        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')
        label2 = tkinter.Label(root, text="インターバル(秒）", fg="red", bg="white", font=font1)
        label2.pack(side="top")
        label2.place(x=100, y=28) 


    def button1_clicked(self):  
        global interval
        interval =txt2.get()
        
        if interval=="":
            txt3.insert(tkinter.END,str(interval)+"インターバルが未設定です。")
        else:
            txt3.insert(tkinter.END,str(interval)+"秒 に設定しています。" )
                
        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        filenames = []
        filenames = glob.glob('*.jpg')
        print(filenames)

    def quit(self):
        root.destroy()




def view_image():
    global item, canvas
 
    root = tkinter.Tk()
    root.title('test')
    root.geometry("450x350")
    root.mainloop()
 
root = Tk()  
root.title("Image Viewer")  
root.geometry("850x600") 
image_gui(root)  
txt2 = tkinter.Entry(width=10)
txt2.place(x=10, y=30)
txt2.insert(tkinter.END,"1.0")


txt3 = tkinter.Entry(width=80)
txt3.place(x=10, y=60)
txt3.insert(tkinter.END,"")


root.mainloop() 


thread1 = threading.Thread(target=view_image)
thread1.start()
 


for n in filenames:
    img2 = Image.open(n)
    img2 = img2.resize((400,300),Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas = tkinter.Canvas(bg = "white", width=400, height=300)
    canvas.place(x=0, y=0)
    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
    print(interval)
    int_interval=float(interval)
    time.sleep(int_interval) 
    canvas.itemconfig(item,image=img2)