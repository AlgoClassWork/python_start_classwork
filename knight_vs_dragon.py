class Person:
    def __init__(self,name,health,damage,weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

knight = Person(name='Олег',health=100,damage=10,weapon='меч')
razboinik = Person(name='Адольф',health=90,damage=9,weapon='сирюкен')
dragon = Person(name='Смауг',health=200,damage=50,weapon='фаербол')
