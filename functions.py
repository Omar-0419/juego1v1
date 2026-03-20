import random

def generate_damage(min, max):
    damage = random.randint(min, max)
    return damage

def show_state(name_hero, hp_hero, name_enemy, hp_enemy):
    hp = {
            name_hero: hp_hero,
            name_enemy: hp_enemy
    }

    print() ############# falta

    return hp

def turn_player():
    action = input("1. Attack\n2. Heal\n3. Special ability\nWhat do you want to do?: ").lower()

    if action == "attack" or action == "1":
        damage = random.randint(10, 25)
        print(f"Damage caused: {damage}")
    
    elif action == "heal" or action == "2":
        print("You have healed: +20 life")
    
    elif action == "special ability" or action == "3":
        probability = random.randint(0, 1)

        if probability == 0:
            great_damage = random.randint(30, 50)
            print("The special ability was successfully executed!")
            print(f"Damage caused by the great damage: {great_damage}")
        
        else:
            print("The special ability failed")
    
    else:
        print("Invalid option")

def turn_enemy():
    attack = random.randint(15, 20)
    return attack

def verify_winner(hp_hero, hp_enemy):
    verify = True ########################### en duda

    if hp_hero == 0:
        print("You win!")
        verify = False

    elif hp_enemy == 0:
        print("You lose.")
        verify = False
    
    else:
        verify = True

    return verify