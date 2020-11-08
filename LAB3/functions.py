from cv2 import *
import numpy as np


def nothing():
    pass


def create_trackbar():
    namedWindow("range")
    createTrackbar("h1", "range", 90, 255, nothing)
    createTrackbar("s1", "range", 60, 255, nothing)
    createTrackbar("v1", "range", 40, 255, nothing)
    createTrackbar("h2", "range", 120, 255, nothing)
    createTrackbar("s2", "range", 255, 255, nothing)
    createTrackbar("v2", "range", 200, 255, nothing)


def get_trackbar():
    h1 = getTrackbarPos('h1', 'range')
    s1 = getTrackbarPos('s1', 'range')
    v1 = getTrackbarPos('v1', 'range')
    h2 = getTrackbarPos('h2', 'range')
    s2 = getTrackbarPos('s2', 'range')
    v2 = getTrackbarPos('v2', 'range')
    lower_blue = np.array([h1, s1, v1])
    upper_blue = np.array([h2, s2, v2])
    return [lower_blue, upper_blue]


def open_video(url):
    cap = VideoCapture(url)
    if not cap.isOpened():
        print("Błąd otwierania pliku")
        sys.exit(0)
    else:
        return cap

