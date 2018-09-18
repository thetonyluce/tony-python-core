'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''

 # This is a guess the number game.
#import random module
import random

#guesscounter (user gets 10 tries)
guessesTaken = 0

#startgame
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
print('Hola ' + myName + ', I am thinking of a number between 1 and 20.'

#ask user for guess (repeat u)
while guessesTaken < 10:
print('Try and guess my number, feeble human') # There are four spaces in front of print.
guess = input()
guess = int(guess)
guessesTaken = guessesTaken + 1

    #guesses too low
    if guess < number:
    print('Your guess is too low.') # There are eight spaces in front of print.

    #guesses too high
    if guess > number:\
    print('Your guess is too high.')

    #guesses just right
    if guess == number:
    break

    if guess == number:
    guessesTaken = str(guessesTaken)

    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
    number = str(number)

    print('Loser'. The number I was thinking of was ' + number)
