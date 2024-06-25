from random import randint
from time import sleep

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

knight = Person(name='Олег',health=150,damage=30,weapon='меч')
razboinik = Person(name='Адольф',health=150,damage=30,weapon='сирюкен')
dragon = Person(name='Смауг',health=200,damage=50,weapon='фаербол')

print('Бравый рыцарь по имени',knight.name,'\n')
sleep(1)
print('пошел в поход за головой дракона','\n')
sleep(1)
print('по пути он встретил заброшенный немецкий бункер','\n')
sleep(1)
print('из него выглядывает какое то существо','\n')
sleep(1)
otvet = input('Хотите сразится?')
if otvet == 'да':
    print('Вы повстречали самого',razboinik.name,'\n')
    sleep(1)
    print('Оказывается он выжил после 45','\n')
    sleep(1)
    print('Да начнется сражение','\n')
    sleep(1)
    while knight.health > 0 and razboinik.health > 0:
        knight.udar(razboinik)
        print('\n')
        razboinik.udar(knight)
        print('\n')
    if knight.health > razboinik.health:
        print('Победил',knight.name,'\n')
        sleep(1)
        print('Теперь он стал сильнее','\n')
        knight.health += 100
        knight.damage *= 2
        print('Теперь его статы равны',knight.health,'/', knight.damage,'\n')
        sleep(1)
        print('Наконец наш герой добрался до пещеры дракона','\n')
        sleep(1)
        print('Да начнется битва','\n')
        while knight.health > 0 and dragon.health > 0:
            knight.udar(dragon)
            print('\n')
            dragon.udar(knight)
            print('\n')
        if knight.health > dragon.health:
            print('Победил',knight.name,'\n')
            sleep(1)
            print('Теперь он может забрать голову дракона и купить себе оружию броню и пачку сухариков')
        else:
            print('В следующий раз одевай шапку')
        
    else:
        print(knight.name,'пал в этом не легком бою','\n')

