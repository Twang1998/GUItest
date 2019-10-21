
import cv2
from PIL import Image, ImageTk
import numpy
import tkinter.filedialog
import tkinter as tk 
import os
import threading
import time

window = tk.Tk()
 



def getfilesname(path):
    filesname =[]
    if(path != ''):
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".jpg" or os.path.splitext(i)[1] == ".png" or os.path.splitext(i)[1] == ".JPG" or os.path.splitext(i)[1] == ".jpeg":
                filesname+=[path+'/'+i]
    else:
        filesname = []
    return filesname

def selectPath():
    global pathh
    global path
    global image_file1,image_file2,image_file3,image_file4
    global img1,img2,img3,img4
    global filesname
    global img_open1,img_open2,img_open3,img_open4
    global box,box2,box3,box4,scale
    scale =10 
    box = (0, 0, 400*scale, 300*scale)    
    box2 = box
    box3 = box
    box4 = box
    path = tkinter.filedialog.askdirectory()
    pathh.set(path)

    filesname = getfilesname(path)

    while(len(filesname) == 0 or len(filesname)%4 != 0):
        path = tkinter.filedialog.askdirectory()
        pathh.set(path)
        filesname = getfilesname(path)

    img1 = cv2.imread(filesname[0],0)
    img2 = cv2.imread(filesname[1],0)
    img3 = cv2.imread(filesname[2],0)
    img4 = cv2.imread(filesname[3],0)
    
    img_open1 = Image.open(filesname[0])
    img_open2 = Image.open(filesname[1])
    img_open3 = Image.open(filesname[2])
    img_open4 = Image.open(filesname[3])

    image_file1 = create(img_open1,box)
    image_file2 = create(img_open2,box2)
    image_file3 = create(img_open3,box3)
    image_file4 = create(img_open4,box4)

    putimage()

def print_selection():
    print('you have selected ' + var.get())

def create(img_open,box):
    region = img_open.crop(box)     

    region1 = region.resize((400, 300))

    image_file = ImageTk.PhotoImage(image = region1)
    return image_file

def putimage():
    global canvas1,canvas2,canvas3,canvas4
    global image1,image2,image3,image4
    global box

    canvas1.delete(image1)
    canvas2.delete(image2)
    canvas3.delete(image3)
    canvas4.delete(image4)

    #canvas1 = tk.Canvas(window,  height=300, width=400)
    image1 = canvas1.create_image(200, 0, anchor='n',image=image_file1)       
    #canvas1.place(x=50, y=100, anchor='nw')

    #canvas2 = tk.Canvas(window,height=300, width=400)
    image2 = canvas2.create_image(200, 0, anchor='n',image=image_file2)   
    #canvas2.place(x=550, y=100, anchor='nw')

    #canvas3 = tk.Canvas(window,  height=300, width=400)
    image3 = canvas3.create_image(200, 0, anchor='n',image=image_file3)    
    #canvas3.place(x=50, y=450, anchor='nw')

    #canvas4 = tk.Canvas(window, height=300, width=400)
    image4 = canvas4.create_image(200, 0, anchor='n',image=image_file4)      
    #canvas4.place(x=550, y=450, anchor='nw')


def hit_me():
    global var1,var2,var3,var4,var,box

    print(var1.get(),var2.get(),var3.get(),var4.get(),var.get())
    print(box)

def drag(event):
    global box,box2,box3,box4
    global img1,img2,img3,img4
    global image_file1,image_file2,image_file3,image_file4
    global loc
    global scale,flag
 
    nowloc=[]
    nowloc.append(event.x)
    nowloc.append(event.y)
    loc.append(nowloc)
    if (len(loc) >= 3):
        del loc[0]
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

        box2 = box
        box3 = box
        box4 = box
        # if (abs(time.perf_counter()-timer) >10):

        #     box2 = match(img1,img2,box)
        #     box3 = match(img1,img3,box)
        #     box4 = match(img1,img4,box)
        #     timer = time.perf_counter()  

        image_file1 = create(img_open1,box)
        image_file2 = create(img_open2,box2)
        image_file3 = create(img_open3,box3)
        image_file4 = create(img_open4,box4)

        putimage()


def scaler(event):
    global scale,flag
    global box,box2,box3,box4
    global img1,img2,img3,img4
    global image_file1,image_file2,image_file3,image_file4



    boxx = list(box)

    oldscale = scale

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


    boxx[2] = boxx[0]+400*scale
    boxx[3] = boxx[1]+300*scale
  
    box = tuple(boxx)
    box2 = box
    box3 = box
    box4 = box
    # box2 = match(img1,img2,box)
    # box3 = match(img1,img3,box)
    # box4 = match(img1,img4,box)

    image_file1 = create(img_open1,box)
    image_file2 = create(img_open2,box2)
    image_file3 = create(img_open3,box3)
    image_file4 = create(img_open4,box4)

    putimage()

def locclear(event):
    global loc
    loc.clear()

def match(img1,img2,box1):
    img = img2
    template = img1[box1[1]:box1[3],box1[0]:box1[2]]
    w, h = template.shape[::-1]

    methods = ['cv2.TM_SQDIFF']
#methods = ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED',
#            'cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
#            'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED']

    for meth in methods:
        method = eval(meth)
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) #找到最大值和最小值

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    box=top_left+bottom_right

    return box

def update():
    global box,box2,box3,box4
    global img1,img2,img3,img4,flag
    global image_file1,image_file2,image_file3,image_file4

    box2 = match(img1,img2,box)
    box3 = match(img1,img3,box)
    box4 = match(img1,img4,box)

    image_file1 = create(img_open1,box)
    image_file2 = create(img_open2,box2)
    image_file3 = create(img_open3,box3)
    image_file4 = create(img_open4,box4)

    putimage()



window.title('My Window')
 

window.geometry('1000x800') 

#path = 'C:/Users/37151/Desktop/tkinter/sense1'
path = os.getcwd() + '/sense1'
pathh = tk.StringVar()
tk.Label(window,text = "目标路径:").place(x=550, y=75, anchor='w')
tk.Entry(window, textvariable = pathh).place(x=620, y=75,width = 250, anchor='w')

tk.Button(window, text = "路径选择", command = selectPath).place(x=900, y=75, anchor='w')

filesname=getfilesname(path)

flag = 0
loc = []

scale = 10

box = (0, 0, 400*scale, 300*scale)  
box2 = (0, 0, 400*scale, 300*scale)
box3 = (0, 0, 400*scale, 300*scale)
box4 = (0, 0, 400*scale, 300*scale)

var = tk.StringVar()    
r1 = tk.Radiobutton(window, text='noise', variable=var, value='noise', command=print_selection)
r1.place(x=50, y=50, anchor='w')
r2 = tk.Radiobutton(window, text='detail', variable=var, value='detail', command=print_selection)
r2.place(x=175, y=50, anchor='w')
r3 = tk.Radiobutton(window, text='baoguang', variable=var, value='baoguang', command=print_selection)
r3.place(x=300, y=50, anchor='w')
r4 = tk.Radiobutton(window, text='color', variable=var, value='color', command=print_selection)
r4.place(x=425, y=50, anchor='w')

var1 = tk.StringVar()   
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

var2 = tk.StringVar()    
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

var3 = tk.StringVar()  
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

var4 = tk.StringVar() 
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

img1 = cv2.imread(filesname[0],0)
img2 = cv2.imread(filesname[1],0)
img3 = cv2.imread(filesname[2],0)
img4 = cv2.imread(filesname[3],0)

img_open1 = Image.open(filesname[0])
img_open2 = Image.open(filesname[1])
img_open3 = Image.open(filesname[2])
img_open4 = Image.open(filesname[3])

   

image_file1 = create(img_open1,box)
image_file2 = create(img_open2,box2)
image_file3 = create(img_open3,box3)
image_file4 = create(img_open4,box4)

canvas1 = tk.Canvas(window, height=300, width=400)
image1 = canvas1.create_image(200, 0, anchor='n',image=image_file1)  
canvas1.place(x=50, y=100, anchor='nw')

canvas2 = tk.Canvas(window, height=300, width=400)
image2 = canvas2.create_image(200, 0, anchor='n',image=image_file2)     
canvas2.place(x=550, y=100, anchor='nw')

canvas3 = tk.Canvas(window, height=300, width=400)
image3 = canvas3.create_image(200, 0, anchor='n',image=image_file3)     
canvas3.place(x=50, y=450, anchor='nw')

canvas4 = tk.Canvas(window, height=300, width=400)
image4 = canvas4.create_image(200, 0, anchor='n',image=image_file4)  
canvas4.place(x=550, y=450, anchor='nw')
  
b = tk.Button(window, text='upload(点一下就行)', font=('Arial', 12), command=hit_me)
b.place(x=550, y=25, anchor='w')

b0= tk.Button(window, text='match', font=('Arial', 12), width = 5,command=update)
b0.place(x=750, y=25, anchor='w')

window.bind("<MouseWheel>",scaler)
window.bind("<B1-Motion>",drag)
window.bind("<ButtonRelease-1>",locclear)

window.attributes("-topmost",True)
window.mainloop()