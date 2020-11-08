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


def numpy_array(array):
    [a, b, c, d] = array
    a = (a[0][0], a[0][1])
    b = (b[0][0], b[0][1])
    c = (c[0][0], c[0][1])
    d = (d[0][0], d[0][1])
    return [a, b, c, d]


def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)

    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect


def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    maxWidth = int(maxWidth[0][0])

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    maxHeight = int(maxHeight[0][0])
    # print(maxHeight)

    # maxWidth = 640
    # maxHeight = 360

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    # return the warped image
    return warped, maxWidth, maxHeight
