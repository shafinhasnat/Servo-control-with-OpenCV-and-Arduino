import cv2
import numpy as np
import serial
import struct
import time
a=0
b=0
x=0
y=0
ser = serial.Serial('com4',9600)
time.sleep(2)
font=cv2.FONT_HERSHEY_SIMPLEX
FaceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
def BoxDraw():
    cv2.line(flipit,(213,0),(213,480),(255,0,0),2)
    cv2.line(flipit,(426,0),(426,480),(255,0,0),2)
    cv2.line(flipit,(0,160),(640,160),(255,0,0),2)
    cv2.line(flipit,(0,320),(640,320),(255,0,0),2)
    pass
while True:
    ret,frame=cap.read()
    flipit=cv2.flip(frame,1)
    gray=cv2.cvtColor(flipit,cv2.COLOR_BGR2GRAY)
    face=FaceCascade.detectMultiScale(gray,1.2,4)
##    BoxDraw()
    try:
        for (x1,y1,w1,h1) in face:
            a=int((2*x1+w1)/2)
            b=int((2*y1+h1)/2)
            x=int(a/3.66)
            y=int(b/2.55)
            ser.write(struct.pack('>BB', x,y))
##            data1 = ser.readline()
##            data2 = ser.readline()
####
##            print(data1,', ',data2)
            cv2.rectangle(flipit,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
##            cv2.circle(flipit,(a,b),3,(0,0,255),-1)
            
    except:
        pass
            
    cv2.imshow('flipit',flipit)
    k=cv2.waitKey(20) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
