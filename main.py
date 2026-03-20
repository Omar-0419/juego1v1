import functions

name_hero = input("What is your name?: ")
hp_hero = 100
name_enemy = "Monster"
hp_enemy = 120
potions = 3

functions.show_state(hp_hero, hp_enemy)

while functions.verify_winner(hp_hero, hp_enemy):
    functions.turn_player(hp_hero, hp_enemy, potions)