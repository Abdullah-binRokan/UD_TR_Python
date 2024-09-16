# import random    # NameError for not importing random Lib

def coin_flip():
	return random.choice(['heads', 'tails'])

print("flip coin, you are the heads.\n")

if coin_flip() == 'heads':
	print('Heads - You win!')
else:
	print('Tails - You lose!')


