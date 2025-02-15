import time
from random import randint

class Character:
    def __init__(self, name, weapon, damage, health):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.health = health
        self.alive = True
        
    def about(self):
        # Introduce the character with a short delay
        print(f"\n{self.name} — мастер боевых искусств. Его оружие — {self.weapon}.")
        time.sleep(1)
        print(f"Здоровье: {self.health} HP.\n")
        time.sleep(1)

    def punch(self, opponent):
        # Simulate attack with random result
        print(f"\n{self.name} наносит удар с {self.weapon} по {opponent.name}.")
        time.sleep(1)
        strike_type = randint(1, 3)

        if strike_type == 1:
            opponent.health -= self.damage
            print(f"Наносит урон! У противника {opponent.name} теперь {opponent.health} HP.")
        elif strike_type == 2:
            opponent.health -= self.damage * 2
            print(f"Критический удар! У противника {opponent.name} теперь {opponent.health} HP.")
        elif strike_type == 3:
            print(f"Промах! {self.name} не попал в {opponent.name}.")
        
        time.sleep(1)
    
    def is_alive(self):
        return self.health > 0

    def fight(self, opponent):
        print("\nБитва начинается!\n")
        time.sleep(1)
        
        while self.is_alive() and opponent.is_alive():
            # Random turn for either player or opponent to strike
            turn = randint(1, 2)
            if turn == 1:
                self.punch(opponent)
            else:
                opponent.punch(self)
            
            time.sleep(1)

        # Outcome of the battle
        if self.is_alive():
            print(f"\n{self.name} одерживает победу в этой жестокой битве!\n")
        else:
            print(f"\n{self.name} пал в бою... Но его имя будет жить в легендах.\n")
        

# Creating characters
hero = Character(name='Мачо-Абу', weapon='Рука', damage=20, health=100)
villain = Character(name='Адольф', weapon='Сирюкен', damage=20, health=100)

# Introduce characters
hero.about()
villain.about()

# Start the fight
hero.fight(villain)
