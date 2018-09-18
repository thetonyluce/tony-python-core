'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open('12_files/words2.txt', 'r') as f: #open this file as variable f
for word in f.readlines():                  #read file line by line
        word = word.rstrip()                #strip whitespace characters
        if len(word) > 20:                  #if length of word > 20
            print(word)                     #print results
