# ООП - ОБЬЕКТНО ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ
# Обьект - Набор данных и действий которые мы привыкли называть каким то именем
# Ориентированный - Нацелен
# Программирование - Процесс написание программ (кода)
# Класс - группа обьектов со схожими признаками
# Зачем нужны классы ? Класс нужен чтобы создавать обьекты
# Класс - описание будущего обьекта
# __init__ - магический метод (конструктор)
# запускается при использовании класса (создание обьекта)
# self - ссылка на текущий обьект
# свойство - переменная внутри класса (описание обьекта пример: вес рост)
# метод - функция внутри класса (действие вашего обьекта например удар)

class Person:
    def __init__(self, name, speed, weapon ):
        self.name = name
        self.health = 100
        self.damage = 10
        self.speed = speed
        self.weapon = weapon

    def heal(self):
        self.health += 25
        print(self.name,'восполнил здоровье:')
        print('Текущий уровень здоровья', self.health)

    def punch(self, vrag):
        vrag.health -= self.damage
        print(self.name , 'ударил', self.weapon)
        print(vrag.name, 'получил урон')
        print('У него осталось', vrag.health, 'здоровья')

hero = Person(name='Генадий', speed=10, weapon='меч')
enemy = Person(name='Адольф', speed=10, weapon='палка')

hero.punch(enemy)
hero.punch(enemy)
enemy.punch(hero)
hero.heal()




