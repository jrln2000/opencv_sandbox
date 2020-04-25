import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
img = cv2.imread("antaro small 2.png",0)

p = img.shape
print(p)
rows,cols = img.shape

for i in range(rows):
    k = 0
    for j in range(cols):
        if img[i,j] > k:
            k = img[i,j]
            x = j
    print(x)
        
