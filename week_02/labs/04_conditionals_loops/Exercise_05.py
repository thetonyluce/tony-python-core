'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
    of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
    Print the results to the console.

    For example, if a user enters 1 and 100, the output should be:
        The sum is: 5050
        The average is: 50.5
'''

user_number1 = int(input("Tell me a low number:"))
user_number2 = int(input("Now tell me a higher number:"))

sum = 0
tally = 0
for i in range(user_number1, user_number2 + 1):
    sum += i
    tally = + 1

number_average = (sum / tally)

print("The total is: ", sum)
print("The average is:", number_average)
