import cv2

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\catSample1.png")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #CONVERT COLOR TO GRAY IMAGE

cv2.imwrite("E:\AI Master Class\Artificial-Intelligence-Python\pics\grayCat.jpg",grayImg) #SAVE THE GRAYSCALE IMAGE

cv2.imshow("Original", img)

cv2.imshow("Gray Scale", grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
