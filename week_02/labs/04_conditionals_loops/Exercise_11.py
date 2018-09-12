'''
Apply a Cesar cipher of 7 to the 'secret' variable.

p.s.: http://www.montypython.net/scripts/dentist.php

'''
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

abc = list('abcdefghijklmnopqrstuvwxyz')
encrypted = ""

for char in secret:  # for every charater in secret message
    if char.lower(secret) in abc:  # if it's a lowercase letter from the abc list
        for i, j in enumerate(abc):  # enumerate characters in abs - e.g. 1 a, 2 b, etc
            if j == char.lower():  # if there's a lower case letter
                new_char = abc[(i + cipher) % len(abc)]  # create a new_char from abc list that has a value of 7 positions different than the original character.
    else:
        encrypted += char

print(encrypted)
