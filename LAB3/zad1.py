import imutils as imutils
from cv2 import *
import sys
import numpy as np
from LAB3.functions import *
import math

cap = open_video("film/lab3.webm")

# width = 360
# height = 640
width = 1280
height = 720
dilation_size = 5
kernel = np.ones((5, 5), np.uint8)
kernel_turbo = np.ones((80, 80), np.uint8)

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])

create_trackbar()

while True:
    success, img = cap.read()
    if success:
        img = resize(img, (width, height))
        img_blur = GaussianBlur(img, (7, 7), BORDER_DEFAULT)
        img_hsv = cvtColor(img_blur, COLOR_BGR2HSV)

        [lower, upper] = get_trackbar()
        mask = cv2.inRange(img_hsv, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours_all = findContours(mask, RETR_TREE, CHAIN_APPROX_SIMPLE)
        contours_all = imutils.grab_contours(contours_all)
        contours_sorted = sorted(contours_all, key=lambda x: cv2.contourArea(x), reverse=True)

        if len(contours_sorted) > 0:
            contour_one = contours_sorted[0]
            M = moments(contour_one)
            x1 = int(M["m10"] / M["m00"])
            y1 = int(M["m01"] / M["m00"])
            circle(img, (x1, y1), 7, (255, 255, 255), -1)
            drawContours(img, [contour_one], -1, (0, 255, 0), 2)

        if len(contours_sorted) > 1:
            contour_two = contours_sorted[1]
            M = moments(contour_two)
            x2 = int(M["m10"] / M["m00"])
            y2 = int(M["m01"] / M["m00"])
            circle(img, (x2, y2), 7, (255, 255, 255), -1)
            drawContours(img, [contour_two], -1, (0, 255, 0), 2)

            deltay = y1 - y2
            if deltay < 0:
                deltay = deltay * (-1)

            if deltay < 30:
                line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # imshow("mask", mask)
        imshow("img", img)
        # pretty_window = np.concatenate((img, img_blur, img_hsv), axis=1)
        # imshow("pretty_window", pretty_window)
    else:
        break
    if waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
