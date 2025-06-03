from tkinter import *
from tkinter import ttk

import flashcards

# creating window and setup
root = Tk()
root.title("Simple Flashcards")
root.geometry("900x700")

# setting applicaiton theme
style = ttk.Style(root)
style.theme_use("vista")

# *** variables
index = 0
answer = StringVar(root)
accronym = StringVar(root)

# *** functions
def showAnswer():
	answer.set(flashcards.shuffledKeys[index])

def showNext():
	global index
	index += 1
	accronym.set(flashcards.originalCards[flashcards.shuffledKeys[index]])
	answer.set("")


# *** GUI elements

# show the accronym with a label
showAccronymLabel = Label(root, textvariable=accronym,
													font=("Arial", 24, "bold"), padx=225)
showAccronymLabel.grid(row=0, column=0)

accronym.set(flashcards.originalCards[flashcards.shuffledKeys[index]])

# show answer with label, starts hidden
showAnswerLabel = Label(root, textvariable=answer,
												font=("Arial", 16, "bold"))
showAnswerLabel.grid(row=1, column=0)

# button to show answer
showAnswerButton = Button(root, text="Show Answer", command=showAnswer)
showAnswerButton.grid(row=2, column=0)

# next button
nextButton = Button(root, text="Next", command=showNext)
nextButton.grid(row=3, column=0)

root.mainloop()