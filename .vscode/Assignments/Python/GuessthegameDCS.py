from ast import Break
import random

GuessTheNumber= random.randint(0,9)


for x in range(0,10):
  UserGuess= int(input("Please enter your guess?"))
  if UserGuess == GuessTheNumber:
    print("Your Guess is correct!!")
    Break
    
