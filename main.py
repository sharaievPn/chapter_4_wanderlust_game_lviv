"""Wanderlust game

Imports back-end classes from game.py
Player gets in different streets of Lviv.
On each street player finds weapon or treat and meets
enemy or friend. Player can treat friends and fight with enemies.
If player uses incorrect weapon against particular enemy, game is lost.
If player treats friend with the correct item, friend gives a hint on how
to defeat particular enemy.
The game ends when all enemies are defeated and player made a trip from
Kozelnytska to Krakivska and back.

https://github.com/sharaievPn/chapter_4_wanderlust_game_lviv
"""

import game
from random import shuffle


def play():
    # initialize streets
    kozelnytska = game.Street('Kozelnytska str')
    kozelnytska.set_description('Kozelnytska str')

    stryiska = game.Street('Stryiska str')
    stryiska.set_description('Stryiska str')

    franka = game.Street('Franko str')
    franka.set_description("Franka str")

    shevchenka = game.Street('Shewchenko str')
    shevchenka.set_description("Shewchenko str")

    krakivska = game.Street('Krakiwska str')
    krakivska.set_description("Krakiwska str")

    bandery = game.Street('Bandera str')
    bandery.set_description('Bandera str')

    streets = [kozelnytska,
               stryiska,
               franka,
               krakivska,
               shevchenka,
               bandery]

    winning_condition = dict()
    for street in streets:
        winning_condition.update({street: 0})
    winning_condition[kozelnytska] = 1
    # streets initialized

    # link streets
    kozelnytska.link_street(stryiska, 'west')
    kozelnytska.link_street(franka, 'north')

    stryiska.link_street(kozelnytska, 'east')
    stryiska.link_street(franka, 'south')

    franka.link_street(kozelnytska, 'south')
    franka.link_street(stryiska, 'north')
    franka.link_street(shevchenka, 'west')
    franka.link_street(krakivska, 'east')

    shevchenka.link_street(franka, 'east')
    shevchenka.link_street(krakivska, 'north')
    shevchenka.link_street(bandery, 'west')

    krakivska.link_street(shevchenka, 'south')
    krakivska.link_street(kozelnytska, 'west')

    bandery.link_street(shevchenka, 'east')
    # linked streets

    # initialize persons
    kavaler = game.Friend('Kavaler', 'A man entertaining a woman')
    kavaler.set_description('Young, rich, handsome')

    lotr = game.Enemy('Lotr', 'Scoundrel, robber, plunderer')
    lotr.set_description('Cheap clothes and a sly smile')

    zbui = game.Enemy('Zbui', 'Robber, burglar')
    zbui.set_description('Yesterday was a lotr')

    batar = game.Enemy('Batar', "A brawler, a drunkard, a brutal man popular with women")
    batar.set_description('Galba is always with him')

    laidak = game.Friend('Laidak', 'A poor homeless person')
    laidak.set_description('Tattered clothes and an outstretched hand')

    student = game.Friend('Student', 'A creature that feeds on ultraviolet light')
    student.set_description('Somewhat similar to a laidback man, wearing a cloak')

    persons = [lotr,
               zbui,
               batar,
               kavaler,
               student,
               laidak]

    enemies = [lotr,
               zbui,
               batar]
    enemies_to_hint = [lotr,
                       zbui,
                       batar]
    # persons initialized

    # initialize items
    shokolad = game.Treat('chocolate')
    shokolad.set_description('qualifying')
    kavaler.set_treat('chocolate')

    food = game.Treat('food')
    food.set_description('fresh')
    student.set_treat('food')

    money = game.Treat('money')
    money.set_description('coins')
    laidak.set_treat('money')

    knife = game.Weapon('knife')
    knife.set_description('sharp')

    gun = game.Weapon('gun')
    gun.set_description('loaded')

    electric_shoker = game.Weapon('pepper spray')
    electric_shoker.set_description('ultra spicy')

    weapons = [knife,
               gun,
               electric_shoker]

    all_items = [shokolad,
                 food,
                 money,
                 knife,
                 gun,
                 electric_shoker]

    treats = [shokolad,
              food,
              money]

    # items initialized

    # link weaknesses
    shuffle(weapons)
    for i in range(3):
        persons[i].set_weakness(weapons[i].name)
    # weaknesses linked

    # place persons
    shuffle(streets)
    shuffle(persons)
    shuffle(all_items)
    for i in range(6):
        streets[i].set_character(persons[i])
        streets[i].set_item(all_items[i])
    # persons placed

    current_street = kozelnytska
    backpack = []

    dead = False
    counter = 0
    flag = False

    while dead is False:
        if counter != 0:
            print("\n")

        counter += 1
        current_street.get_details()

        inhabitant = current_street.get_person()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_street.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            # Move in the given direction
            try:
                current_street = current_street.move(command)
            except KeyError:
                continue

        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_street.set_item(None)
            else:
                print("There's nothing here to take!")

        elif command == "fight":
            if inhabitant is not None:
                if inhabitant.weakness is not None:
                    # Fight with the inhabitant, if there is one
                    print("What will you fight with?")
                    fight_with = input()

                    correct = False
                    for weapon in weapons:
                        if weapon.name == fight_with:
                            correct = True

                    if not correct:
                        print(f"You can't fight with {fight_with}")
                        continue

                    # Do I have this item?
                    if fight_with in backpack:

                        if inhabitant.fight(fight_with) is True:
                            # What happens if you win?
                            print("Hooray, you won the fight!")
                            current_street.character = None
                            enemies.remove(inhabitant)
                        else:
                            # What happens if you lose?
                            print("Oh dear, you lost the fight.")
                            print("That's the end of the game")
                            dead = True
                    else:
                        if fight_with[0] in 'aeiou':
                            print("You don't have an " + fight_with)
                        else:
                            print("You don't have a " + fight_with)
                else:
                    print("You can't fight with friend!")
            else:
                print("There is no one to fight with here!")

        elif command == 'treat':
            if inhabitant is not None:
                if inhabitant.treat is not None:
                    # Treat the person, if there is one
                    print("What will you treat with?")
                    treat_with = input()

                    correct = False
                    for treat in treats:
                        if treat.name == treat_with:
                            correct = True

                    if not correct:
                        print(f"You can't treat with {treat_with}")
                        continue

                    # Do I have this item?
                    if treat_with in backpack:

                        if inhabitant.make_treatment(treat_with):
                            # What happens if you treated correctly?
                            if len(enemies) > 0:
                                print("Hooray, here is your hint!")
                                if enemies[0] in enemies_to_hint:
                                    enemies_to_hint.remove(enemies[0])
                                    print(f'To defeat {enemies[0].name} '
                                          f'you need {enemies[0].weakness}')
                                    current_street.character = None
                                else:
                                    print(f'To defeat {enemies_to_hint[0].name} '
                                          f'you need {enemies_to_hint[0].weakness}')
                                    enemies_to_hint = enemies_to_hint[1:]
                                    current_street.character = None
                            else:
                                print("Your friend is happy now!")
                                current_street.character = None
                        else:
                            # What happens if you lose?
                            print("Your friend doesn't need that")
                            continue
                    else:
                        if treat_with[0] in 'aeiou':
                            print("You don't have an " + treat_with)
                        else:
                            print("You don't have a " + treat_with)
                else:
                    print("You can't treat enemy!")
            else:
                print("There is no one to treat here!")

        else:
            print("I don't know how to " + command)

        winning_condition[current_street] += 1
        if current_street == krakivska:
            flag = True
            winning_condition[kozelnytska] = 1

        if not flag:
            continue

        if len(enemies) > 0:
            continue

        for visit in list(winning_condition.values()):
            if visit < 1:
                break

        if winning_condition[kozelnytska] < 2:
            continue
        else:
            print('Hooray, you won the game!')
            return None


play()
