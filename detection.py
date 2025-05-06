# pip install opencv-python
import cv2
# pip install matplotlib
import matplotlib.pyplot as plt

original_img = cv2.imread('face1.jpg')
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
rgb_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

face = cv2.CascadeClassifier('face.xml')
result = face.detectMultiScale(gray_img)

for (x, y, w, h) in result:
    cv2.rectangle( rgb_img, (x, y), (x + w, y + h), (0, 255, 0), 5 )

plt.imshow(rgb_img)
plt.axis('off')
plt.show()



# ВИДЕО ДЕТЕКЦИЯ
import cv2

face = cv2.CascadeClassifier('face.xml')

camera = cv2.VideoCapture(0)

while True:
    _ , frame = camera.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = face.detectMultiScale(gray_img)

    for (x, y, w, h) in result:
        cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 255, 0), 5 )

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
