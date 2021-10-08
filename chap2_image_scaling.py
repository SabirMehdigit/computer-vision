import cv2

image =cv2.imread("face.jpg")


imgGray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(image,100,100)

cv2.imshow("Face(Gray)",imgGray)
cv2.imshow("face(blur)",imgBlur)
cv2.imshow("face(canny",imgCanny)

cv2.waitKey(0)