#we called since ramdom to can use the library and use the funcions from library
import random

#this function let's us know the damage, we use 2 parameter and the always return in a number int
# we import from library the function radom.randint.
def generate_damage(min: int, max: int):
    damage = random.randint(min, max)

    if random.random() <= 0.10:
        print("CRITICAL HIT! Damage is doubled.")
        return damage * 2
    
    return damage


#This function show us the name and the hp of the players
def show_state(hp_hero: int, hp_enemy: int):
    print(f"Life hero: {hp_hero}")
    print(f"Life enemy: {hp_enemy}")

#this functions show the turn between player called heroe 
def turn_player(hp_hero: int, hp_enemy: int, potions: int):
    action = input("1. Attack\n2. Heal\n3. Special ability\nWhat do you want to do?: ").lower()

    if action == "attack" or action == "1":
        damage = generate_damage(10, 25)
        print(f"Damage caused: {damage}")
        input()
        
        hp_enemy -= damage
        attack_enemy = turn_enemy(hp_hero, hp_enemy)
        hp_hero -= attack_enemy
        print(f"The enemy has attacked: {attack_enemy}")
        input()

    elif action == "heal" or action == "2":
        if potions > 0:           
            potions -= 1
            hp_hero += 20
            print("You have healed: +20 life")
            print(f"stock's potions {potions}")

            attack_enemy = turn_enemy(hp_hero, hp_enemy)
            hp_hero -= attack_enemy
            print(f"The enemy has attacked: {attack_enemy}")
            input()

        else:
            print("You haven't stock")
    
    elif action == "special ability" or action == "3":
        if random.random() <= 0.50:
            damage = generate_damage(30, 50)
            hp_enemy -= damage
            print(f"SUCCESS! Special ability dealt {damage} damage.")

        else:
            print("FAILED! The special ability did nothing.")

    else:
        print("Invalid option. Try again.")

        return turn_player(hp_hero, hp_enemy, potions)

    return hp_hero, hp_enemy, potions

#this functions show the turn between player called monster
def turn_enemy(hp_hero, hp_enemy):
    print("\nENEMY'S TURN ")
  
    if hp_enemy < 24:
        hp_enemy += 15
        print("The Enemy is scared and heals +15 HP.")

    else:
        damage = generate_damage(15, 20) 
        hp_hero -= damage
        print(f"The Enemy attacks you for {damage} damage.")

    return hp_hero, hp_enemy

#this function  is to prove who's win
def verify_winner(hp_hero: int, hp_enemy: int):
    verify = True 

    if hp_hero <= 0:
        print("You lose!")
        verify = False

    elif hp_enemy <= 0:
        print("You win!")
        verify = False
    
    else:
        verify = True

    return verify