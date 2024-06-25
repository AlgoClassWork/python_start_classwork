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
        enemy.health -= self.damage
        print('Здоровье',enemy.health)

knight = Person(name='Олег',health=100,damage=10,weapon='меч')
razboinik = Person(name='Адольф',health=90,damage=9,weapon='сирюкен')
dragon = Person(name='Смауг',health=200,damage=50,weapon='фаербол')

while knight.health > 0 and razboinik.health > 0:
    knight.udar(razboinik)
    razboinik.udar(knight)
