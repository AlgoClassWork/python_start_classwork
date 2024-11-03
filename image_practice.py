from PIL import Image, ImageOps, ImageEnhance

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename 
        self.original = Image.open(self.filename)
        self.changes = [] 
        
    def do_black(self):
        black = ImageOps.grayscale(self.original)
        self.changes.append(black)
        temp = self.filename.split('.') 
        new = temp[0] + str(len(self.changes)) + '.jpg'
        black.save(new)

    def flip(self):
        flip = self.original.rotate(180)
        self.changes.append(flip)
        temp = self.filename.split('.') 
        new = temp[0] + str(len(self.changes)) + '.jpg'
        flip.save(new)

image = ImageEditor('негр.jpg')
image.flip()
image.do_black()
