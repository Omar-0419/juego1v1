#we called since ramdom to can use the library and use the funcions from library
import random

#this function let's us know the damage, we use 2 parameter and the always return in a number int
# we import from library the function radom.randint.
def generate_damage(min: int, max: int):
    damage = random.randint(min, max)
    return damage


#This function show us the name and the hp of the players
def show_state(hp_hero, hp_enemy):

    print(f"Life hero: {hp_hero}")
    print(f"Life enemy: {hp_enemy}")

#this functions show the turn between player called heroe 
def turn_player(hp_hero, hp_enemy, potions):
    action = input("1. Attack\n2. Heal\n3. Special ability\nWhat do you want to do?: ").lower()

    if action == "attack" or action == "1":
        damage = generate_damage(10, 25)
        print(f"Damage caused: {damage}")
        hp_enemy -= damage
        hp_hero -= turn_enemy()
        print(f"The enemy has attacked: {turn_enemy()}")

    elif action == "heal" or action == "2":
        if potions > 0:           
            potions -= 1
            hp_hero += 20
            print("You have healed: +20 life")
            print(f"stock's potions {potions}")
        else:
            print("You haven't stock")
    
    elif action == "special ability" or action == "3":
        probability = random.randint(0, 1)

        if probability == 1:
            great_damage = random.randint(30, 50)
            print("The special ability was successfully executed!")
            print(f"Damage caused by the great damage: {great_damage}")
        
        else:
            print("The special ability failed")
    
    else:
        print("Invalid option")
    
    show_state(hp_hero,hp_enemy)
    
    return hp_hero, hp_enemy, potions

#this functions show the turn between player called monster
def turn_enemy():
    attack = random.randint(15, 20)
    return attack

#this function  is to prove who's win
def verify_winner(hp_hero, hp_enemy):
    verify = True 

    if hp_hero == 0:
        print("You win!")
        verify = False

    elif hp_enemy == 0:
        print("You lose.")
        verify = False
    
    else:
        verify = True

    return verify