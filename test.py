import numpy as np
import cv2
import win32api,win32con

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
posx = 0
posy = 0


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
 	     	
    	   
    face=frame[y1Min:y1Max,x1Min:x1Max]
    eye=face[yMin:yMax,xMin:xMax]

    #cv2.line(eye,((xMax-xMin)/2,yMin),((xMax-xMin)/2,yMax),(255,0,0),2)
    #cv2.line(eye,(xMin,(yMin+yMax)/2),(xMax,(yMin+yMax)/2),(0,255,0),2)

    height,width = eye.shape[:2]
    eye=cv2.resize(eye,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

    #low = np.array([0,0,0])
    #high= np.array([0,0,10])
    #hsv = cv2.cvtColor(eye,cv2.COLOR_BGR2HSV)
    #mask= cv2.inRange(hsv,low,high)
    
    eye = cv2.medianBlur(eye,5)
    ceye= cv2.threshold(eye,127,255,cv2.THRESH_BINARY)
    ceye= cv2.cvtColor(eye,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(ceye,cv2.cv.CV_HOUGH_GRADIENT,5,200,param1=50,param2=100,minRadius=5,maxRadius=30)
    if circles is None:
	continue

    circles = np.uint16(np.around(circles))
    
    for i in circles[0,:]:
    	cv2.circle(ceye,(i[0],i[1]),i[2],(0,255,0),1) 
        cv2.circle(ceye,(i[0],i[1]),2,(0,0,255),3)
	posx=i[0]
        posy=i[1]     

    win32api.SetCursorPos((posx,posy))
    cv2.imshow('Frame',frame)
    cv2.imshow('Face',face)
    cv2.imshow('Eye',eye)
    cv2.imshow('circle',ceye)
    #cv2.imshow('hsv',hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


cap.release()
cv2.destroyAllWindows()