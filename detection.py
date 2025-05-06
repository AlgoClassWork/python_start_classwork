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

plt.imshow(rgb)
plt.axis('off')
plt.show()
