class Hero:
    def __init__(self,name,weapon,health,power):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power
    
    def info(self):
        print('На поле битвы появляется',self.name)
        print('В руках он держит',self.weapon)

knight = Hero('Артур','меч',100,10)
enemy = Hero('Адольф','сирюкен',90,9)
