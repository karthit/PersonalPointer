import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('xml/haarcascade_lefteye_2splits.xml')

xMin=0
yMin=0
xMax=320
yMax=240
x1Min=0
y1Min=0
x1Max=320
y1Max=240

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)	
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = frame[y:y+h, x:x+w]
	x1Min=x
	x1Max=x+w
	y1Min=y
	y1Max=y+h
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for(ex,ey,ew,eh) in eyes:
	     if(ex>100):
	     	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	     	xMin=ex
	     	xMax=ex+ew
	     	yMin=ey
	     	yMax=ey+eh
	     	print ex,ey
    	   
    temp1=frame[y1Min:y1Max,x1Min:x1Max]
    temp=temp1[yMin:yMax,xMin:xMax]
    gray1=cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY) 
    edge=cv2.Canny(gray1,2500,2500,apertureSize=5)
    vis = temp.copy()
    vis/=2
    vis[edge!=0]=(0,255,0)
    cv2.imshow('E',temp)
    cv2.imshow('G',vis)
    cv2.imshow('F',temp1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
