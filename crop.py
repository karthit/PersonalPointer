# Required modules
import cv2

# Constants for the crop size
xMin = 0
yMin = 0
xMax = 320
yMax = 240

# Open cam, decode image, show in window
cap = cv2.VideoCapture(0) # use 1 or 2 or ... for other camera
cv2.namedWindow("Original")
cv2.namedWindow("Cropped")
key = -1
while(key < 0):
    success, img = cap.read()

    cropImg = img[yMin:yMax,xMin:xMax] # this is all there is to cropping

    cv2.imshow("Original", img)
    cv2.imshow("Cropped", cropImg)

    key = cv2.waitKey(1)
cv2.destroyAllWindows()