# версия python ниже 3.13
# скачать visual c++
# pip install pillow
from PIL import Image
import tensorflow_hub
import tensorflow
import requests
import numpy

model = tensorflow_hub.load('https://tfhub.dev/google/imagenet/mobilenet_v3_small_075_224/classification/5')
labels = requests.get("https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt").text.splitlines()

image = Image.open('bars.jpg').resize((224,224))
image = numpy.expand_dims(numpy.array(image) / 255, axis=0 ).astype(numpy.float32)

predict = model(image)
probs = tensorflow.nn.softmax(predict)[0].numpy()

for predict in probs.argsort()[-5:] :
    print(f' {labels[predict]} : {probs[predict] * 100 } %')
