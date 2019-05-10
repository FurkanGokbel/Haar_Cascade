# -*- coding: utf-8 -*-
# @Time : 23.09.2018 12:28
# @Author : Raşit EVDÜZEN
# @File : Yuz_Goz_Tanıma.py
# @Software: PyCharm
import cv2

yuz_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
goz_cascade = cv2.CascadeClassifier('haarcascade-eye.xml')



img = cv2.imread('yuz2.png')

griton = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzler = yuz_cascade.detectMultiScale(griton,1.3,5)
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_griton = griton[y:y+h,x:x+w]
    roi_renkli = img[y:y+h,x:x+w]
    gozler = goz_cascade.detectMultiScale(roi_griton)
    for (ex,ey,ew,eh) in gozler:
        cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(0,158,0),2)


cv2.imshow('goruntu',img)
cv2.imwrite('İşlenmiş.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()










