import imutils as imutils
from cv2 import *
import sys
import numpy as np
from LAB3.functions2 import *
import math

cap = open_video("kartka.mp4")

width = 1280
height = 720
dilation_size = 5
kernel_close = np.ones((2, 2), np.uint8)
white_lower = (200, 200, 200)
white_higher = (255, 255, 255)

namedWindow("range")
createTrackbar("x1", "range", 13, 100, nothing)
createTrackbar("y1", "range", 13, 100, nothing)
createTrackbar("cx1", "range", 277, 1000, nothing)
createTrackbar("cy1", "range", 277, 1000, nothing)

while True:
    success, img = cap.read()
    if success:
        x1 = getTrackbarPos('x1', 'range')
        y1 = getTrackbarPos('y1', 'range')
        cx1 = getTrackbarPos('cx1', 'range')
        cy1 = getTrackbarPos('cy1', 'range')

        kernel = np.ones((x1, y1), np.uint8)
        img = resize(img, (width, height))
        img_bw = cvtColor(img, COLOR_BGR2GRAY)
        img_bw = equalizeHist(img_bw)
        mask_canny = Canny(img_bw, cx1, cy1, 3)
        mask_canny = cv2.morphologyEx(mask_canny, cv2.MORPH_DILATE, kernel)
        mask_canny = Canny(img_bw, cx1, cy1, 3)
        contours = findContours(mask_canny, RETR_LIST, CHAIN_APPROX_SIMPLE)
        mask_canny = cv2.morphologyEx(mask_canny, cv2.MORPH_DILATE, kernel_close)
        contours_all = imutils.grab_contours(contours)
        contours_4 = []
        for contour in contours_all:
            # if len(contour) == 4:
                # contours_4.append(contour)
            drawContours(img, contour, -1, (0, 255, 0), 2)

        # if len(contours_4) > 0:
        #     contours_4_sorted = sorted(contours_4, key=lambda x: cv2.contourArea(x), reverse=False)


        # mask_white = cv2.inRange(img, white_lower, white_higher)

        imshow('mask', mask_canny)
        imshow('img', img)
    else:
        break
    if waitKey(500) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
