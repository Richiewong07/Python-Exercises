from random import *

class Character():
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

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

    def dead(self):
        print("You received {} coins for defeating {}!".format(self.bounty, self.name))

class Hero(Character):

    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

    def attack(self, enemy):
        # DOUBLE DAMAGE ADDED TO HERO
        prob = randint(1,10)
        if prob == 2:
            self.power *= 2
            print('DOUBLE DAMAGE ACTIATED FOR THE HERO! POWER INCREASE FROM 5 TO 10')

        enemy.health -= self.power
        print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))

        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))


    def attack_zero(self, enemy):
        enemy.health -= 0
        print("{0} done 0 damage to the {1}. {1} cannot die!".format(self.name, enemy.name))



class Goblin(Character):

    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)


class Zombie(Character):

    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

class Medic(Character):

    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

    def recuperate(self):
        prob = randint(1,10)
        if prob <= 2:
            self.health += 2
            print('{} recuperate 2 health points!'.format(self.name))


class Shadow(Character):

    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

    def take_damage(self, enemy):
        prob = randint(1,10)
        if prob >= 9:
            self.health -= enemy.power
            print("The {} does {} damage to the {}.".format(enemy.name, enemy.power, shadow.name))

            if shadow.health <= 0:
                print("The {} is dead.".format(shawdow.name))

        else:
            print('{} did NO DAMAGE to the {}'.format(enemy.name, self.name))
