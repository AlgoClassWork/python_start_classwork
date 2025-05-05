import cv2
import matplotlib.pyplot as plt
# Загрузка изображения
image = cv2.imread('face2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
# Загрузка классификатора
face_cascade = cv2.CascadeClassifier('face.xml')
# Обнаружение лиц
faces = face_cascade.detectMultiScale(gray)
# Отрисовка прямоугольников на лицах
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Отображение изображения
plt.imshow(image), plt.axis('off'), plt.show()



# для видео

import cv2

face_cascade = cv2.CascadeClassifier('face.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Камера', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
