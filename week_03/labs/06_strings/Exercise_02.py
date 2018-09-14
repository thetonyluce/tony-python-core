'''
A string slice can take a third index that specifies the “step size”; that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.

Use this idiom to write a one-line version of is_palindrome from Exercise 3.
'''

possible_palindrome = input('Welcome to the palindrome test. Enter a possible palindrome to continue:')


if possible_palindrome[::1] == possible_palindrome[::-1]:

    print ("Well done. You've found a palindrome. Are you the palindrome fairy?")

else:

    print ("This is not the palindrome you are looking for.")
