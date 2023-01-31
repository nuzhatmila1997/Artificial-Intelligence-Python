import cv2

img = cv2.imread("E:\AI Master Class\Artificial-Intelligence-Python\pics\Cat03.jpg") #read image
textImg = cv2.putText(img,"So cute",(200,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imwrite("textOnImg.jpg",textImg)
