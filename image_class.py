import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
from PIL import Image
import requests

# Загружаем модель классификации изображений
model = hub.load("https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_s/classification/2")

# Загружаем метки классов (названия объектов)
labels = requests.get("https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt").text.splitlines()

# Загружаем и подготавливаем изображение
img = Image.open("img1.jpg").resize((224, 224))  # Изменяем размер
x = np.expand_dims(np.array(img) / 255.0, axis=0).astype(np.float32)  # Преобразуем в массив

# Делаем предсказание
preds = model(x)
probs = tf.nn.softmax(preds)[0].numpy()  # Преобразуем в вероятности

# Показываем топ-5 предсказаний
top = probs.argsort()[-5:][::-1]
for i in top:
    print(f"{labels[i]}: {probs[i]*100:.2f}%")

# Проверяем наличие конкретного объекта (например, "banana")
name = "banana"
if name in labels:
    i = labels.index(name)
    print(f"\nВероятность, что на изображении {name}: {probs[i]*100:.2f}%")
