import random


class Fighter:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.alive = True

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 1:
            damage = 1

        print(f"{self.name} attacks {enemy.name}")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} has died")
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.alive

    def show_stats(self):
        print(
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Attack: {self.attack}, "
            f"Defense: {self.defense}, "
            f"Alive: {self.alive}"
        )

class BattleArena:
    def __init__(self):
        self.fighters = []

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def get_alive_fighters(self):
        return [fighter for fighter in self.fighters if fighter.is_alive()]

    def start_battle(self):
        print("Battle started!\n")

        while len(self.get_alive_fighters()) > 1:
            alive_fighters = self.get_alive_fighters()

            fighter1, fighter2 = random.sample(alive_fighters, 2)

            fighter1.attack_enemy(fighter2)

            if fighter2.is_alive():
                fighter2.attack_enemy(fighter1)

            print("\nCurrent fighters state:")
            for fighter in self.fighters:
                fighter.show_stats()
            print("-" * 40)

    def show_winner(self):
        alive = self.get_alive_fighters()
        if alive:
            winner = alive[0]
            print(f"\nWinner: {winner.name}")
            print(f"Congratulations {winner.name} on your victory, tiger gurl hoho!")
        else:
            print("No winner")

fighter1 = Fighter("Aruka", 45, 14, 6)
fighter2 = Fighter("Molya", 40, 18, 5)
fighter3 = Fighter("Raikhanka", 38, 17, 6)
fighter4 = Fighter("Asylaika", 40, 16, 5)

arena = BattleArena()
arena.add_fighter(fighter1)
arena.add_fighter(fighter2)
arena.add_fighter(fighter3)
arena.add_fighter(fighter4)

arena.start_battle()
arena.show_winner()