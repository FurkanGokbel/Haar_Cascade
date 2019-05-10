import cv2
import numpy as np


capture = cv2.VideoCapture('Video.mp4')    #1 harici dışarıdan bir kamera ekliyor

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
    _,frame = capture.read()
    griton = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    insan = human_cascade.detectMultiScale(griton,1.1,4)

    for (x,y,w,h) in insan:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow('insanlar',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()











