import cv2 #library import - OpenCV

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg") #read an image

cv2.imwrite("catSample1.png", img) #save an image [saving the image kept in img with different name and extension]

cv2.imshow("Cat Image", img) #display the image until you close [showing this image with a title]
cv2.waitKey(0) # it will show continuously if waitkey is 0

cv2.destroyAllWindows() # if you terminate it will destroy all windows 
