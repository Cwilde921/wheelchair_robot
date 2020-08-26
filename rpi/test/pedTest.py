
from imutils import paths
from imutils.object_detection import non_max_suppression
import imutils
import numpy as np
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

imageName = "person1.jpeg"
imagePath = "../test_imgs/inpt/" + imageName
outputPath = "../test_imgs/outpt/" + imageName

image = cv2.imread(imagePath)
image = imutils.resize(image, width=min(400, image.shape[1]))
orig = image.copy()

#cv2.imshow("testing", image)
#cv2.waitKey(0)

rects, weights = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#print(rects)

for (x, y, w, h) in rects:
    cv2.rectangle(orig, (x, y), (x+w, y+h), (0, 0, 225), 2)

rects = np.array([[x, y, x+w, y+h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

for (xA, yA, xB, yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

cv2.imshow("initial", orig)
cv2.imshow("final", image)
print(weights)
cv2.waitKey(0)
