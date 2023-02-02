import cv2, os
from pathlib import Path
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
sub_data = 'ammu'

path = os.path.join(datasets, sub_data)
try:
    os.makedirs("datasets/ammu")
except FileExistsError:
    # directory already exists
    pass
(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces: #segregating x,y,w,h
        cv2.rectangle(im, (x,y), (x+w, y+h), (255, 0, 0), 2)
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png'% (path, count), face_resize)
        count+=1
    cv2.imshow('OpenCV',im)
    key =cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()

