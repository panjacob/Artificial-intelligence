from cv2 import *

# face_cascade = cv2.CascadeClassifier("resources/haarcascade_frontalcatface.xml")
face_cascade = cv2.CascadeClassifier("resources/haarcascade_eye.xml")
img = imread('resources/lenna.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
print(len(faces))
for (x, y, w, h) in faces:
    face = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
imshow('test', img)

if waitKey(1000000) & 0xFF == ord('q'):
    pass
