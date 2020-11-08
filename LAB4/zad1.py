import imutils as imutils
from cv2 import *
import sys
import numpy as np
from LAB4.functions import *
import math
import copy

cap = open_video("kartka2.mp4")

width = 1280
height = 720
width_warped = 640
height_warped = 360
dilation_size = 5
kernel_close = np.ones((10, 10), np.uint8)
white_lower = (200, 200, 200)
white_higher = (255, 255, 255)
lower_red = np.array([150, 100, 200])
upper_red = np.array([200, 150, 255])
screen_numer = 0

namedWindow("range")
createTrackbar("x1", "range", 20, 100, nothing)
createTrackbar("y1", "range", 20, 100, nothing)
createTrackbar("cx1", "range", 50, 1000, nothing)
createTrackbar("cy1", "range", 50, 1000, nothing)

warped = None

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
        # img_bw = equalizeHist(img_bw)
        img_blur = GaussianBlur(img_bw, (11, 11), BORDER_DEFAULT)
        img_blur = cv2.morphologyEx(img_blur, cv2.MORPH_DILATE, kernel)
        mask_canny = Canny(img_blur, cx1, cy1, 3)
        mask_canny = cv2.morphologyEx(mask_canny, cv2.MORPH_CLOSE, kernel_close)
        contours, hierarchy = findContours(mask_canny, RETR_EXTERNAL, CHAIN_APPROX_NONE)
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        if len(contours_sorted) >= 1:
            cnt = contours_sorted[0]
            peri = arcLength(cnt, True)
            approx = approxPolyDP(cnt, 0.1 * peri, True)
            objCor = len(approx)
            if objCor == 4:
                pts = np.array(numpy_array(approx), dtype="float32")
                warped, warped_width, warped_height = four_point_transform(img, pts)
                # drawContours(img, cnt, -1, (0, 255, 0), 3)
                drawContours(img, approx, -1, (0, 0, 255), 30)

                mask_warped_marker = cv2.inRange(warped, lower_red, upper_red)
                contours_all_marker = findContours(mask_warped_marker, RETR_TREE, CHAIN_APPROX_SIMPLE)
                contours_all_marker = imutils.grab_contours(contours_all_marker)

                if len(contours_all_marker) == 1:
                    marker_contour = contours_all_marker[0]
                elif len(contours_all_marker) > 1:
                    contours_sorted_marker = sorted(contours_all_marker, key=lambda x: cv2.contourArea(x), reverse=True)
                    marker_contour = contours_sorted_marker[0]
                else:
                    marker_contour = None

                if marker_contour is not None:
                    marker_x = marker_contour[0][0][0]
                    marker_y = marker_contour[0][0][1]
                    # print(str(marker_x) + " : "+ str(warped_width) + "   |   " + str(marker_y) + " : " + str(warped_height) )
                    left = marker_x < warped_width / 2
                    right = marker_x > warped_width / 2
                    up = marker_y < warped_height / 2
                    down = marker_y > warped_height / 2
                    if left and up:
                        warped = rotate(warped, ROTATE_90_CLOCKWISE)
                    if left and down:
                        warped = rotate(warped, ROTATE_90_CLOCKWISE)
                        warped = rotate(warped, ROTATE_90_CLOCKWISE)
                    if right and down:
                        warped = rotate(warped, ROTATE_90_COUNTERCLOCKWISE)

        if warped is not None:
            warped = resize(warped, (width_warped, height_warped))
            imshow('warped', warped)
        imshow('img', img)

    else:
        break
    if waitKey(20) & 0xFF == ord('q'):
        break
    if waitKey(20) & 0xFF == ord('x'):
        cv2.imwrite("img/screen" + str(screen_numer) + ".png", warped)
        screen_numer += 1
        print("img/screen" + str(screen_numer) + ".png saved!")

cap.release()
destroyAllWindows()
