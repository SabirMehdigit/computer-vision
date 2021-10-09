import cv2
import numpy as np

image =cv2.imread("face.jpg")
kernel =np.ones((5,5),np.uint8)


imgGray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(image,150,200)

imgDialation= cv2.dilate(imgCanny,kernel,iterations=1)  # increase the size of lines
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Face(Gray)",imgGray)
cv2.imshow("face(blur)",imgBlur)
cv2.imshow("face(canny",imgCanny)
cv2.imshow("Dialation(canny",imgDialation)
cv2.imshow("Eroded(canny",imgEroded)

cv2.waitKey(0)