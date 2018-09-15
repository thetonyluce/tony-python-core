'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at:
http://en.wikipedia.org/wiki/Letter_frequencies.
Solution: http://thinkpython2.com/code/most_frequent.py.

Source: Chapter on "Tuples" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2013.html

'''

import operator

#get input from user
user_input = input("Write something. Write Anything.: ")

#create a dicionary with letters and corresponding frequency
def frequency_analysis(user_input):
    d = dict()
    for c in user_input:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


#call the frequncy analysis
frequency_dict = frequency_analysis(user_input)

#sot the dictionary and print in reverse order
sorted_names = sorted(frequency_dict, key=lambda x: frequency_dict[x])
for k in sorted_names:
    print("{} : {}".format(k, frequency_dict[k]))
