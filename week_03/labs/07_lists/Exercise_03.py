'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

'''


def nested_sum(t):
    sum = 0
    for each_list in t:
        for each_item in each_list:
            sum += each_item
    return(sum)


t = [[1, 2], [3], [4, 5, 6]]
sum = nested_sum(t)
print(sum)
