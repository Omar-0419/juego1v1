import functions


print(functions.generate_damage(10, 50))

name_hero = "Omar"
hp_hero = 100
name_enemy = "Mounstro"
hp_enemy = 120

print(functions.show_state(name_hero, hp_hero, name_enemy, hp_enemy))

functions.turn_player()

print("Damage caused by enemy: ",functions.turn_enemy())

print(functions.verify_winner(20, 0))