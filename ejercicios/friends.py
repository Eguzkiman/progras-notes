# -*- coding: utf-8 -*-
# La línea de arriba solo es para poder poner acentos, no es importante.

"""
Escribe un programa que defina las siguientes clases:

CLASE 1) User
	
	Propiedades:
		username: (string)
		friends: (Una lista de otros Users)
		friend_requests: (Una lista de friend requests)

	Métodos:
		send_friend_request (self, other_user)
			Este método debe crear una nueva friend_request, y añadirla a
			la lista de friend_requests del otro usuario.
			También debe imprimir lo siguiente:
				"<tu nombre de usuario> ha enviado una solicitud
				de amistad a <otro nombre de usuario>"
			Este método debe regresar la friend_request enviada

		accept_friend_request (self, friend_request)
			Este método debe añadir al usuario que envió a la solicitud a
			la lista de amigos y luego eliminar la friend_request de la lista
			de friend_requests.
			También debe imprimir lo siguiente:
				"<tu nombre de usuario> ha aceptado la solicitud
				de amistad de <otro nombre de usuario> :)"

		reject_friend_request (self, friend_request)
			Este método debe eliminar la friend_request de la lista de
			friend_requests.
			También debe imprimir lo siguiente:
				"<tu nombre de usuario> ha rechazado la solicitud
				de amistad de <otro nombre de usuario> :("

		print_status (self)
			Este método debe imprimir en consola la cantidad de amigos y solicitudes
			de amistad que tiene un usuario.

			Ejemplo:
			Eguzki tiene 2 amigos y 3 solicitudes de amistad.

CLASE 2) FriendRequest
	
	Propiedades:
		sender: (Usuario que envió la request)

PARA PROBAR SI ESTÁS BIEN:

Añade el siguiente código al final de tu programa:

sebas = User('Sebastián Sensual')
lau = User('Lau')
gabo = User('El Gabo')

request = sebas.send_friend_request(lau)
lau.accept_friend_request(request)

request = gabo.send_friend_request(lau)
lau.reject_friend_request(request)

Si tu programa funciona correctamente, debería imprimir en consola lo siguiente:

Sebastián Sensual ha envidado una solicitud de amistad a Lau
Lau tiene 0 amigos y 1 solicitudes de amistad.
Lau ha aceptado la solicitud de amistad de Sebastián Sensual :)
Lau tiene 1 amigos y 0 solicitudes de amistad.
El Gabo ha envidado una solicitud de amistad a Lau
Lau tiene 1 amigos y 1 solicitudes de amistad.
Lau ha rechazado la solicitud de amistad de El Gabo :(
Lau tiene 1 amigos y 0 solicitudes de amistad.

"""

class User:
	def __init__ (self, username):
		self.username = username
		self.friends = []
		self.friend_requests = []

	def send_friend_request (self, other_user):
		print self.username + ' ha envidado una solicitud de amistad a ' + other_user.username
		request = FriendRequest(self)
		other_user.friend_requests.append(request)
		return request

	def accept_friend_request (self, friend_request):
		print self.username + ' ha aceptado la solicitud de amistad de ' + friend_request.sender.username + ' :)'
		self.friends.append(friend_request.sender)
		self.friend_requests.remove(friend_request)

	def reject_friend_request (self, friend_request):
		print self.username + ' ha rechazado la solicitud de amistad de ' + friend_request.sender.username + ' :('
		self.friend_requests.remove(friend_request)
	
	def print_status (self):
		print self.username + ' tiene ' + str(len(self.friends)) + ' amigos y ' + str(len(self.friend_requests)) + ' solicitudes de amistad.'
		

class FriendRequest:
	def __init__ (self, sender):
		self.sender = sender

sebas = User('Sebastián Sensual')
lau = User('Lau')
gabo = User('El Gabo')


request = sebas.send_friend_request(lau)
lau.print_status()
lau.accept_friend_request(request)
lau.print_status()
request = gabo.send_friend_request(lau)
lau.print_status()
lau.reject_friend_request(request)
lau.print_status()

