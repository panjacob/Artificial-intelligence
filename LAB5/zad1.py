from LAB5.functions import *

cap = open_video('resources/cars.mp4')
car_cascade = cv2.CascadeClassifier("resources/cars2.xml")

trackers = []
passed_cars = 0


def is_overlap(x2, y2, w2, h2):
    if len(trackers) == 0:
        return False
    for tracker, box in trackers:
        (x1, y1, w1, h1) = box
        if not ((x1 >= x2 + w2 or x2 >= x1 + w1) and (y1 <= y2 + h2 or y2 <= y1 + h1)):
            return True
    return False


def new_tracker(img, box):
    (x, y, w, h) = box
    if not is_overlap(x, y, w, h):
        tracker = TrackerMOSSE_create()
        tracker.init(img, box)
        trackers.append((tracker, box))


def update_trackers(img, passed_cars):
    for tracker, box in trackers:
        ok, bbox = tracker.update(img)
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(img, p1, p2, (0, 0, 255), 2)
        else:
            trackers.remove((tracker, box))
            passed_cars += 1
    return passed_cars


while True:
    img = get_img(cap)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(img_gray, 1.5, 4)
    for (x, y, w, h) in cars:
        if not is_overlap(x, y, w, h):
            new_tracker(img, (x, y, w, h))

    passed_cars = update_trackers(img, passed_cars)

    text = 'now: ' + str(len(trackers)) + "   passed: " + str(passed_cars)
    putText(img, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    imshow("Video", img)
