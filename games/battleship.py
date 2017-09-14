import random

total_ships = 4

board = [['_' for x in range(0, 3)] for x in range(0, 3)]
known_board = [['_' for x in range(0, 3)] for x in range(0, 3)]

def print_board(board):
	for row in board:
		print ' '.join(row)

def add_ship (board):
	x = random.randint(0, 2)
	y = random.randint(0, 2)
	if board[x][y] == 'o':
		add_ship(board)
	else:
		board[x][y] = 'o'

add_ship(board)
add_ship(board)
add_ship(board)
add_ship(board)

print_board(board)
print_board(known_board)

while total_ships > 0:
	x = int(raw_input('Dame tu coordenada en x'))
	y = int(raw_input('Dame tu coordenada en y'))

	if board[x][y] == 'o':
		print 'Boom!'
		total_ships -= 1
		board[x][y] = '_'
		known_board[x][y] = 'o'
	else:
		print 'Nope'
		known_board[x][y] = 'x'

	print_board(known_board)

print 'yay ganaste xd'