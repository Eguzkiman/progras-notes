"""
Escribe un programa que defina las siguientes clases:

1) Card
Properties:
	value (integer from 1, 13)
	suit ('hearts', 'diamonds', 'spades', 'clubs')

2) Deck
Properties:
	cards (list of cards)

Methods:
	shuffle (shuffles the cards)

	 make_hand (returns a new hand with five cards)


Ejemplo:

my_deck = Deck()
Deck.shuffle()

for card in my_deck.cards:
	print card.value + card.suit

 3) Hand

Properties:
	cards: (list of cards)	

Methods:
	Shuffle (shuffles the cards)

	has_poker (returns true if has poker...)

"""

import random

class Card:
	def __init__ (self, value, suit):
		self.value = value
		self.suit = suit

class Deck:
	def __init__ (self):
		cards = []
		suits = ['hearts', 'diamonds', 'clubs', 'spades']

		for suit in suits:
			for value in range(1, 14):
				card = Card(value, suit)
				cards.append(card)

		self.cards = cards

	def shuffle (self):
		random.shuffle(self.cards)

	def make_hand (self):
		cards = []
		for i in range(0, 5):
			card = self.cards.pop()
			cards.append(card)
		return Hand(cards)

class Hand:
	def __init__ (self, cards):
		self.cards = cards

my_deck = Deck()

my_hand = my_deck.make_hand()

print len(my_hand.cards)



