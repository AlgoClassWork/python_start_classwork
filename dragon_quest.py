from random import *
from time import sleep

class Person():
    def __init__(self,name,weapon,health,damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage
    
    def punch(self,vrag):
        print(self.name,'наносит удар с помощью',self.weapon+'а',vrag.name+'у')
        udar = randint(1,3)
        if udar == 1:
            vrag.health -= self.damage * 2
            print('Крит урон у противника. Осталось',vrag.health,'хп')
        elif udar == 2:
            vrag.health -= self.damage
            print('Атака прошла успешно. Осталось',vrag.health,'хп')
        else:
            print('Промах')

    def fight(self,vrag):
        while self.health > 0 and vrag.health > 0:
            self.punch(vrag)
            sleep(1)
            if vrag.health <= 0:
                break
            vrag.punch(self)
            sleep(1)
            print('\n')

        if self.health > 0:
            print(vrag.name,'пал в этом нелегком бою.')
            print('Вы получили усиление. Теперь ваши статы равны:')
            self.health *= 8
            self.damage *= 2
            print('Урон:', self.damage, 'Здоровье:', self.health)
        else:
            print('Game over')
            return False
        return True

def introduction():
    print("Вы - рыцарь Джон, отважный искатель приключений, отправившийся на поиски легендарного сокровища.")
    print("Ваш путь лежит через мрачный и таинственный лес, где скрыты неведомые опасности.")
    print("Вы оказались перед заброшенным немецким бункером, в котором ощущается зловещее присутствие.")
    print("Вы можете войти внутрь и столкнуться с возможной угрозой или обойти это место стороной.")
    print()

def encounter_bunker():
    print("Вы решаете войти в бункер, надеясь найти что-то полезное или встретить врага.")
    print("Внутри вас встречает ужасный враг - Адольф, владелец таинственного оружия.")
    print("Вы должны решить, будете ли вы сражаться с ним или попытаетесь избежать боя.")
    choice = input("Выберите: (сражаться / избежать): ").strip().lower()
    if choice == "сражаться":
        print("Вы решаете сразиться с Адольфом.")
        return True
    elif choice == "избежать":
        print("Вы решаете обойти бункер стороной и продолжить свой путь.")
        return False
    else:
        print("Неверный выбор. Попробуйте снова.")
        return encounter_bunker()

def dragon_lair():
    print("Ваше путешествие приводит вас в логово дракона, где охраняется сокровище.")
    print("Перед вами появляется огромный дракон Смауг, который готовится к бою.")
    print("Вы должны сразиться с ним, чтобы получить сокровище или погибнуть в этом бою.")
    return input("Сразиться с драконом? (да / нет): ").strip().lower() == "да"

def game_loop():
    hero = Person(name='Джон', weapon='Меч', health=100, damage=20)
    enemy = Person(name='Адольф', weapon='Сирюкен', health=90, damage=18)
    dragon = Person(name='Смауг', weapon='Огонь', health=200, damage=40)

    introduction()
    if encounter_bunker():
        hero.fight(enemy)
        if hero.health <= 0:
            return
    else:
        print("Вы обходите бункер и продолжаете путь к логову дракона.")
    
    if dragon_lair():
        if hero.fight(dragon):
            print("Поздравляю! Вы победили дракона и получили сокровище!")
        else:
            print("Вы не смогли одолеть дракона. Ваше приключение окончено.")
    else:
        print("Вы решили не сражаться с драконом и покинули его логово. Ваше приключение окончено.")

game_loop()
