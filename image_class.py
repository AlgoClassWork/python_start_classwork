labels = requests.get("https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt").text.splitlines()
