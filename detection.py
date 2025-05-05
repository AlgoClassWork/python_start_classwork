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
