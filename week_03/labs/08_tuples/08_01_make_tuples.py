'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''
user_input = input("Please input 10 numbers separated by commas:")
number_list = (user_input.split(","))
new_list = [float(i) for i in number_list]

def tuplify(input_list):
    tuple_list = []
    input_list.sort()
    for i in range(0, len(input_list), 2):
        list_slice = input_list[i:i+2]
        if len(list_slice) % 2 != 0:
            list_slice.append(0)
        tup = tuple(list_slice)
        tuple_list.append(tup)
    return tuple_list

# testing the function
print(tuplify(new_list))
