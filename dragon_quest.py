from random import *

class Person():
    def __init__(self,name,weapon,health,damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage
    
    def punch(self,vrag):
        print(self.name,'наносит удар с помощью',self.weapon+'a',vrag.name+'у')
        udar = randint(1,3)
        if udar == 1:
            vrag.health -= self.damage * 2
            print('Крит урон',self.damage * 2,'у противника осталось',vrag.health,'хп')
        if udar == 2:
            vrag.health -= self.damage
            print('Атака прошла успешна',self.damage,'у противника осталось',vrag.health,'хп')
        if udar == 3:
            print('Промах')

hero = Person(name='Джон',weapon='Меч',health=100,damage=20)
enemy = Person(name='Адольф',weapon='Сирюкен',health=90,damage=18)
dragon = Person(name='Смауг',weapon='Огонь',health=200,damage=40)
