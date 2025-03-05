from random import randint

class Sprite:
    def __init__(self, name, health, damage, weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

    def about(self):
        print(f'На поле боя появился {self.name}')
        print(f'В его руках находится {self.weapon}')
        print(f'Его статы: {self.health} | {self.damage} \n')

    def strike(self, opponent):
        rand_num = randint(1,3)
        print(f'{self.name} совершил удар по {opponent.name}')
        if rand_num == 1:
            opponent.health -= self.damage
        if rand_num == 2:
            opponent.health -= self.damage * 2
            print('Крит удар')
        if rand_num == 3:
            print('Промах')
        print(f'Уровень здоровья {opponent.name} опустился до {opponent.health} хп \n')

    def fight(self, opponent):
        while self.health > 0 and opponent.health > 0:
            self.strike(opponent)
            opponent.strike(self)

        if self.health > 0:
            self.damage *= 5
            self.health += 150
            print(f'Герой пережил битву и стал сильнее теперь его статы равны {self.health} | {self.damage}')
        else:
            print(f'{self.name} пал в этом нелегком бою против {opponent.name}')

player = Sprite(name='Абу', health=100, damage=10, weapon='меч')
enemy = Sprite(name='Пикачу', health=150, damage=8, weapon='молнии')
dragon = Sprite(name='Смауг', health=200, damage=40, weapon='огонь')



