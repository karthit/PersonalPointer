import cv2
import os
import math
import numpy

minRad = 50
maxRad = 75

b1 = 2
b2 = 5
b3 = 5

c1 = 5
c2 = 200
c3 = 50
c4 = 100

bw = 1

vc =cv2.VideoCapture(0)
if vc.isOpened():
    vc.set(3,800)
    vc.set(4,600)
#       vc.set(10,10)
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    blur = cv2.bilateralFilter(frame,b1,b2,b3)
#       blur = cv2.GaussianBlur(frame,(5,5),1)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)#frame
#       edges = cv2.Canny(gray, 200, 20, apertureSize=3)#80 120 3
    edges = gray

    circles = cv2.HoughCircles(edges,cv2.cv.CV_HOUGH_GRADIENT,c1,c2,param1=c3,param2=c4,minRadius=minRad,maxRadius=maxRad)
    print "\n\n"
    print circles

    if circles != None:
        circles = numpy.uint16(numpy.around(circles),decimals=1)
        for cir in circles[0,:]:
            if bw == 1:
                cv2.circle(edges,(cir[0],cir[1]),cir[2],(0,255,0),2)#frame
                cv2.circle(edges,(cir[0],cir[1]),2,(0,0,255),)#frame
            else:           
                #draw outer circle
                cv2.circle(blur,(cir[0],cir[1]),cir[2],(0,255,0),2)#frame
                #draw center
                cv2.circle(blur,(cir[0],cir[1]),2,(0,0,255),)#frame
    if bw == 1:
        cv2.imwrite('/home/kasper/test/test.jpg', edges, [int(cv2.IMWRITE_JPEG_QUALITY), 90])   
    else:
        cv2.imwrite('/home/kasper/test/test.jpg', blur, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    ch = cv2.waitKey(10)

    if ch != -1:
        print "keypressed"
        print ch
        break
    cv2.destroyAllWindows()