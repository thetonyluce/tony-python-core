'''
Write a script that finds the first vowel in a a user inputted string.

'''

# Step 1 - define vowels
# Step 2 - request input from user
# Step 3 - read string from user
# Step 4 - comparing against vowels until first vowel then break and print


vowels = "aeiouAEIOU"


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
            break


word = input("Having trouble recognizing vowels? Enter your word and I'll tell you the first vowel in that word:")

in_both(vowels, word)
