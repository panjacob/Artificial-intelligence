from cv2 import *

cap = VideoCapture("film/szukaj_zielonego.webm")

if not cap.isOpened():
    print("Błąd otwierania pliku")

print("Wymiary: " + str(CAP_PROP_FRAME_WIDTH) + "x" + str(CAP_PROP_FRAME_HEIGHT))

while True:
    success, img = cap.read()
    if success:
        flip(img, +1, img)
        imshow("Video", img)
    else:
        break
    if waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
destroyAllWindows()
