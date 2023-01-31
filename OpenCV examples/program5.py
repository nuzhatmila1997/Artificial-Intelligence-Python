import cv2

vs = cv2.VideoCapture(0) #initialize the camera

while True: #infinite loop for capturing
    _, img = vs.read() #reading the frame from the camera, ignoring the flag

    cv2.imshow("VideoStream", img) #show the frame
    key = cv2.waitKey(1) & 0xFF #hexa value of the key we are pressing
    if key == ord('q'): #ascii of 'q'
        break
vs.release() #releasing the camera
cv2.destroyAllWindows() #close all windows
    
