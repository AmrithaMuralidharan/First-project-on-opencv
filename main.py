import cv2
capture = cv2.VideoCapture(0)
while True:
    capture.read()
    key,image=capture.read()
    cv2.imshow("video",image)
    cv2.waitKey(1)