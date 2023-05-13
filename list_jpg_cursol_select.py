import tkinter


from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from tkinter import filedialog as tkFileDialog
from PIL import Image, ImageTk


class image_gui():
    def __init__(self):  
        button= ttk.Button(win, text=u'jpgファイル選択', command=self.file_selected)  
        button.pack()
        button.place(x=10, y=10)


    #----------------------------------------
    def select_lb(self,event):
        for i in self.lb.curselection():
            print(self.filenames[i])
            self.prev_image(self.filenames[i])
    #----------------------------------------


    def file_selected(self):  




        fTyp = [('', '*')]
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        #print(self.filenames[0])
     
 
        txt = StringVar(value=self.filenames)
        self.lb= Listbox(win, listvariable=txt,width=80,height=6)
        self.lb.bind('<<ListboxSelect>>', self.select_lb)
        self.lb.grid(row=0, column=1)
        self.lb.configure(selectmode="extended")
        scrollbar = ttk.Scrollbar(win,orient=VERTICAL,command=self.lb.yview)
        scrollbar.grid(row=0,column=2,sticky=(N,S))


    def prev_image(self,n):






        self.sizevalid=0
   
        img2 = Image.open(n)
        x = 300
        y = 300
        img2.thumbnail((x, y), Image.ANTIALIAS)


        img2 = ImageTk.PhotoImage(img2)


        canvas = tkinter.Canvas(width=600, height=500)
        #canvas.pack()
        canvas.place(x=100, y=300)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)


        win.mainloop()




win = Tk()
win.title('test')
win.geometry("800x600")
image_gui()
 
win.mainloop()