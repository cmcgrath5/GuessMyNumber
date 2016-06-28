#GuessMyNumber.py

from random import randint

randAnswer = (randint(1,10))

while True:
	try:
		guess = int (input ("Guess a number between 1-10: "))
		break
	except ValueError:
		print("Please enter a number value: ")

while (guess != randAnswer):
	if (guess == randAnswer):
		print ("You guessed correctly!")
	elif (guess < randAnswer):
		guess = int (input("Your guess was too low, guess again: "))
	elif (guess > randAnswer):
		guess = int (input("Your guess was too high, guess again: "))
	else:
		guess = int(input ("Sorry, guess again: "))
print ("CORRECT! Great guess!")
