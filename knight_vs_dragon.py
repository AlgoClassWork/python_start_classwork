from random import randint

class Person:
    def __init__(self,name,health,damage,weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

    def info(self):
        print('На поле боя появился',self.name)
        print('Его секретное оружие это',self.weapon)

    def udar(self,enemy):
        print(self.name,'наносит удар при помощи',self.weapon,enemy.name)
        num = randint(1,3)
        if num == 1:
            enemy.health -= self.damage
        if num == 2:
            enemy.health -= self.damage * 2
            print('крит')
        if num == 3:
            print('промах')

knight = Person(name='Олег',health=100,damage=10,weapon='меч')
razboinik = Person(name='Адольф',health=100,damage=10,weapon='сирюкен')
dragon = Person(name='Смауг',health=200,damage=50,weapon='фаербол')

