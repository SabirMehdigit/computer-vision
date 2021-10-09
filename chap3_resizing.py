import cv2
import numpy as np


img=cv2.imread("face.jpg")
print(img.shape)

imgResize=cv2.resize(img,(500,500))
print(imgResize.shape)


imgCrooped=img[50:100,100:300]

#cv2.imshow("image",img)

#display resized image
#cv2.imshow("Resized image",imgResize)

#display Crooped image
cv2.imshow("Crooped image",imgCrooped) 

cv2.waitKey(0)