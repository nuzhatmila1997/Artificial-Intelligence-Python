import cv2 #import opencv library
import imutils #import imutils library

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg") #read image
resizeImg = imutils.resize(img, width=100) #resize image with width 100
cv2.imwrite("resizeImage.jpg", resizeImg) #save the resized image
