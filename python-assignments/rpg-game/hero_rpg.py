from random import *

class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        while self.health > 0:
            return True

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def attack(self, enemy):
        # DOUBLE DAMAGE ADDED TO HERO
        probability = randint(1,10)
        if probability == 2:
            self.power *= 2
            print('DOUBLE DAMAGE ACTIATED FOR THE HERO! POWER INCREASE FROM 5 TO 10')
        enemy.health -= self.power
        print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))


    def attack_zero(self, enemy):
        enemy.health -= 0
        print("{} done 0 damage to the {0}. {0} cannot die!".format(self.name, enemy.name))



class Goblin(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)


class Zombie(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Medic(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def recuperate(self):
        probability randint(1,10)
        if probability == 2:
            self.health += 2
            print('{} recuperate 2 health points!'.format(self.name))
