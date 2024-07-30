class Person():
    def __init__(self,name,weapon,health,damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage

hero = Person(name='Джон',weapon='Меч',health=100,damage=20)
enemy = Person(name='Адольф',weapon='Сирюкен',health=90,damage=18)
dragon = Person(name='Смауг',weapon='Огонь',health=200,damage=40)
