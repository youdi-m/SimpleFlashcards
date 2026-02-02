from tkinter import *
from tkinter import ttk

import flashcards

# creating window and setup
root = Tk()
root.title("Simple Flashcards")
root.geometry("500x600") # width x height
root.tk_setPalette(background='#282828', foreground='#ffffff')

# setting applicaiton theme
style = ttk.Style(root)
style.theme_use("vista")

index = 0
answer = StringVar(root)
accronym = StringVar(root)


# change answer text to match the answer
def showAnswer():
	answer.set(flashcards.shuffledKeys[index])
	showAnswerButton.pack_forget()
	rightButton.pack(side='top', anchor='center', pady=10)
	wrongButton.pack(side='top', anchor='center', pady=10)

# increment index, get next accronym and set answer text to nothing
def sortCard(attempt):
	global index

	if attempt == 'right':
		current_key = flashcards.shuffledKeys[index]
		flashcards.originalCards.pop(current_key)
		flashcards.shuffledKeys.pop(index)
	else:
		index += 1
	
	# Handle wrapping and empty deck
	if len(flashcards.originalCards) == 0:
		accronym.set("All done!")
		answer.set("")
		return
	
	if index >= len(flashcards.shuffledKeys):
		index = 0

	accronym.set(flashcards.originalCards[flashcards.shuffledKeys[index]])
	answer.set(" ")
	rightButton.pack_forget()
	wrongButton.pack_forget()
	showAnswerButton.pack(side='top', anchor='center', pady=10)

# *** GUI elements

# main frame to hold everything in place
topFrame = Frame(root, height=300, width=600)
topFrame.pack(expand=True)
topFrame.pack_propagate(False)

bottomFrame = Frame(root, height=200, width=600)
bottomFrame.pack(expand=True)
bottomFrame.pack_propagate(False)

# LABEL to show the accronym with a label
showAccronymLabel = Label(topFrame, textvariable=accronym,
													font=("Arial", 32, "bold"), wraplength=500)
showAccronymLabel.pack(side='top', anchor='center', pady=10)

accronym.set(flashcards.originalCards[flashcards.shuffledKeys[index]])

# LABEL to show answer with label, starts hidden
showAnswerLabel = Label(topFrame, textvariable=answer,
												font=("Arial", 24, "bold"), wraplength=500, pady=100)
showAnswerLabel.pack(side='top', anchor='center')

buttonFrame = Frame(root, )

# BUTTON to show answer
showAnswerButton = Button(bottomFrame, text="Show", command=showAnswer, width=13, font=("Arial", 10, "bold"))
showAnswerButton.pack(side='top', anchor='center', pady=10)

# BUTTONS for sorting

rightButton = Button(bottomFrame, text="Right", command=lambda: sortCard('right'), width=13, font=("Arial", 10, "bold"))
wrongButton = Button(bottomFrame, text="Wrong", command=lambda: sortCard('wrong'), width=13, font=("Arial", 10, "bold"))

# BUTTON to show next card
# nextButton = Button(bottomFrame, text="Next", command=showNext, width=13, font=("Arial", 10, "bold"))

root.mainloop()