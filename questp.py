from random import randint

class Person:
    def __init__(self,name, weapon, damage, health):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.health = health
        self.alive = True
        
    def about(self):
        print('Меня зовут', self.name, 'Я сражаюсь', self.weapon)
        print('Мое здоровье на уровне', self.health, 'очков')

    def punch(self, vrag):
        print(self.name, 'наносит удар', self.weapon, 'по', vrag.name)
        udar = randint(1,3)
        if udar == 1:
            vrag.health -= self.damage
        if udar == 2:
            print('Крит')
            vrag.health -= self.damage * 2
        if udar == 3:
            print('Промах')

player = Person(name='Мачо-Абу', weapon='Рука', damage=5, health=100)
enemy = Person(name='Адольф', weapon='Сирюкен', damage=15, health=50)
print('Здоровье врага', enemy.health)
player.punch(enemy)
print('Здоровье врага', enemy.health)


