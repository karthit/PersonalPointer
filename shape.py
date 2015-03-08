import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    
    frame = cv2.medianBlur(frame,5)
    cimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(cimg,cv2.cv.CV_HOUGH_GRADIENT,5,200,param1=50,param2=100,minRadius=10,maxRadius=100)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
    	cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1) 
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('frame',cimg)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()