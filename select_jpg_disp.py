#フォルダー選択後インターバル時間間隔で表示
import sys
import time
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

interval = 1.0
sizerate = 1.0
filenames =[]
import webbrowser
import os


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("Image Viewer")  
        self.root.geometry("850x300") 


        self.txt2 = tkinter.Entry(width=10)
        self.txt2.place(x=10, y=30)
        self.txt2.insert(tkinter.END,"1.0")
        self.txt3 = tkinter.Entry(width=80)
        self.txt3.place(x=10, y=60)
        self.txt3.insert(tkinter.END,"")

        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=330, y=30)
        self.txt4.insert(tkinter.END,"1.0")

        self.txt5 = tkinter.Entry(width=10)
        self.txt5.place(x=770, y=80)
        self.txt5.insert(tkinter.END,"1000")

        self.txt6 = tkinter.Entry(width=10)
        self.txt6.place(x=770, y=130)
        self.txt6.insert(tkinter.END,"50%")

        self.txt7 = tkinter.Entry(width=10)
        self.txt7.place(x=770, y=160)
        self.txt7.insert(tkinter.END,"50%")


        button1 = Button(self.root, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=670, y=12) 

        button3= Button(self.root, text=u'ファイル選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=670, y=42) 


        button2 = tk.Button(self.root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=770, y=12) 

        button4 = tk.Button(self.root, text = 'web実行', command=self.webslide)
        button4.grid(row=0, column=1)  
        button4.place(x=770, y=40) 

        button5 = tk.Button(self.root, text = '終了', command=self.endall)
        button5.grid(row=0, column=1)  
        button5.place(x=770, y=250) 



        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')
        label2 = tkinter.Label(self.root, text="インターバル(秒）", fg="red", bg="white", font=font1)
        label2.pack(side="top")
        label2.place(x=100, y=28) 

        label4 = tkinter.Label(self.root, text="サイズ倍率", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=400, y=28) 


        label5 = tkinter.Label(self.root, text="webインターバル(ミリ秒）", fg="black", bg="white", font=font1)
        label5.pack(side="top")
        label5.place(x=550, y=80) 

        label6 = tkinter.Label(self.root, text="web写真width", fg="black", bg="white", font=font1)
        label6.pack(side="top")
        label6.place(x=550, y=130) 

        label7 = tkinter.Label(self.root, text="web写真height", fg="black", bg="white", font=font1)
        label7.pack(side="top")
        label7.place(x=550, y=160) 


        self.root.mainloop() 

    def check_value(self):

        global interval

        self.txt3.delete(0, tk.END)      


        interval =self.txt2.get()


        global sizerate
        sizerate =self.txt4.get()
        
        if interval=="":
            self.txt3.insert(tkinter.END,str(interval)+"インターバルが未設定です。")
        else:
            self.txt3.insert(tkinter.END,str(interval)+"秒 に設定しています。" )

        if sizerate=="":
            self.txt3.insert(tkinter.END,str(sizerate)+"倍率が未設定です。")
        else:
            self.txt3.insert(tkinter.END,str(sizerate)+"倍に設定しています。" )

    def button1_clicked(self):  

        self.check_value()

        global filenames
        ini_dir = 'C:'
        self.ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(self.ret))
        os.chdir(str(self.ret))
        filenames = []
        filenames = glob.glob('*.jpg')
        print(filenames)
        self.filenames=filenames
        self.dir = 1

    def button3_clicked(self):  
        global filenames

        self.check_value()



        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)
        self.filenames=filenames
        self.dir = 0


    def quit(self):
        self.root.destroy()

    def endall(self):
        sys.exit()
        
                
    def webslide(self):

        self.interval_web =self.txt5.get()
        self.web_width =self.txt6.get()
        self.web_height =self.txt7.get()

        cwd = os.getcwd()
        
        SAMPLE_DIR = cwd
        print(cwd)
        #if not os.path.exists(SAMPLE_DIR):
        # ディレクトリが存在しない場合、ディレクトリを作成する
        #    os.makedirs(SAMPLE_DIR)       
        web_site=cwd+"\\webslide.html"
        f = open(web_site, 'w')


        datalist = []
        datalist.append('<!DOCTYPE html>\n') 
        datalist.append('<html>\n') 
        datalist.append('<head>\n') 
        datalist.append('<title> 画像表示 </title>\n') 
        datalist.append('</head>\n') 
        datalist.append('<body>\n') 
        datalist.append('<img id = \"pic\" src = \"\"  width = "') 
        datalist.append(self.web_width) 
        datalist.append('"  height = "') 
        datalist.append(self.web_height) 
        datalist.append('" >\n') 
        datalist.append('<script>\n') 
        datalist.append('const img = [\n') 

        for file in self.filenames:
            if self.dir==1:
                file=self.ret+"\\"+file
            file_c = file.replace('\\', '\\\\');
            print(file_c)
            datalist.append('"'+file_c+'",\n') 

        datalist.append('];\n') 
        datalist.append('let count = -1;\n') 
        datalist.append('jpgChange();\n') 
        datalist.append('function jpgChange()\n') 
        datalist.append('{\n') 
        datalist.append('count++;\n') 
        datalist.append('if (count == img.length) count = 0;\n') 
        datalist.append('pic.src = img[count];\n') 
        datalist.append('setTimeout(\"jpgChange()\",') 
        datalist.append(self.interval_web) 
        datalist.append(');\n') 


        datalist.append('}\n') 
        datalist.append('</script>\n') 
        datalist.append('</body>\n') 
        datalist.append('</html>\n') 

        f.writelines(datalist)

        f.close()



        webbrowser.open(web_site)



class sub_gui():
    def __init__(self):
        self.suspend_flag = 0

    def key_handler(self,e):
        
        print(e.keycode)

        if(e.keycode==38):
            self.sizeup()
        if(e.keycode==40):
            self.sizedown()

        if(e.keycode==37):
            self.speeddown()
        if(e.keycode==39):
            self.speedup()



    def suspend(self):
        self.suspend_flag = 1
    def resume(self):
        self.suspend_flag = 0

    def speedup(self):
        global interval
        if(float(interval) > 0.1):
            interval = float(interval) - 0.1

    def speeddown(self):
        global interval
        interval = float(interval) + 0.1


    def sizeup(self):
        global sizerate
        sizerate = float(sizerate) + 0.1

    def sizedown(self):
        global sizerate
        sizerate = float(sizerate) - 0.1

    def initial(self):
        #jpgの変更処理
        thread3 = threading.Thread(target=self.change_image)
        thread3.start()



    def view_image(self):
        global item, canvas
 
        self.root = tkinter.Tk()
        self.root.title('jpg viewer')
        self.root.geometry("1000x650")

        button4 = tk.Button(self.root, text = '停止', command=self.suspend)
        button4.grid(row=0, column=1)  
        button4.place(x=930, y=50) 

        button5 = tk.Button(self.root, text = '再開', command=self.resume)
        button5.grid(row=0, column=1)  
        button5.place(x=930, y=80) 

        button6 = tk.Button(self.root, text = '終了', command=self.quit)
        button6.grid(row=0, column=1)  
        button6.place(x=930, y=110) 

        button7 = tk.Button(self.root, text = '加速(->)', command=self.speedup)
        button7.grid(row=0, column=1)  
        button7.place(x=930, y=140) 

        button8 = tk.Button(self.root, text = '減速(<-)', command=self.speeddown)
        button8.grid(row=0, column=1)  
        button8.place(x=930, y=170) 

        button9 = tk.Button(self.root, text = '拡大(↑）', command=self.sizeup)
        button9.grid(row=0, column=1)  
        button9.place(x=930, y=200) 

        button10 = tk.Button(self.root, text = '縮小(↓)', command=self.sizedown)
        button10.grid(row=0, column=1)  
        button10.place(x=930, y=230) 

        button11 = tk.Button(self.root, text = '最初から', command=self.initial)
        button11.grid(row=0, column=1)  
        button11.place(x=930, y=260) 

        self.root.bind("<KeyPress>", self.key_handler)

        self.root.mainloop()
 
 
    def change_image(self):
        while(1):
            for n in filenames:
                if self.suspend_flag == 1:
                    while(1):
                        time.sleep(1)
                        if self.suspend_flag == 0:
                            break
                img2 = Image.open(n)
                before_x, before_y = img2.size[0], img2.size[1]
                x = int(round(float(300 / float(before_y) * float(before_x))))
                y = 300
                img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
                #img2 = img2.resize((900,600),Image.ANTIALIAS)
                img2 = ImageTk.PhotoImage(img2)
                canvas = tkinter.Canvas(bg = "white", width=900, height=600)
                canvas.place(x=0, y=0)
                item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
                print("size")
                print(sizerate)
                print("int")
                print(interval)
                int_interval=float(interval)
                time.sleep(int_interval) 
                canvas.itemconfig(item,image=img2)

    def quit(self):
        self.root.destroy()

image_gui()  

s=sub_gui()




#jpg表示画面を表示
thread1 = threading.Thread(target=s.view_image)
thread1.start()

#jpgの変更処理
thread2 = threading.Thread(target=s.change_image)
thread2.start()
