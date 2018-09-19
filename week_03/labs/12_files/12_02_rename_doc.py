'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the 1st file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

# Read in the file
with open('12_files/fuck_martinez.txt', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('Fuck', 'Duck')
filedata = filedata.replace('fuck', 'duck')
filedata = filedata.replace('suck', 'cluck')

# Write the file out again
with open('12_files/duck_martinez.txt', 'w') as file:
    file.write(filedata)
