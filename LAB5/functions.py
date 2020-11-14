# from cv2 import *
from cv2 import *
import numpy as np


def open_video(url):
    cap = VideoCapture(url)
    if not cap.isOpened():
        print("Błąd otwierania pliku")
        sys.exit(0)
    else:
        return cap


def get_img(cap):
    success, img = cap.read()
    if waitKey(20) & 0xFF == ord('q'):
        cap.release()
        destroyAllWindows()
        exit(0)
    if success:
        return img
    else:
        cap.release()
        destroyAllWindows()
        exit(9000)
