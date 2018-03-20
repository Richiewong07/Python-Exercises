from hero_rpg import *

def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)
    zombie = Zombie(5,5)

    choose_enemy = input('Who do you want to fight? (Goblin or Zombie): ')

    if choose_enemy == 'Goblin':
        while goblin.alive() and hero.alive():
            hero.print_status()
            goblin.print_status()
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                hero.attack(goblin)
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if goblin.alive():
                goblin.attack(hero)

    elif choose_enemy == 'Zombie':
        while zombie.alive() and hero.alive():
            hero.print_status()
            zombie.print_status()
            print()
            print("What do you want to do?")
            print("1. fight zombie")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                hero.attack_zero(zombie)
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if zombie.alive():
                zombie.attack(hero)


main()
