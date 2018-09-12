'''
Complete Exercise 3.2 (p.27) from the textbook.

'''

user_name = input("Give me your name kid. Probably doesn't print correctly: ")


def right_justify(name):
    position = 70 - len(name)
    return position


print (right_justify(user_name) * " ", user_name)

import random
random.choice
