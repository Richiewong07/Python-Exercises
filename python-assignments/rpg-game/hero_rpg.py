
class Hero():
    def __init__(self, hero_health, hero_power):
        self.hero_health = hero_health
        self.hero_power = hero_power

    def attack (self):
        goblin_health = 6
        goblin_power = 2

        goblin_health -= self.hero_power
        print("You do {} damage to the goblin.".format(self.hero_power))

        if goblin_health <= 0:
            print("The goblin is dead.")

class Goblin():
    def __init__(self, goblin_health, goblin_power):
        self.goblin_health = goblin_health
        self.goblin_power = goblin_power


hero = Hero(10, 5)
goblin = Goblin(6, 2)

hero.attack()
