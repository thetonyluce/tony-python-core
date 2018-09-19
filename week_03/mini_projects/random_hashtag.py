'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random

# Read in the file
with open('/usr/share/dict/words', 'r') as file:
    file_data = file.read()
    file_data = file_data.split()

print(random.choice(file_data))
# print(random.choice(new_string)
