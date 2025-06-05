import random

# original list of cards
originalCards = {}

# function to add the .txt file into originalCards and add to dict
def createCards(file):
	# opening file
	file = open(file, "r")

	# loop through text and add the accronyms and answers to the dict
	for line in file:
		key, ans = line.split(" ", 1)
		originalCards[ans] = key.strip()

# function to take the keys from the dict so we can shuffle them in a list
def shuffleCards(dict):

	shuffledCards = list(dict.keys())
	random.shuffle(shuffledCards)

	return shuffledCards

createCards("flashcards.txt")
shuffledKeys = shuffleCards(originalCards)