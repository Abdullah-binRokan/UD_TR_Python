import random

def flip_coin():
    return random.choice(['heads', 'tails'])

def die_roll():
    return random.randint(1, 6)

print("flip coin:", flip_coin())

print("die roll:", die_roll())
