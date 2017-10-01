import random

signs = [
	"Aries",
	"Leo",
	"Sagitario",
	"Tauro",
	"Virgo",
	"Capricornio",
	"Geminis",
	"Libra",
	"Acuario",
	"Cancer",
	"Escorpio",
	"Piscis",
]

def make_compat (signs):
	compats = {}
	for sign in signs:
		compats[sign] = random.randint(0, 10)  
	return compats

comps = {}
for sign in signs:
	comps[sign] = make_compat(signs)

print comps

