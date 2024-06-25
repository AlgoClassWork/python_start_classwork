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
        print('Началось сражение между', self.name, 'и', opponent.name,'\n')
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

knight = Hero('Артур','меч',100,100)
enemy = Hero('Адольф','сирюкен',90,25)
dragon = Hero('Смауг','фаербол',250,50)

print('Бравый рыцарь по имени',knight.name,'отправился в логово дракона','\n')
sleep(2)
print('На пути нашего рыцарь появилась преграда нацисткий танк','\n')
sleep(2)
print('Вы даже не представляете кто в нем сидит','\n')
sleep(2)
otvet = input('Хотите узнать и сразится?')
if otvet == 'да':
    print('Так точно этот тот самый','\n', enemy.name)
    sleep(2)
    knight.fight(enemy)
    if knight.health > enemy.health:
        knight.health = 200
        knight.power *= 2
        print('Вы выйграли и наконецто добрались до логова дракона','\n')
        sleep(2)
        print('можете немного передохнуть секунд так 5','\n')
        sleep(5)
        print('ииииии в бой','\n')
        knight.fight(dragon)
        if knight.health > dragon.health:
            print('Поздравляем с победой в сундуке лежит пачка сухариков с сыром')
        else:
            print('За это стоило умереть')
    else:
        print('Победил',opponent.name,'\n')
        print('Твое путешествие окончено :(')
    

