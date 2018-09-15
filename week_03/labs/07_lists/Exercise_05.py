'''
Complete Exercise 10.3 (p.121) from the textbook.

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def middle(list):
    return list[1:-1]

print(middle(list))
