from random import randint
from time import sleep

def pause():
    sleep(0.6)


# ======= БАЗОВЫЙ КЛАСС ПЕРСОНАЖА =======
class Person:
    def __init__(self, name, weapon, luck, damage):
        self.name = name
        self.weapon = weapon
        self.luck = luck
        self.damage = damage
        self.max_health = 30
        self.health = self.max_health

    def is_alive(self):
        return self.health > 0

    def punch(self, target):
        luck_factor = randint(1, self.luck)
        dmg = randint(self.damage // 2, self.damage) + luck_factor // 3
        dmg = max(1, dmg)

        print(f"{self.name} атакует {target.name} ({self.weapon}).")
        pause()

        target.health -= dmg
        if target.health < 0:
            target.health = 0

        print(f"Урон: {dmg}")
        print(f"Здоровье {target.name}: {target.health}\n")
        pause()

    def fight(self, target):
        print(f"\n=== БОЙ: {self.name} против {target.name} ===\n")

        while self.is_alive() and target.is_alive():
            self.punch(target)
            if target.is_alive():
                target.punch(self)

        if self.is_alive():
            print(f"{self.name} одержал победу!")
            return True
        else:
            print(f"{self.name} пал в бою...")
            return False

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"\n{self.name} восстанавливает здоровье. Теперь: {self.health}\n")


# ======= СЮЖЕТНЫЕ СЦЕНЫ =======

def intro():
    print("Ты — Артур, молодой путник, ищущий свою судьбу.")
    pause()
    print("Сегодня ты подошёл к лесу, о котором ходят легенды.")
    pause()
    print("Говорят, в его глубине скрыт Смауг — древний дракон.")
    pause()
    print("Но сначала нужно добраться до его логова...\n")
    pause()

def crossroad():
    print("\nТы подходишь к развилке дорог. Куда пойдёшь?\n")
    print("1 — направо, к старой башне")
    print("2 — налево, к туманному болоту")
    print("3 — прямо через тёмный лес")
    choice = input("Твой выбор: ")

    return choice


def tower_path(player):
    print("\nТы идёшь к старой башне.")
    pause()
    print("Перед входом стоит рыцарь Адольф, похожий на стража.")
    pause()
    print("Он поднимает меч: «Назад! Здесь не место слабым!»\n")

    print("1 — попытаться договориться")
    print("2 — вступить в бой")
    choice = input("Твой выбор: ")

    if choice == "1":
        print("\nТы пытаешься убедить рыцаря пропустить тебя.")
        pause()
        success = randint(1, 10) <= player.luck // 3
        if success:
            print("Адольф долго смотрит на тебя, затем медленно опускает меч.")
            pause()
            print("«Иди. Но помни: дракон не знает пощады.»")
            return "skip_enemy"
        else:
            print("«Слова — пустота. Покажи силу!» — рыцарь нападает!\n")
            return "fight_enemy"
    else:
        return "fight_enemy"


def swamp_path(player):
    print("\nТы идёшь к туманному болоту.")
    pause()
    print("Под ногами тихо хлюпает грязь, что-то шевелится в воде.")
    pause()
    print("Из-за камышей появляется торговец-отшельник.\n")
    print("— Хочешь зелье выносливости? Всего одна монета... — шепчет он.")

    print("\n1 — купить зелье")
    print("2 — отказаться")
    choice = input("Твой выбор: ")

    if choice == "1":
        print("\nТы покупаешь зелье и выпиваешь его.")
        pause()
        print("Ты чувствуешь, как сила возвращается.")
        player.heal(20)
        return "safe"
    else:
        print("\nТы обходишь торговца стороной.")
        pause()
        print("Туман сгущается... но путь остаётся безопасным.")
        return "safe"


def forest_path(player):
    print("\nТы идёшь через тёмный лес.")
    pause()
    print("Среди деревьев мелькают тени... что-то следит за тобой.")
    pause()
    print("Внезапно на тропу выскакивает Адольф — разбойник!\n")

    print("1 — убежать")
    print("2 — сразиться")
    choice = input("Твой выбор: ")

    if choice == "1":
        success = randint(1, 10) <= player.luck // 2
        if success:
            print("\nТы успеваешь скрыться среди деревьев!")
            return "skip_enemy"
        else:
            print("\nТы спотыкаешься — разбойник настигает тебя!")
            return "fight_enemy"
    else:
        return "fight_enemy"


def dragon_scene(player):
    print("\nТы добрался до логова дракона Смауга.")
    pause()
    print("Пещера наполнена жаром и запахом золота.")
    pause()
    print("Смауг медленно поднимает голову.\n")
    print("— Сме mortal, пришёл бросить мне вызов?.. — рычит он.\n")

    print("1 — вступить в бой")
    print("2 — попытаться поговорить")
    choice = input("Твой выбор: ")

    if choice == "2":
        print("\n— Великий Смауг, я ищу мудрости, а не смерти, — говоришь ты.")
        pause()
        success = randint(1, 10) <= player.luck // 2
        if success:
            print("Дракон улыбается. Его глаза вспыхивают интересом.")
            pause()
            print("— Ты первый смертный за века, кто осмелился говорить со мной.")
            pause()
            print("— Иди. Я дарую тебе жизнь и частицу знаний.\n")
            return "talk_ending"
        else:
            print("— Жалок, — рычит дракон и атакует!")
            return "fight_dragon"

    return "fight_dragon"


def endings(type_ending):
    print("\n===== КОНЕЦ =====\n")

    if type_ending == "victory":
        print("Ты победил дракона и вышел из пещеры с его сокровищами.")
        print("Люди будут петь о тебе легенды!")

    elif type_ending == "death":
        print("Твоя история окончена... но, возможно, потомки расскажут о твоём подвиге.")

    elif type_ending == "talk":
        print("Ты не стал сражаться. Ты выбрал мудрость.")
        print("Дракон отпустил тебя, а его слова изменили твою судьбу.")

    print("\nСпасибо за игру!")
    print("Хочешь — я могу расширить квест, добавить новых врагов или систему навыков!")


# ======= ЗАПУСК ИГРЫ =======

player = Person("Артур", "меч", 10, 10)
enemy = Person("Адольф", "сюрикен", 12, 6)
dragon = Person("Смауг", "огонь", 40, 20)

intro()

path = crossroad()

# 1 — башня
# 2 — болото
# 3 — лес

# Что будет с Адольфом?
result = None

if path == "1":
    result = tower_path(player)

elif path == "2":
    result = swamp_path(player)

elif path == "3":
    result = forest_path(player)

else:
    print("\nТы стоял слишком долго. Ночь опустилась, и ты вернулся домой.")
    exit()


# Встреча с Адольфом, если нужно
if result == "fight_enemy":
    survived = player.fight(enemy)
    if not survived:
        endings("death")
        exit()

# Выжили — идём к дракону
dragon_result = dragon_scene(player)

if dragon_result == "fight_dragon":
    survived = player.fight(dragon)
    if survived:
        endings("victory")
    else:
        endings("death")

elif dragon_result == "talk_ending":
    endings("talk")

