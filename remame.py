# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:14:20 2019

@author: lenovo
"""




import os
import cv2
i=1 
path = "D:/ASD/"
 
#img = cv2.imread("D:/ASD/0061.png")
#
#
#cropped = img[650:4900, 480:3450]  # 裁剪坐标为[y0:y1, x0:x1]
#cv2.imwrite("D:/ASDF/0061.png", cropped)
for filename in os.listdir(path):

    name = filename.split('.')
    print(name[1])
    if name[1] == "jpg":
        os.rename(os.path.join(path, filename), os.path.join(path, str(i) + '.png'))
    i=i+1
