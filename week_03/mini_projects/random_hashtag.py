'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random
import this



# Read in the file
with open('/usr/share/dict/words', 'r') as file :
  filedata = file.read()

print(type(filedata))
# print(random.choice(new_string)
