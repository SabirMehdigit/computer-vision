import cv2

cap= cv2.VideoCapture("nature.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    print("chk1")
    if cv2.waitKey(500) & 0xFF==ord('q'):
        print("CHK2")
        break
