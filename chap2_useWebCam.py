import cv2

cap= cv2.VideoCapture(0) # to use default camera
cap.set(3,640)
cap.set(4,480)



while True:
    success, img = cap.read()
    cv2.imshow("LiveWebCamera",img)
     
    if cv2.waitKey(1) & 0xFF==ord('q'):
     
        break
