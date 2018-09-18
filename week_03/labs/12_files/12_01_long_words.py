'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open('/Users/anthonyluce/CodingNomads/Labs/python_core/week_03/labs/12_files/words2.txt', 'r') as f:
    data = f.read()

print(data)


"""
last = data[-1].rstrip()

with open('output.txt'), 'w') as f:
    f.write(last)
"""
