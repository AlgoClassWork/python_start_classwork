import tensorflow_hub
import tensorflow
import numpy
from PIL import Image
import requests

# pip install tensorflow, tensorflow_hub, numpy, pillow
# visual c++ с сайта microsoft и python версии не выше 3.12

model = tensorflow_hub.load('https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_l/classification/2')
labels = requests.get("https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt").text.splitlines()

image = Image.open('bars.jpg').resize((500,500))
x = numpy.expand_dims( numpy.array(image) / 255, axis=0).astype(numpy.float32)

predict = model(x)
probs = tensorflow.nn.softmax(predict)[0].numpy()

top_five = probs.argsort()[-5:][::-1]
for element in top_five:
    print(f' {labels[element]} : {probs[element] * 100}%')
