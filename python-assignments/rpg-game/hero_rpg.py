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
            print("The {} are dead.".format(enemy.name))

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("{} do {} damage to the {}.".format(self.name, self.power, enemy.name))
    #     if enemy.health <= 0:
    #         print("The {} is dead.".format(enemy.name))

    def attack_zero(self, enemy):
        enemy.health -= 0
        print("You done 0 damage to the {0}. {0} cannot die!".format(enemy.name))

    # def print_status(self):
    #     print("{} have {} health and {} power.".format(self.name, self.health, self.power))


class Goblin(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
    #     if enemy.health <= 0:
    #         print("{} are dead.".format(self.name))
    #
    # def print_status(self):
    #     print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Zombie(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("The {} does {} damage to the {}.".format(enemy.name, self.power, self.name))
    #     if enemy.health <= 0:
    #         print("{} are dead.".format(self.name))
    #
    # def print_status(self):
    #     print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
