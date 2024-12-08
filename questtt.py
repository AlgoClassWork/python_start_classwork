from random import randint

class Person:
    def __init__(self, name, weap, hp, dmg):
        self.name = name
        self.weapon = weap
        self.health = hp
        self.damage = dmg
    
    def hello(self):
        print(self.name,'говорит привет')

    def punch(self,vrag):
        num = randint(1,3)
        if num == 1:
            vrag.health -= self.damage
            print(self.name,'наносит удар', vrag.name)
        if num == 2:
            vrag.health -= self.damage * 2
            print(self.name,'наносит удар и выпадает крит', vrag.name)
        if num == 3:
            vrag.health -= self.damage / 2
            print(self.name,'наносит удар и немного промахивается', vrag.name)
        print(vrag.name,'осталось',vrag.health,'здоровья')

hero = Person(name='Шрек', weap='меч', hp=100, dmg=25)
enemy = Person(name='Осел', weap='копыта', hp=150, dmg=15)
dragon = Person(name='Смауг', weap='фаер бол', hp=300, dmg=50)


