import cv2

img1 = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg")
print(img1.shape) #dimension and type 3 --> rgb/ color image (1024, 1025, 3)
img2 = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\grayCat.jpg")
print(img2.shape)
print(img1.size) #3148800
print(img1.dtype) #uint8
