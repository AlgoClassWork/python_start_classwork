from random import randint
from time import sleep

class Hero:
    def __init__(self,name,weapon,health,power):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power
    
    def info(self):
        print('На поле битвы появляется',self.name)
        print('В руках он держит',self.weapon)

    def fight(self,opponent):
        print('Началось сражение между', self.name, 'и', opponent.name)
        while self.health > 0 and opponent.health > 0:
            print(self.name,'наносит удар',opponent.name,)

            udar = randint(1,3)
            if udar == 1:
                opponent.health -= 0
                print('Промах')
            elif udar == 2:
                opponent.health -= self.power
                print('Есть пробитие')
            else:
                opponent.health -= self.power * 2
                print('Сработал крит')

            sleep(1)
            print('\n')

            print(opponent.name,'отвечает',self.name,)
            udar = randint(1,3)
            if udar == 1:
                self.health -= 0
                print('Промах')
            elif udar == 2:
                self.health -= opponent.power
                print('Есть пробитие')
            else:
                self.health -= opponent.power * 2
                print('Сработал крит')

            sleep(1)
            print('\n')

        if self.health > opponent.health:
            print('Победил', self.name)
        else:
            print('Победил',opponent.name)

knight = Hero('Артур','меч',100,10)
enemy = Hero('Адольф','сирюкен',90,9)
knight.fight(enemy)
