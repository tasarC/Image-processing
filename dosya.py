import cv2
import numpy as np
from matplotlib import pyplot as plt

OUTPUT_IMAGE = "xxxxxxx"
#resm = "../odev2.bmp"
img = cv2.imread("odev2.bmp")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def ortalamadeger(ort):
       ort.sort()
       if(len(ort)%2!=0):
        return ort[int(len(ort)/2)]
       else:
        deger = int(len(ort)/2)
        return int((ort[deger]/2 + ort[deger+1])/2)

def medianFilter(resim, kernel_size):
    cpy = resim.copy() 
    satır = resim.shape[0]
    sutun = resim.shape[1] 
    ofs = int(kernel_size/2)
    for i in range(ofs, satır-ofs):
        for j in range(ofs, sutun -ofs):
            dglr = []
            for k in range(kernel_size * kernel_size):
                img_deger = resim[int(i + k/kernel_size - ofs)][int(j+ k%kernel_size-ofs)]
                dglr.append(img_deger)
            cpy[i][j] = ortalamadeger(dglr)
    return cpy

    
 
kernel_s = 5
im2_median = medianFilter(img, kernel_s)
fig = plt.figure()
plt.subplot('121')
#cv2.imshow('a', img)
plt.imshow(img,cmap='gray')
plt.subplot('122')
plt.imshow(im2_median,cmap='gray')
#cv2.imshow('b', im2_median)
cv2.imwrite('xxx.jpg',im2_median)
plt.show()

  

