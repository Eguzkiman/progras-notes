import random
plays = ['piedra', 'papel', 'lagarto', 'spock', 'tijera']
wins = {
	'piedra': 	['lagarto', 'tijera'],
	'tijera': 	['lagarto', 'papel'],
	'papel': 	['piedra', 'spock'],
	'lagarto': 	['papel', 'spock'],
	'spock': 	['piedra', 'tijera']
}

def play ():
	i = random.randint(0, 4)
	computer_play = plays[i]
	player_play = raw_input('Piedra, papel, tijera, lagarto, spock? ');
	print 'I played ' + computer_play
	if player_play == computer_play:
		print 'Empate lol'
	elif player_play in wins[computer_play]:
		print 'perdiste :c'
	else:
		print 'ganaste :v'
	play()

play()