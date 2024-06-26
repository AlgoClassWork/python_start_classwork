from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = Image.open(filename)
        self.modified = list() 

    def gray(self):
        gray = self.original.convert('L')
        # автонейминг
        self.modified.append(gray)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.modified)) + '.' + temp_filename[1]
        gray.save(new_filename)

    def blur(self):
        blur = self.filter(ImageFilter.BLUR)
        # автонейминг
        self.modified.append(blur)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.modified)) + '.' + temp_filename[1]
        blur.save(new_filename)


picture1 = ImageEditor('pepe.jpg')
picture1.blur()
picture1.gray()

