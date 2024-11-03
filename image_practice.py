from PIL import Image, ImageOps, ImageEnhance

with Image.open('негр.jpg') as picture:
    # ИНФОРМАЦИЯ О КАРТИНКЕ
    print('Размер картинки', picture.size)
    print('Формат картинки', picture.format)
    print('Тип', picture.mode)
    #picture.show()
    # Ч.Б ФИЛЬТР
    gray_picture = ImageOps.grayscale(picture)
    print('Тип', gray_picture.mode)
    #gray_picture.show()
    # ПОВОРОТ
    rotate_picture = picture.rotate(180)
    #rotate_picture.show()
    # ЗЕРКАЛО
    mirror_picture = ImageOps.mirror(picture)
    #mirror_picture.show()
    contrast_picture = ImageEnhance.Contrast(picture)
    contrast_picture = contrast_picture.enhance(10)
    #contrast_picture.show()
    # СОХРАНЕНИЕ
    gray_picture.save('серый негр.jpg')
    rotate_picture.save('повернутый негр.jpg')
    mirror_picture.save('зеркальный негр.jpg')
    contrast_picture.save('негр в контрасте.jpg')
