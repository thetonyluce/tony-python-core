'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

Exercise 7
Write a function called has_duplicates that takes a list and returns
True if there is any element that appears more than once.
It should not modify the original list.'''

import random


def has_duplicates(t):
    sort = t[:]
    sort.sort()
    for i in range(len(sort) - 1):
        if sort[i] == sort[i + 1]:
            return True


def birthday_duplicates():
    birthdays = []
    count = 0
    i = 0
    while i < 1000:
        for items in range(23):
            birthdays.append(random.randint(1, 365))

        if has_duplicates(birthdays):
            count += 1
        i += 1
    return count / i * 100
