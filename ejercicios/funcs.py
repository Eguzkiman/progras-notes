import math

# 1)
def f (x, y, z):
	return x + y + z

y = f(1, 2, 3)

print y
# 2)
def square (x):
	return x * x

def sqrt (x):
	return math.sqrt(x)

def pythagoras (a, b):
	return sqrt(square(a) + square(b))

print square(5)


# 3)

"""
	1) Haz una funcion que reciba tres parámetros,
		y regrese la suma

	2) Haz las siguientes funciones:
		'square': Regresa el cuadrado de un número
		'sqrt': Calcula la raíz de un número
			(Tienes que googlear esto :v)
		'pythagoras': Recibe la longitud de dos catetos de un triángulo
			y regresa la hipotenusa 
			(usa las funciones square y sqrt que definiste antes)



	3) Haz el ejercicio anterior (que haga exactamente
		lo mismo), pero sin usar ciclos

		(HINT: Usa funciones) ((funciones recursivas))
"""