username = raw_input("Username:")
password = raw_input("password:")

users = [
	{"username": "Eguzki", "password": "thisismypasswordxd"},
	{"username": "alexandra_alexander", "password": "pass123"}
]

for user in users:
	if user["username"] == username and user["password"] == password:
		print 'Bienvenido' + username + '!'