import random

def play ():
	n = random.randint(0, 0)
	user_input = int(raw_input('Guess my number! '))
	if n == user_input:
		print 'yay'
		return True
	else:
		print 'nein'
		return False

for i in range(0, 3):
	won = play()
	if won:
		print 'yay you won!'
		break
