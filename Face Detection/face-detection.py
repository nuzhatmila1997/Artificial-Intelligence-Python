import cv2

alg = "haarcascade_frontalface_default.xml" #access the model file
haar_cascade = cv2.CascadeClassifier(alg) #loading the model file with cv2

cam = cv2.VideoCapture(0) #initialize the camera

while True:
    _, img = cam.read() #read frame from camera

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to grayscale

    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4) #get coords of face

    for (x, y, w, h) in face: #segregating x,y,w,h
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
