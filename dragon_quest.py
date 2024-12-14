from random import randint
import time

# Класс персонажа
class Person:
    def __init__(self, name, weap, hp, dmg):
        self.name = name        # Имя персонажа
        self.weapon = weap      # Оружие персонажа
        self.health = hp        # Здоровье
        self.damage = dmg       # Урон, который персонаж наносит
        self.alive = True       # Жив ли персонаж

    def hello(self):
        """Приветствие персонажа."""
        print(f"{self.name} говорит привет.")

    def punch(self, enemy):
        """Удар по врагу с случайным эффектом."""
        num = randint(1, 3)  # Рандом для разнообразных ударов
        if num == 1:
            enemy.health -= self.damage
            print(f"{self.name} наносит удар по {enemy.name}!")
        elif num == 2:
            enemy.health -= self.damage * 2
            print(f"{self.name} наносит критический удар по {enemy.name}!")
        elif num == 3:
            enemy.health -= self.damage // 2
            print(f"{self.name} немного промахивается, нанося слабый удар по {enemy.name}...")
        
        # Проверка состояния врага после удара
        print(f"{enemy.name} осталось {enemy.health} здоровья.")
        if enemy.health <= 0:
            enemy.alive = False
            print(f"{enemy.name} погиб!")

    def fight(self, enemy):
        """Бой между персонажами."""
        print(f"\nНачинается бой между {self.name} и {enemy.name}!")
        time.sleep(1)  # Пауза для атмосферы
        
        while self.alive and enemy.alive:
            if self.alive:
                self.punch(enemy)
                time.sleep(1)  # Задержка после удара

            if enemy.alive:
                enemy.punch(self)
                time.sleep(1)  # Задержка после удара врага

        if self.alive:
            print(f"\n{self.name} победил в этом нелегком бою!")
        else:
            print(f"\n{enemy.name} одолел {self.name} в бою.")

# Создаем героев
hero = Person(name='Шрек', weap='меч', hp=100, dmg=25)
enemy = Person(name='Осел', weap='копыта', hp=150, dmg=15)
dragon = Person(name='Смауг', weap='фаербол', hp=300, dmg=50)

# Начало игры с коротким введением
print("Добро пожаловать в игру 'Рыцарь и Дракон'!")
time.sleep(2)

# Вступительная часть
print("\nВ вашем мире ходят легенды о героях и чудовищах. Один из таких героев — Шрек.")
time.sleep(2)
print("Он известен своей силой и храбростью, но сегодня ему предстоит столкнуться с серьезным врагом...")
time.sleep(2)

# Бой с врагом
hero.fight(enemy)

# Бой с драконом (если герой победил)
if hero.alive:
    print("\nПосле победы над Оселом, Шрек решает бросить вызов самому страшному чудовищу - дракону Смаугу!")
    time.sleep(2)
    hero.fight(dragon)

else:
    print("\nШрек потерпел поражение, но его история не заканчивается здесь...")
