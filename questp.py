import time
from random import randint

def pause(seconds=1):
    time.sleep(seconds)

class Character:
    def __init__(self, name, weapon, damage, health):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.health = health
        self.alive = True

    def about(self):
        # Информация о персонаже
        print(f"\n{self.name} — великий мастер боевых искусств. Его оружие — {self.weapon}.")
        pause(1)
        print(f"Здоровье: {self.health} HP.\n")
        pause(1)

    def punch(self, opponent):
        # Симуляция удара с рандомным результатом
        print(f"\n{self.name} наносит удар с {self.weapon} по {opponent.name}...")
        pause(1)
        strike_type = randint(1, 3)

        if strike_type == 1:
            opponent.health -= self.damage
            print(f"Наносит урон! У противника {opponent.name} теперь {opponent.health} HP.")
        elif strike_type == 2:
            opponent.health -= self.damage * 2
            print(f"Критический удар! У противника {opponent.name} теперь {opponent.health} HP.")
        elif strike_type == 3:
            print(f"Промах! {self.name} не попал в {opponent.name}.")
        pause(1)
    
    def is_alive(self):
        return self.health > 0

    def fight(self, opponent):
        # Битва между двумя персонажами
        print("\nБитва начинается...\n")
        pause(1)
        
        while self.is_alive() and opponent.is_alive():
            # Случайный выбор, кто наносит удар
            turn = randint(1, 2)
            if turn == 1:
                self.punch(opponent)
            else:
                opponent.punch(self)
            
            pause(1)

        # Итог битвы
        if self.is_alive():
            print(f"\n{self.name} одерживает победу в этой жестокой битве!\n")
        else:
            print(f"\n{self.name} пал в бою... Но его имя будет жить в легендах.\n")

    def level_up(self):
        # Повышение уровня персонажа
        self.health *= 10
        self.damage *= 2
        print(f"\n{self.name} стал сильнее! Здоровье: {self.health} HP, Урон: {self.damage}.\n")
        pause(1)


# Создание персонажей
hero = Character(name='Мачо-Абу', weapon='Рука', damage=20, health=100)
villain = Character(name='Адольф', weapon='Сирюкен', damage=20, health=100)
dragon = Character(name='Страшный-Ычпачмак', weapon='Огонь', damage=50, health=500)
wizard = Character(name='Волшебник', weapon='Посох', damage=30, health=150)
mercenary = Character(name='Наемник', weapon='Меч', damage=40, health=200)

print('Добро пожаловать в игру "Рыцарь и дракон"!')
pause(1)
print('Ваша задача: пройти через опасные земли, сразиться с чудовищами и одержать победу над драконом.')
pause(1)
print('Вы начинаете свой путь из родного города Бишкек...')
pause(1)

print('По пути к логову дракона вы наткнулись на старый немецкий бункер.')
answer = input('Хотите осмотреть бункер или продолжить путь? (да/нет): ')

if answer.lower() == 'да':
    print('\nВы решаете осмотреть бункер...')
    pause(1)
    print('Вдалеке вы замечаете большое чудовище с усами...')
    pause(1)
    print('Оно напоминает злого магистра боевых искусств, готовьтесь к бою!')
    villain.about()
    hero.fight(villain)
    
    if hero.is_alive():
        print('\nВы восстановили здоровье и стали ещё сильнее после победы!')
        hero.level_up()
        pause(1)
        print('Дорога продолжена... наконец-то вы подошли к логову дракона.')
        pause(1)
        print('Он вас ждал. Вы его ждали. И принцесса вас ждала...')
        pause(1)
        print('Готовьтесь к решающему бою!')
        dragon.about()
        hero.fight(dragon)
        
        if hero.is_alive():
            print('Поздравляем! Вы победили дракона, спасли принцессу и забрали сокровища!')
            pause(2)
            print('Вам предстоит стать легендой, и ваше имя будут помнить веками.')
        else:
            print('Конец путешествия. Вы погибли в бою с драконом... Но ваш дух будет жить в легендах.')
    else:
        print('\nКонец путешествия. Вы погибли в бою с чудовищем...')
else:
    print('Такой трус до дракона не доберется. Прощайте!')
    pause(2)
    print('Путеводная звезда погасла, и ваше приключение закончилось...')
    time.sleep(3)

