from imutils import paths
from imutils.object_detection import non_max_suppression
from picamera import PiCamera
from picamera.array import PiRGBArray

import imutils
import numpy as np
import cv2
import time

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detectPeople(image, hog):
    #resize image to increase speed and acuracy
    image = imutils.resize(image, width=min(400, image.shape[1]))
    #apply hog descriptor to detect people in image
    rects, weights = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    #apply non-maxima supression 
    rects = np.array([[x, y, x+w, y+h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    #draw boxes on image
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    
    return image

camera = PiCamera()
#camera.rotation = 180
#camera.resolution=(640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera)#, size=(640, 480))

#camera.start_preview(alpha=150)
#time.sleep(10)
#camera.stop_preview()

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = detectPeople(image, hog)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break