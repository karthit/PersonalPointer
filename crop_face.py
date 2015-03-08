import numpy as np
import cv2

xMin=0
yMin=0
xMax=10
yMax=10

face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")
cv2.namedWindow("Cropped")
key=-1
while(key<0):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	xMin=x
	yMin=y
	xMax=x+w
	yMax=y+h	
    cropImg = frame[yMin:yMax,xMin:xMax]
    cv2.imshow('crop',cropImg)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()
