class Person:
	def __init__ (self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def say_hi (self, other):
		if self.age < other.age - 20:
			if other.gender == 'm':
				print 'Buenas tardes Mr. ' + other.name
			elif other.gender == 'f':
				print 'Buenas tardes Mrs. ' + other.name
		else:
			print 'Hola ' + other.name + '! Soy ' + self.name

rapp = Person('Javier', 3, 'm')
aris = Person('Aris', 160, 'f')
euki = Person('Euki', 120, 'm')
isma = Person('Ismael', 4, 'm')

rapp.say_hi(aris)
rapp.say_hi(euki)
rapp.say_hi(isma)