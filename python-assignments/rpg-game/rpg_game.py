from hero_rpg import *


# hero = Hero('Hero', 10, 5, 0)
# goblin = Goblin('Goblin', 20 ,2, 5)
# zombie = Zombie('Zombie', 5 ,1, 100)
# medic = Medic('Medic', 10, 3, 6)
# shadow = Shadow('Shawdow', 1, 4, 4)

def main():


    hero = Hero('Hero', 10, 5, 0)
    goblin = Goblin('Goblin', 20 ,2, 5)
    zombie = Zombie('Zombie', 5 ,1, 100)
    medic = Medic('Medic', 10, 3, 6)
    shadow = Shadow('Shawdow', 1, 4, 4)

    print('WELCOME TO HERO RPG GAME.')
    print()

    choose_enemy = input('Who do you want to fight? (Goblin, Zombie, Medic, Shadow): ')

    if choose_enemy == 'Goblin':
        enemy = goblin
    elif choose_enemy == 'Zombie':
        enemy = zombie
    elif choose_enemy == 'Medic':
        enemy = medic
    elif choose_enemy == 'Shadow':
        enemy = shadow


    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("4. use item")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            if choose_enemy =='Goblin':
                hero.attack(enemy)
            elif choose_enemy == 'Zombie':
                hero.attack_zero(enemy)
            elif choose_enemy == 'Medic':
                hero.attack(enemy)
                enemy.recuperate()
            elif choose_enemy== 'Shadow':
                enemy.take_damage(hero)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            enemy.attack(hero)
        else:
            enemy.dead()
            hero.receive_coins(enemy)


    play_again = input('Do you want to play again? (Y or N): ')
    if play_again == 'Y':

        main()
    else:
        print('Thank you for playing!')




if __name__ == '__main__':
    main()
