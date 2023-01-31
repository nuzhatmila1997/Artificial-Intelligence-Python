import cv2

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg") #read image
rectImg = cv2.rectangle(img,(100,50),(125,80),(0,255,0),2)
cv2.imwrite("rectangleImg.jpg",rectImg)
