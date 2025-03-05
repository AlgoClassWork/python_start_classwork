import time
from random import randint

# Функция для задержки текста, чтобы игрок мог успевать читать
def slow_print(text, delay=1.5):
    print(text)
    time.sleep(delay)

# Класс персонажа (Sprite) с улучшенными методами
class Sprite:
    def __init__(self, name, health, damage, weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

    # Метод для вывода информации о персонаже
    def about(self):
        slow_print(f'На поле боя появился {self.name}...')
        slow_print(f'В его руках находится {self.weapon}.')
        slow_print(f'Его статы: Здоровье - {self.health}, Урон - {self.damage}\n')

    # Метод для выполнения удара
    def strike(self, opponent):
        rand_num = randint(1, 3)
        slow_print(f'{self.name} совершил удар по {opponent.name}...')

        if rand_num == 1:
            opponent.health -= self.damage
        elif rand_num == 2:
            opponent.health -= self.damage * 2
            slow_print('Критический удар! Урон удвоен!\n', delay=1)
        else:
            slow_print('Промах... Удар не достиг цели!\n', delay=1)

        slow_print(f'Уровень здоровья {opponent.name} опустился до {opponent.health} хп.\n', delay=1)

    # Метод для сражения
    def fight(self, opponent):
        slow_print(f'\nСражение между {self.name} и {opponent.name} начинается...\n', delay=2)

        # Пока оба бойца живы
        while self.health > 0 and opponent.health > 0:
            self.strike(opponent)
            if opponent.health > 0:
                opponent.strike(self)
        
        # Вывод результата сражения
        if self.health > 0:
            # Если герой победил
            self.damage *= 5
            self.health += 150
            slow_print(f'Герой пережил битву и стал сильнее! Теперь его статы: Здоровье - {self.health}, Урон - {self.damage}\n', delay=2)
        else:
            slow_print(f'{self.name} пал в этом нелегком бою против {opponent.name}.\n', delay=2)

# Создание персонажей
player = Sprite(name='Абу', health=100, damage=10, weapon='меч')
enemy = Sprite(name='Пикачу', health=150, damage=8, weapon='молнии')
dragon = Sprite(name='Смауг', health=200, damage=40, weapon='огонь')

# Начальная история
slow_print('Бравый герой по имени Абу отправился в путешествие за принцессой и сокровищем...', delay=2)
slow_print('По дороге к логову дракона он натыкается на ужасное электрическое чудище...')

# Вопрос о сражении
answer = input('Хотите сразиться с чудищем и стать сильнее? (да/нет): ')
if answer.lower() == 'да':
    player.fight(enemy)
else:
    slow_print('Хорошо, что вы струсили. У него был пульт от ядерной ракеты...')

# Проверка состояния игрока после сражения с Пикачу
if player.health > 0:
    slow_print('Вы добрались до логова дракона. Готовьтесь к сражению с ним...', delay=2)
    player.fight(dragon)

# Финал игры в зависимости от состояния здоровья игрока
if player.health > 0:
    slow_print('Вы забрали много сокровищ и спасли принцессу. Живите счастливо!', delay=2)
else:
    slow_print('Вы слишком слабый для этого мира... Но, возможно, когда-нибудь вы вернетесь сильнее...', delay=2)

