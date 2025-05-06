# pip install opencv-python
# pip install matplotlib
import cv2
import matplotlib.pyplot as plt

original = cv2.imread('face.jpg')
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

face = cv2.CascadeClassifier('face.xml')

result = face.detectMultiScale(gray)

for (x, y, w, h) in result:
    cv2.rectangle(rgb, (x, y), (x + w, y + h), (0,255,0), 1)



# ВИДЕО ДЕТЕКЦИЯ
import cv2

face = cv2.CascadeClassifier('face.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = face.detectMultiScale(gray)

    for (x, y, w, h) in result:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

plt.imshow(rgb)
plt.axis('off')
plt.show()
