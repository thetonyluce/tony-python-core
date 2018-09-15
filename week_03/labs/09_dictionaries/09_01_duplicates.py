'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''
import operator
import collections

string_list = [1,2,3,4,5,5,5,6,6,8,9,10,11,12,12,16]
counted_frequency = collections.Counter(string_list)
inv_count = {v: k for k, v in counted_frequency.items()}

def has_dupes(d):
    for key, value in d.items():
        if value > 1:
            return ('You have been duped.')

        else:
            return ('Not so duped, are you?')

result = has_dupes(inv_count)
print(result)
