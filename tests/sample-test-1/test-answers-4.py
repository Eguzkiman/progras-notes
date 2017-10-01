text = raw_input('Dime tu texto: ')
longest_word_length = 0
words = text.split()

for word in words:
	length = len(word)
	if length > longest_word_length:
		longest_word_length = length


print ''.join(['*' for char in range(0, longest_word_length + 4)])

for word in words:
	print '* ' + word + ''.join([' ' for char in range(0, longest_word_length - len(word))]) + ' *'

print ''.join(['*' for char in range(0, longest_word_length + 4)])