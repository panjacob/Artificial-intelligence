import imutils as imutils
from cv2 import *
import sys
import numpy as np
from LAB3.functions2 import *
import math

cap = open_video("film/ferrari.mp4")

width = 1280
height = 720
dilation_size = 5
kernel = np.ones((150, 150), np.uint8)
kernel_turbo = np.ones((80, 80), np.uint8)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])

create_trackbar()

while True:
    success, img = cap.read()
    if success:
        img = resize(img, (width, height))
        flip(img, 0, img)
        img_blur = GaussianBlur(img, (7, 7), BORDER_DEFAULT)
        img_hsv = cvtColor(img_blur, COLOR_BGR2HSV)

        [lower, upper] = get_trackbar()
        mask = cv2.inRange(img, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    else:
        break
    if waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
