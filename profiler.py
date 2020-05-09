import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import sys

name = str(sys.argv[1])

print(name)

#load the image
img = cv2.imread((name + ".png"),0)

#record its dimensions.. (not req just gives reasurrance of correct data input)
p = img.shape
print(p)

# save height and width for use as bounds of for loops
rows,cols = img.shape
# create file for print output to be saved in
sys.stdout = open((name + ".py"), "w")


print(name + " = [")
# step thru each pixel in the Y axis 
for i in reversed(range(rows)):
    # reset colour value
    k = 0
    # step thru each pixel in the X axis
    for j in range(cols):
        # is this the darkest one we've found yet?
        if img[i,j] > k:
            #record the pixel value
            k = img[i,j]
            # save the X position of this pixel
            x = j
    # divide by 10 to get 1/10 mm precision        
    x = x / 10
    # output to file
    print(str(x),',',sep='')

# how many more rows are required to make up our 200mm max height (2000 total rows)
remainingRows = 2000 - rows
#count thru the number of rows we need to add
for i in range(remainingRows):
    #repeat the last dimension
    print(str(x),',',sep='')

print("]")

sys.stdout.close()

sys.stdout = sys.__stdout__

print('filler', remainingRows)

print("done :)")