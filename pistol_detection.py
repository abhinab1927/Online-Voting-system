

import numpy as np
import cv2

import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None



gun_exist = False

while True:
    (grabbed, frame) = camera.read()

   

    # resize the frame, convert it to grayscale, and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (100, 100))
    
    if len(gun) > 0:
        gun_exist = True
        
    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]    

    # if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue

  
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF or 0xFF == ord('q')

if gun_exist:
    print("guns detected")
else:
    print("guns NOT detected")

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()






