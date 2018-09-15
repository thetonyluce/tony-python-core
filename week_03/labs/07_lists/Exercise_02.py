'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_1 = [0, 4, 6, 18, 25, 42, 100]
list_2 = [1, 4, 9, 24, 42, 88, 99, 100]

set1 = set(list_1)
set2 = set(list_2)

matched = set1.intersection(set2) # set(['dog', 'cat', 'donkey'])
unmatched = set1.symmetric_difference(set2) # set(['pig'])

print (list(matched))
print (list(unmatched))
