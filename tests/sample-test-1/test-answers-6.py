x1 = int(raw_input('x1: '))
y1 = int(raw_input('y1: '))
x2 = int(raw_input('x2: '))
y2 = int(raw_input('y2: '))
px = int(raw_input('px: '))
py = int(raw_input('py: '))

step_x = 1 if x2 > x1 else -1
step_y = 1 if y2 > y1 else -1

if px in range(x1, x2 + 1, step_x) and py in range(y1, y2 + 1, step_y):
	if px == x1 or px == x2 or py == y1 or py == y2:
		print 'in border'
	else:
		print 'inside'
else:
	print 'outside'