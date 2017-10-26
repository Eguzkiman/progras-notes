"""
Escribe un programa que defina las siguientes clases:

1) Player
	Properties: 
		Name: String
		Mass: Integer
		isDead: Boolean

	Methods:
		Eat: Consume a una Food o otro Player, y absorbe su masa
		Nota: Si te comes a otro usuario, su propiedad isDead debe ser True
		Nota: Si estás muerto, no puedes comer nada :(
		Nota: Solo puedes comer players con al menos 50 de masa menos que tú

2) Food
	Properties:
		Mass: Integer
		isDead: Boolean

Ejemplo:

Euki = Player('Eguzkiman', 20)
Diego = Player('Diego', 20)

food1 = Food(20)
food2 = Food(20)
food3 = Food(20)

Euki.eat(Diego)
=> necesitas más masa para comer a Diego
Euki.eat(food1)
=> omnomnomnom
Euki.eat(food2)
=> omnomnomnom
Euki.eat(food3)
=> omnomnomnom
Euki.eat(Diego)
=> Eguzki se comió a Diego!
=> Omnomnomnom

"""

class Player:
	def __init__ (self, name, mass):
		self.mass = int(mass)
		self.isDead = False

Euki = Player('Euki', 20)