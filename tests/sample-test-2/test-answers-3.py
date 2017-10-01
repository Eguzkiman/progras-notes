word = raw_input('Dime una palabra: ')

current = ''
final = ''

for char in word:
	current += char
	final += current

print final