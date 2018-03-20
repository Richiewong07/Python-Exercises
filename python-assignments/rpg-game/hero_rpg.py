class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        while self.health > 0:
            return True

class Hero(Character):

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")

    def attack_zero(self, enemy):
        enemy.health -= 0
        print("You done 0 damage to the zombie. Zombie cannot die!")

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))


class Goblin(Character):

    def attack(self, enemy):
        enemy.health -= self.power
        print("The Goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

    def print_status(self):
        print("The Goblin has {} health and {} power.".format(self.health, self.power))

class Zombie(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print("The Zombie does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

    def print_status(self):
        print("The Zombie has {} health and {} power.".format(self.health, self.power))
