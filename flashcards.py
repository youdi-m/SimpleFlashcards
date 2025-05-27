import random

# original list of cards
originalCards = {}

# secondary list of cards based on how well the user did 
horribleScore = {}
badScore = {}
goodScore = {}
greatScore = {}
amazingScore = {}

# function to add the .txt file into originalCards and add to dict
def createCards(file):
	# opening file
	file = open(file, "r")

	# loop through text and add the accronyms and answers as hashmaps
	for line in file:
		key, ans = line.split(" ", 1)
		originalCards[key] = key.strip()

# show every card once while sorting them
def showCards(dict):

	# create an iterable list to assign first dict keys to
	# second key is still in original dict, we then shuffle the list
	cards = list(originalCards.keys())
	random.shuffle(cards)

	# TODO: break this into its own function
	for card in cards:
		# show accronym
		print(card)

		print(originalCards[card])

createCards("flashcards.txt")
showCards(originalCards)