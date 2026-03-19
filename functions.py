import random

def generate_damage(min, max):
    damage = random.randint(min, max)
    return damage

def show_state(name_hero, hp_hero, name_enemy, hp_enemy):
    hp = {
            name_hero: hp_hero,
            name_enemy: hp_enemy
    }

    return hp