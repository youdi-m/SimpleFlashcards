import random

# original list of cards
originalCards = {}

#sorting list based on how well the user did
# not implemented yet
horribleScore = {}
badScore = {}
goodScore = {}
greatScore = {}
amazingScore = {}

# function to add the .txt file into originalCards and add to dict
def createCards(file):
	# opening file
	file = open(file, "r")

	# loop through text and add the accronyms and answers to the dict
	for line in file:
		key, ans = line.split(" ", 1)
		originalCards[ans] = key.strip()

# taking the keys from the dict so we can shuffle them in a list
def shuffleCards(dict):

	shuffledCards = list(dict.keys())
	random.shuffle(shuffledCards)

	return shuffledCards

createCards("flashcards.txt")
shuffledKeys = shuffleCards(originalCards)