'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
user_num_one = int(input("Give me a lil' whole number: "))
user_num_two = int(input("Give me a big ol' whole number: "))

for i in range(user_num_one, user_num_two):
    print(i**2)
