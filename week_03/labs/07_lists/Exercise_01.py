'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

user_input = input("Please input 10 numbers separated by commas:")
number_list = (user_input.split(","))
new_list = [float(i) for i in number_list]

sum_list = sum(new_list)
list_average = sum(new_list) / len(new_list)
print (sum_list)
print(list_average)
