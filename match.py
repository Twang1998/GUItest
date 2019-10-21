# import cv2

# import time
# from PIL import Image, ImageTk
# import numpy

# def match(img1,img2,box1):
    
#     #img = cv2.cvtColor(numpy.asarray(img2),cv2.COLOR_RGB2BGR)
#     #template = cv2.cvtColor(numpy.asarray(temp),cv2.COLOR_RGB2BGR)
#     img = img2
#     template = img1[box1[1]:box1[3],box1[0]:box1[2]]
#     w, h = template.shape[::-1]

#     methods = ['cv2.TM_SQDIFF']
# #methods = ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED',
# #            'cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
# #            'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED']

#     for meth in methods:
#         method = eval(meth)

#         res = cv2.matchTemplate(img,template,method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) #找到最大值和最小值

#         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#             top_left = min_loc
#         else:
#             top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     box=top_left+bottom_right

#     img=Image.open('2.jpg')
#     imgg=img.crop(box)

#     return box
    
    
# img1 = cv2.imread('1.jpg',0)
# box1 =(1481,1922,1894,2214)
# img2 = cv2.imread('2.jpg',0)
# #crop = img1[1481:1922,867:1731]
# #cv2.imshow('Original',crop)
# #cv2.waitKey(0)
# print(match(img1,img2,box1))




# cpu_start = time.perf_counter()  
# cpu_end = time.perf_counter()  
# print (cpu_start)
# print(cpu_end)
# print('cpu:', cpu_end - cpu_start)

import threading
import time
def change_user():
    print('这是中断,切换账号')
    t = threading.Timer(3, change_user)
    t.start()
#每过3秒切换一次账号
t = threading.Timer(3, change_user)
t.start()
while True:
    print('我在爬数据')
    time.sleep(1)

