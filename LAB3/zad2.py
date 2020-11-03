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
        # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours_all = findContours(mask, RETR_TREE, CHAIN_APPROX_SIMPLE)
        contours_all = imutils.grab_contours(contours_all)
        contours_sorted = sorted(contours_all, key=lambda x: cv2.contourArea(x), reverse=True)
        # print(len(contours_sorted))
        x1 = 0
        y1 = 0
        if len(contours_sorted) > 0:
            contour_one = contours_sorted[0]
            # drawContours(img, [contour_one], -1, (0, 255, 0), 2)
            try:
                M = moments(contour_one)
                x1 = int(M["m10"] / M["m00"])
                y1 = int(M["m01"] / M["m00"])
                circle(img, (x1, y1), 7, (255, 255, 255), -1)
            except:
                pass

        if len(contours_sorted) > 1:
            contour_two = contours_sorted[1]
            # drawContours(img, [contour_two], -1, (0, 255, 0), 2)
            M = moments(contour_two)
            try:
                x2 = int(M["m10"] / M["m00"])
                y2 = int(M["m01"] / M["m00"])
                circle(img, (x2, y2), 7, (255, 255, 255), -1)
                distance = int(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
                xc = int((x1 + x2) / 2)
                yc = int((y1 + y2) / 2)
            except:
                pass

            if distance > 500:
                display = 'AWARYJNE HAMOWANIE'
                color = (0, 0, 0)
            elif distance > 400:
                display = 'PIK PIK PIK PIK'
                color = (0, 0, 255)
            elif distance > 300:
                display = 'PIK         PIK'
                color = (0, 140, 255)
            elif distance > 200:
                display = '     OK          '
                color = (0, 255, 0)
            else:
                display = ''
                color = (0, 0, 255)
            # circle(img, (xc, yc), 15, color, -1)
            putText(img, str(int((33 * 220) / distance)) + " cm", (xc - 30, yc),
                    FONT_HERSHEY_SIMPLEX, 1, color, 4)
            putText(img, display, (500, 50),
                    FONT_HERSHEY_SIMPLEX, 1, color, 4)

            # print(distance)

        imshow("mask", mask)
        imshow("img", img)
        # pretty_window = np.concatenate((img, img_blur, img_hsv), axis=1)
        # imshow("pretty_window", pretty_window)
    else:
        break
    if waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
