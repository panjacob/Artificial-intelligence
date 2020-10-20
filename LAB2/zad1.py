from cv2 import *
import sys
import numpy as np


def nothing():
    pass


cap = VideoCapture("film/lab2.webm")
if not cap.isOpened():
    print("Błąd otwierania pliku")

width = 360
height = 640

if len(sys.argv) >= 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])

namedWindow("range")
createTrackbar("h1", "range", 100, 255, nothing)
createTrackbar("s1", "range", 100, 255, nothing)
createTrackbar("v1", "range", 100, 255, nothing)
createTrackbar("h2", "range", 106, 255, nothing)
createTrackbar("s2", "range", 200, 255, nothing)
createTrackbar("v2", "range", 255, 255, nothing)

while True:
    success, img = cap.read()
    if success:
        img = resize(img, (width, height))
        img_blur = GaussianBlur(img, (5, 5), BORDER_DEFAULT)
        img_hsv = cvtColor(img_blur, COLOR_BGR2HSV)

        h1 = getTrackbarPos('h1', 'range')
        s1 = getTrackbarPos('s1', 'range')
        v1 = getTrackbarPos('v1', 'range')
        h2 = getTrackbarPos('h2', 'range')
        s2 = getTrackbarPos('s2', 'range')
        v2 = getTrackbarPos('v2', 'range')

        lower_blue = np.array([h1, s1, v1])
        upper_blue = np.array([h2, s2, v2])
        mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
        img_hsv_filtered = bitwise_and(img, img, mask=mask)

        # imshow("hsv", img_hsv)
        imshow("mask", mask)
        # imshow("hsv_filtered", img_hsv_filtered)
        pretty_window = np.concatenate((img, img_hsv, img_hsv_filtered), axis=1)
        imshow("pretty_window", pretty_window)
    else:
        break
    if waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
