
import cv2
from PIL import Image, ImageTk

import tkinter.filedialog
import tkinter as tk  # 使用Tkinter前需要先导入
import os
import threading
import time
#img_open = cv2.imread('1.jpg')
#cv2image = cv2.cvtColor(img_open, cv2.COLOR_BGR2RGBA)

 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x800')  # 这里的乘是小x

pathh = tk.StringVar()

canvas1 = tk.Canvas(window, bg='green', height=300, width=400)
canvas1.place(x=50, y=100, anchor='nw')
image1 = canvas1.create_image(200, 0, anchor='n')

canvas2 = tk.Canvas(window, bg='green', height=300, width=400)
canvas2.place(x=550, y=100, anchor='nw')
image2 = canvas2.create_image(200, 0, anchor='n')

canvas3 = tk.Canvas(window, bg='green', height=300, width=400)
canvas3.place(x=50, y=450, anchor='nw')
image3 = canvas3.create_image(200, 0, anchor='n')

canvas4 = tk.Canvas(window, bg='green', height=300, width=400)
canvas4.place(x=550, y=450, anchor='nw')
image4 = canvas4.create_image(200, 0, anchor='n')


def selectPath():
    global pathh
    filesname = []
    #选择文件path_接收文件地址
    path = tkinter.filedialog.askdirectory()
    print
    
    #通过replace函数替换绝对文件地址中的/来使文件可被程序读取 
    #注意：\\转义后为\，所以\\\\转义后为\\
    path=path.replace("/","\\\\")
    #path设置path_的值
    pathh.set(path)
    dirs = os.listdir(path)
    for i in dirs:
        if os.path.splitext(i)[1] == ".jpg" or os.path.splitext(i)[1] == ".png" or os.path.splitext(i)[1] == ".JPG" or os.path.splitext(i)[1] == ".jpeg":
            filesname+=[path+'/'+i]
 
    global canvas1, canvas2, canvas3, canvas4, image1, image2

    addImage2Canvas(canvas1, image1, filesname[0])
    
    addImage2Canvas(canvas2, image2, filesname[0])
    
    # threading.Thread(target=addImage2Canvas,args=(canvas1, image1, filesname[0])).start()
    
    # threading.Thread(target=addImage2Canvas,args=(canvas2, image2, filesname[1])).start()

    # threading.Thread(target=addImage2Canvas,args=(canvas3, image3, filesname[2])).start()

    # threading.Thread(target=addImage2Canvas,args=(canvas4, image4, filesname[3])).start()

def addImage2Canvas(canvas, image, filesname):
    img_open = Image.open(filesname)    
    image_file = create(img_open)
    canvas.itemconfigure(image, image=image_file)
    canvas.update()

def print_selection():
    print('you have selected ' + var.get())


def create(img_open):
    global box
    region = img_open.crop(box)     

    region1 = region.resize((400, 300))

    image_file = ImageTk.PhotoImage(image = region1)
    return image_file


def putimage():
    global canvas1,canvas2,canvas3,canvas4
    # global box
    # canvas1.delete()
    # canvas2.delete()
    # canvas3.delete()
    # canvas4.delete()
    # canvas1 = tk.Canvas(window,  height=300, width=400)
    # #image_file = tk.PhotoImage(file='1.jpg')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
    # image1 = canvas1.create_image(200, 0, anchor='n',image=image_file1)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
    # canvas1.place(x=50, y=100, anchor='nw')

    # canvas2 = tk.Canvas(window,height=300, width=400)
    # #image_file = tk.PhotoImage(file='1.jpg')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
    # image2 = canvas2.create_image(200, 0, anchor='n',image=image_file2)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
    # canvas2.place(x=550, y=100, anchor='nw')

    # canvas3 = tk.Canvas(window,  height=300, width=400)
    # #image_file = tk.PhotoImage(file='1.jpg')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
    # image3 = canvas3.create_image(200, 0, anchor='n',image=image_file3)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
    # canvas3.place(x=50, y=450, anchor='nw')

    # canvas4 = tk.Canvas(window, height=300, width=400)
    # #image_file = tk.PhotoImage(file='1.jpg')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
    # image4 = canvas4.create_image(200, 0, anchor='n',image=image_file4)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
    # canvas4.place(x=550, y=450, anchor='nw')
    # 第7步，主窗口循环显示

# def hit_me():
#     global var1,var2,var3,var4,var,box

#     print(var1.get(),var2.get(),var3.get(),var4.get(),var.get())
#     print(box)

# b = tk.Button(window, text='upload(点一下就行)', font=('Arial', 12), command=hit_me)
# b.place(x=550, y=25, anchor='w')



loc = []

scale = 10

box = (0, 0, 400*scale, 300*scale)              ##确定拷贝区域大小

def drag(event):
    global box
    global img_open
    global image_file1,image_file2,image_file3,image_file4
    global loc
    global scale
    nowloc=[]
    nowloc.append(event.x)
    nowloc.append(event.y)
    loc.append(nowloc)
    if (len(loc) >= 3):
        del loc[0]

    #print (loc)
 
    boxx = list(box)
    if (len(loc) == 2):
        if boxx[0]+(loc[0][0]-loc[1][0])*scale<=0:
            boxx[0] = 0
        elif boxx[0]+(loc[0][0]-loc[1][0])*scale>= 4032-400*scale:
            boxx[0] = 4032-400*scale
        else:
            boxx[0] = boxx[0]+(loc[0][0]-loc[1][0])*scale

        if boxx[1]+(loc[0][1]-loc[1][1])*scale <= 0:
            boxx[1] = 0
        elif boxx[1]+(loc[0][1]-loc[1][1])*scale>= 3024-300*scale:
            boxx[1]= 3024-300*scale
        else:
            boxx[1] = boxx[1]+(loc[0][1]-loc[1][1])*scale

        boxx[2] = boxx[0] +400*scale
        boxx[3] = boxx[1] +300*scale

        box = tuple(boxx)
        image_file1 = create(img_open1)
        image_file2 = create(img_open2)
        image_file3 = create(img_open3)
        image_file4 = create(img_open4)
        # region = img_open.crop(box)     

        # region1 = region.resize((400, 300))

        # image_file = ImageTk.PhotoImage(image = region1)

        putimage()

def callback(event): 
    print("当前位置：",event.x,event.y)

#frame = tk.Frame(window, width = 1000, height = 800)

# def sett(event):
#     x = event.x
#     y = event.y
# #def scale(event):
# window.bind("<Button-1>",sett)
def scaler(event):
    global scale
    global box
    global img_open
    global image_file1,image_file2,image_file3,image_file4
    boxx = list(box)

    oldscale = scale
    # print (oldscale)
    if(event.delta > 0 and oldscale >1):
        scale = max(oldscale-1,1)
        boxx[0] = boxx[0] + event.x
        boxx[1] = boxx[1] + event.y
  
    if(event.delta < 0 and oldscale < 10):
        scale = min(oldscale+1,10)
        if (boxx[0] - event.x <0):
            boxx[0]=0
        elif(boxx[0] - event.x > 4032-400*scale):
            boxx[0]=4032-400*scale
        else:
            boxx[0] = boxx[0] - event.x
        
        if (boxx[1] - event.y <0):
            boxx[1]=0
        elif(boxx[1] - event.y > 3024-300*scale):
            boxx[1]=3024-300*scale
        else:
            boxx[1] = boxx[1] - event.y
        # boxx[0] = min(boxx[0] - event.x , 4032-400*scale)
 
        # boxx[1] = min(boxx[1] - event.y , 3024-300*scale)

    boxx[2] = boxx[0]+400*scale
    boxx[3] = boxx[1]+300*scale
    #print (scale)
    box = tuple(boxx)

    image_file1 = create(img_open1)
    image_file2 = create(img_open2)
    image_file3 = create(img_open3)
    image_file4 = create(img_open4)
    # region = img_open.crop(box)     

    # region1 = region.resize((400, 300))

    # image_file = ImageTk.PhotoImage(image = region1)

    putimage()

    
def locclear(event):
    global loc
    loc.clear()

# if(len(filesname) != 0 ):
#     window.bind("<MouseWheel>",scaler)
#     window.bind("<B1-Motion>",drag)
#     window.bind("<ButtonRelease-1>",locclear)

#输入框，标记，按键
tk.Label(window,text = "目标路径:").place(x=550, y=75, anchor='w')
#输入框绑定变量path
tk.Entry(window, textvariable = pathh).place(x=620, y=75,width = 250, anchor='w')
tk.Button(window, text = "路径选择", command = selectPath).place(x=900, y=75, anchor='w')

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
r1 = tk.Radiobutton(window, text='noise', variable=var, value='noise', command=print_selection)
r1.place(x=50, y=50, anchor='w')
r2 = tk.Radiobutton(window, text='detail', variable=var, value='detail', command=print_selection)
r2.place(x=175, y=50, anchor='w')
r3 = tk.Radiobutton(window, text='baoguang', variable=var, value='baoguang', command=print_selection)
r3.place(x=300, y=50, anchor='w')
r4 = tk.Radiobutton(window, text='color', variable=var, value='color', command=print_selection)
r4.place(x=425, y=50, anchor='w')

var1 = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.

# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r11 = tk.Radiobutton(window, text='1', variable=var1, value=1)
r11.place(x=90, y=425, anchor='w')
r21 = tk.Radiobutton(window, text='2', variable=var1, value=2)
r21.place(x=160, y=425, anchor='w')
r31 = tk.Radiobutton(window, text='3', variable=var1, value=3)
r31.place(x=230, y=425, anchor='w')
r41 = tk.Radiobutton(window, text='4', variable=var1, value=4)
r41.place(x=300, y=425, anchor='w')
r51 = tk.Radiobutton(window, text='5', variable=var1, value=5)
r51.place(x=370, y=425, anchor='w')

var2 = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r12 = tk.Radiobutton(window, text='1', variable=var2, value=1)
r12.place(x=590, y=425, anchor='w')
r22 = tk.Radiobutton(window, text='2', variable=var2, value=2)
r22.place(x=660, y=425, anchor='w')
r32 = tk.Radiobutton(window, text='3', variable=var2, value=3)
r32.place(x=730, y=425, anchor='w')
r42 = tk.Radiobutton(window, text='4', variable=var2, value=4)
r42.place(x=800, y=425, anchor='w')
r52 = tk.Radiobutton(window, text='5', variable=var2, value=5)
r52.place(x=870, y=425, anchor='w')

var3 = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r13 = tk.Radiobutton(window, text='1', variable=var3, value=1)
r13.place(x=90, y=775, anchor='w')
r23 = tk.Radiobutton(window, text='2', variable=var3, value=2)
r23.place(x=160, y=775, anchor='w')
r33 = tk.Radiobutton(window, text='3', variable=var3, value=3)
r33.place(x=230, y=775, anchor='w')
r43 = tk.Radiobutton(window, text='4', variable=var3, value=4)
r43.place(x=300, y=775, anchor='w')
r53 = tk.Radiobutton(window, text='5', variable=var3, value=5)
r53.place(x=370, y=775, anchor='w')

var4 = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r14 = tk.Radiobutton(window, text='1', variable=var4, value=1)
r14.place(x=590, y=775, anchor='w')
r24 = tk.Radiobutton(window, text='2', variable=var4, value=2)
r24.place(x=660, y=775, anchor='w')
r34 = tk.Radiobutton(window, text='3', variable=var4, value=3)
r34.place(x=730, y=775, anchor='w')
r44 = tk.Radiobutton(window, text='4', variable=var4, value=4)
r44.place(x=800, y=775, anchor='w')
r54 = tk.Radiobutton(window, text='5', variable=var4, value=5)
r54.place(x=870, y=775, anchor='w')



window.mainloop()