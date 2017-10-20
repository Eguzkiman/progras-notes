# -*- coding: utf-8 -*-
# La línea de arriba solo es para poder poner acentos, no es importante.
"""
Programación Orientada a Objetos (POO)

Toda la progra que hemos visto hasta ahora se ha concentrado en escribir 'acciones'
para manipular 'datos'. En orientado a objetos, en cambio, se trata de definir
qué forma tienen esos 'datos'.

A esos datos les llamamos objetos, y a todos los datos que tienen características
similares les llamamos clases.

Por ejemplo, imagina que estás escribiendo el software de un cajero automático, y
necesitas saber si el pin que el usuario introdujo es el correcto.

Para saberlo, necesitas tener una lista con los números y pines de cada tarjeta
bancaria. Como todas las tarjetas bancarias son objetos con características similares
(tienen número de tarjeta y pin), podemos crear una clase para definirlas:
"""

class Tarjeta:
	# Haremos algo aquí en un momento

"""
Las clases se definen con la palabra class, seguida del nombre de la clase, con
mayúscula.

Las clases pueden contener dos cosas: propiedades y métodos:

Las propiedades son variables que tienen todos los objetos de la misma clase. Las
propiedades de una tarjeta bancaria, por ejemplo, serían número de tarjeta y pin.

Los métodos son acciones que se pueden realizar sobre un objeto. Una método de
una tarjeta bancaria, por ejemplo, podría determinar si el pin introducido es
correcto o no.

Existe un método especial en todas las clases: el método __init__. (Nota que es con
doble guión bajo).

__init__ es el método constructor de una clase. Recibe los parámetros necesarios para
crear un nuevo objeto de esa clase. Se usa así:
"""

class Tarjeta:
	def __init__ (self, num, pin):
		self.num = num
		self.pin = pin

"""
Vamos por partes:

Primero, todos los métodos de una clase se definen igual que una función en python,
con la palabra def, seguida del nombre de la función, seguido de paréntesis, con el
nombre de los parámetros que recibe el método, separados por coma.

Segundo, todos los métodos de una clase tienen 'self' como primer parámetro. Siempre.
Self es una referencia al objeto actual, con él puedes accesar a las propiedades y
métodos del mismo objeto.

Tercero, __init__ debe usarse para definir las propiedades del objeto (self).
Por ejemplo, el método __init__ de la clase Tarjeta recibe el número de tarjeta y
el pin, y los asigna como propiedades de self.

Con la clase Tarjeta ya definida, podemos empezar a crear tarjetas bancarias.
Se hace así:
"""

mi_tarjeta = Tarjeta(178319390182, 1337)

print mi_tarjeta.num
# => 178319390182
print mi_tarjeta.pin
#  => 1337

"""
Para crar un objeto de una clase, se usa el nombre de la clase, paréntesis, y los
parámetros de __init__ separados por coma, en este caso, num, y pin.

El parámetro self no es necesario para crear objetos de una clase, solo necesitas
escribir los parámetros que no son self.

Para accesar al valor de una propiedad de un objeto, se usa el nombre del objeto
(nota que es el nombre que le diste al objeto, no el nombre de la clase) más . (punto)
más el nombre de la propiedad. Ejemplo: mi_tarjeta.num. A esta forma de accesar a propiedades de un objeto se
le llama 'Sintaxis de punto'. 

Habíamos dicho que podíamos usar un método para checar si un pin es correcto para una
tarjeta. Podemos hacerlo así:
"""

class Tarjeta:
	def __init__ (self, num, pin):
		self.num = num
		self.pin = pin

	def check_pin (self, attempted_pin):
		return self.pin == attempted_pin

"""
De nuevo, vamos por pasos:

Primero, definimos el método check_pin, que recibe el parámetro attempted_pin
(recuerda que todos los métodos siempre reciben self como primer parámetro)

Segundo, lo que queremos es comparar si el pin que escribió el usuario (attempted_pin)
es el mismo pin de la tarjeta (self.pin). Usamos el operador '==' para comparar si
son iguales.

Por último, podemos usar los métodos de un objeto con la misma sintaxis de punto que
usamos para accesar a sus propiedades:
"""

mi_tarjeta = Tarjeta(178319390182, 1337)
user_input = raw_input('Escribe tu pin: ')

if mi_tarjeta.check_pin(user_input):
	print 'Acceso permitido'
else:
	print 'Pin incorrecto. Acceso denegado.'


"""
Listo holisto. Así es como se usan los conceptos básicos de progra orientada
a objetos c:
"""













