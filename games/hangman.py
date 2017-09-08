import random

lives = 3
words = ['siwarrior', 'eguzkiller', 'ismalion', 'roborrego']

i = random.randint(0, 3)

word = words[i]

underscores = ['_' for char in word]
used_chars = []

print ' '.join(underscores)

while lives > 0:
	print 'Tienes ' + str(lives) + ' vidas'
	user_char = raw_input('Dime una letra :v ')

	if len(user_char) != 1:
		print 'Plz, pon solo un caracter...'

	elif user_char in used_chars:
		print 'Ya usaste esta letra :c'

	elif user_char in word:
		print 'yay'
		used_chars.append(user_char)
		underscores = [char if char in used_chars else '_' for char in word]

	else:
		print 'nope :c'
		lives -= 1
		used_chars.append(user_char)

	print ' '.join(underscores)

	if not '_' in underscores:
		break


if lives == 0:
	print 'perdiste #sad'
else:
	print 'yay ganaste xd'