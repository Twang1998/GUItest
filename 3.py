from PIL import Image, ImageTk
import tkinter.filedialog
import tkinter as tk 
import os

window = tk.Tk()
window.title('My Window')
window.geometry('1000x800') 

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

def create(img_open):
    global box
    region = img_open.crop(box)     
    region1 = region.resize((400, 300))
    image_file = ImageTk.PhotoImage(image = region1)
    return image_file

def setimage(filesname):
    global box
    global canvas1,canvas2,canvas3,canvas4
    img_open1 = Image.open(filesname[0])
    img_open2 = Image.open(filesname[1])
    img_open3 = Image.open(filesname[2])
    img_open4 = Image.open(filesname[3])

    image_file1 = create(img_open1)
    image_file2 = create(img_open2)
    image_file3 = create(img_open3)
    image_file4 = create(img_open4)

    
    canvas1.delete()
    canvas2.delete()
    canvas3.delete()
    canvas4.delete()    

    canvas1 = tk.Canvas(window, bg='green', height=300, width=400)  
    canvas1.image_file = image_file1
    image1 = canvas1.create_image(200, 0, anchor='n',image=image_file1)       
    canvas1.place(x=50, y=100, anchor='nw')

    canvas2 = tk.Canvas(window, bg='green', height=300, width=400)
    canvas2.image_file = image_file2
    image2 = canvas2.create_image(200, 0, anchor='n',image=image_file2)       
    canvas2.place(x=550, y=100, anchor='nw')

    canvas3 = tk.Canvas(window, bg='green', height=300, width=400)
    canvas3.image_file = image_file3
    image3 = canvas3.create_image(200, 0, anchor='n',image=image_file3)    
    canvas3.place(x=50, y=450, anchor='nw')

    canvas4 = tk.Canvas(window, bg='green', height=300, width=400)
    canvas4.image_file = image_file4
    image4 = canvas4.create_image(200, 0, anchor='n',image=image_file4)    
    canvas4.place(x=550, y=450, anchor='nw')


def empty():
    return

def hit_me():
    global var1,var2,var3,var4,var,box
    print(var1.get(),var2.get(),var3.get(),var4.get(),var.get())
    print(box)


def drag(event):
    global box
    global path
    global loc
    global scale
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
        filesname = getfilesname(path)
        setimage(filesname)
def scaler(event):
    global scale
    global box
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

    boxx[2] = boxx[0]+400*scale
    boxx[3] = boxx[1]+300*scale
    box = tuple(boxx)
    filesname = getfilesname(path)
    setimage(filesname)
    
def locclear(event):
    global loc
    loc.clear()


def print_selection():
    print('you have selected ' + var.get())

def selectPath():
    #global pathh
    global path
    global var1,var2,var3,var4,var
    path = tkinter.filedialog.askdirectory()
    pathh.set(path)

    # for widget in window.winfo_children():
    #     widget.destroy()
    filesname = getfilesname(path)
    if(len(filesname) == 0 or len(filesname)%4 != 0):
        selectPath()


scale = 10
box = (0,0,400*scale,300*scale)
path = 'C:/Users/37151/Desktop/tkinter/sense1'
loc = []

pathh = tk.StringVar()
tk.Label(window,text = "目标路径:").place(x=550, y=75, anchor='w')
tk.Entry(window, textvariable = pathh).place(x=620, y=75,width = 250, anchor='w')
tk.Button(window, text = "路径选择", command = selectPath).place(x=900, y=75, anchor='w')

canvas1 = tk.Canvas(window, bg='green', height=300, width=400)
canvas2 = tk.Canvas(window, bg='green', height=300, width=400)
canvas3 = tk.Canvas(window, bg='green', height=300, width=400)
canvas4 = tk.Canvas(window, bg='green', height=300, width=400)

filesname = getfilesname(path)
setimage(filesname)

var = tk.StringVar()   
r1 = tk.Radiobutton(window, text='noise', variable=var, value='noise')
r1.place(x=50, y=50, anchor='w')
r2 = tk.Radiobutton(window, text='detail', variable=var, value='detail')
r2.place(x=175, y=50, anchor='w')
r3 = tk.Radiobutton(window, text='baoguang', variable=var, value='baoguang')
r3.place(x=300, y=50, anchor='w')
r4 = tk.Radiobutton(window, text='color', variable=var, value='color')
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

filesname = getfilesname(path)
setimage(filesname)

window.bind("<MouseWheel>",scaler)
window.bind("<B1-Motion>",drag)
window.bind("<ButtonRelease-1>",locclear)

b = tk.Button(window, text='upload(点一下就行)', font=('Arial', 12), command=hit_me)
b.place(x=550, y=25, anchor='w')


       


window.mainloop()