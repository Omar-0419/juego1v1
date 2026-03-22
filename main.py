import functions

name_hero = input("What is your name?: ")
hp_hero = 100
name_enemy = "Monster"
hp_enemy = 120
potions = 3

while functions.verify_winner(hp_hero, hp_enemy):
    hp_hero, hp_enemy, potions = functions.turn_player(hp_hero, hp_enemy, potions)
    functions.show_state(hp_hero = max(0, hp_hero), hp_enemy = max(0, hp_enemy))