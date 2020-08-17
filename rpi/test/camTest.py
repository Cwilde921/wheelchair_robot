from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera = PiCamera()
#camera.rotation = 180
camera.resolution=(640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

#camera.start_preview(alpha=150)
#time.sleep(10)
#camera.stop_preview()

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break
