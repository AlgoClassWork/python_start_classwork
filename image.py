from PIL import Image, ImageFilter

with Image.open('naruto.jpg') as picture:
    #picture.show()
    #print('Размер изображения', picture.size)
    #print('Формат картинки', picture.format)
    #print('Формат картинки', picture.mode)
    gray =  picture.convert('L') # ч\б фильтр
    blur = picture.filter(ImageFilter.BLUR) # мыло
    rotate = picture.transpose(Image.FLIP_LEFT_RIGHT) # зеркало
    rotate.save('naruto_zerkalo.jpg') # сохранить



