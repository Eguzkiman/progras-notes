def f():
	name = raw_input('Dime tu nombre...')
	print 'Hola ' + name
	f()

f()