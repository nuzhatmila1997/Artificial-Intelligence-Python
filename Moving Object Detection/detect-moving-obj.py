import cv2 #for image
import time #for delay
import imutils #to resize

cam = cv2.VideoCapture(0) #initialize the camera
time.sleep(1) #1 second delay to initialize

firstFrame = None
area = 500

while True:
    _, img = cam.read() #read frame from camera
    text = "No moving object"
    img = imutils.resize(img, width = 500) #resize

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to grayscale

    gaussianBlurImg = cv2.GaussianBlur(grayImg, (21,21), 0) #smoothened

    if firstFrame is None:
        firstFrame = gaussianBlurImg
        continue
    imgDiff = cv2.absdiff(firstFrame, gaussianBlurImg) #difference between the first frame and when moving opject appears. say if the first frame doesn't have me, and gaussian blur frame has me then I am the difference

    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] #binary
    threshImg = cv2.dilate(threshImg, None, iterations=2) #to remove any dots from binary image

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #contour the object
    cnts = imutils.grab_contours(cnts) #grab every contour

    for c in cnts:
        if cv2.contourArea(c) < area: #if area of each contour is less than the total area, that is a moving obj
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        text = "Moving Object Detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
