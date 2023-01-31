import cv2

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg")

gaussianBlurImg = cv2.GaussianBlur(img, (25,25), 0)

cv2.imwrite("gsBlur.jpg",gaussianBlurImg)
