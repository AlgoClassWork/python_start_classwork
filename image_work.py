#pip install pillow
from PIL import Image, ImageOps, ImageEnhance

picture = Image.open('pica.jpg')
print('Размер изображения:', picture.size)
print('Формат:', picture.format)
print('Тип:', picture.mode)

picture_rotate = picture.rotate(180)
picture_rotate.save('pica_rotate.jpg')

picture_gray = ImageOps.grayscale(picture)
picture_gray.save('pica_gray.jpg')

picture_mirror = ImageOps.mirror(picture)
picture_mirror.save('pica_mirror.jpg')

picture_contrast = ImageEnhance.Contrast(picture).enhance(10)
picture_contrast.save('pica_contrast.jpg')
