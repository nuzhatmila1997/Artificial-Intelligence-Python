import cv2
img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshImage = cv2.threshold(grayImage, 185, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("E:\AI Master Class\Artificial-Intelligence-Python\pics\catThresh.png",threshImage)
