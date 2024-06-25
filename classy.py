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
            print(self.name,'наносит удар',opponent.name)
            opponent.health -= self.power
            print(opponent.name,'отвечает',self.name)
            self.health -= opponent.power
        if self.health > opponent.health:
            print('Победил', self.name)
        else:
            print('Победил',opponent.name)

knight = Hero('Артур','меч',100,10)
enemy = Hero('Адольф','сирюкен',90,9)
knight.fight(enemy)
