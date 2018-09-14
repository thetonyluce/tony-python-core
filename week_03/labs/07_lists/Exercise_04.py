'''
Complete Exercise 10.2 (p.120) from the textbook.

'''

t = [1, 2, 3]


def cumsum(t):
    _sum = 0
    cumsum_dumpster = []

    for target_value in t:

        # get value from list before value x
        index_position = t.index(target_value)
        slice_result = t[0:index_position + 1]

        # sum values
        number_result = sum(slice_result)

        # add sum to new list
        cumsum_dumpster.append(number_result)

    return cumsum_dumpster


print(cumsum(t))
