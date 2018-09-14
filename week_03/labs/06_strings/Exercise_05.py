'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
user_input = input('Write something:')

lower_case = user_input.lower()
upper_case = user_input.upper()

vowels = "aeiouAEIOU"

print(lower_case)
print(upper_case)


def in_both(word, vowels):
    upper_case_consonants = ""

    for letter in word:

        if letter in vowels:
            letter = letter.lower()

        else:
            letter = letter.upper()

        upper_case_consonants += letter

    return upper_case_consonants


mixed_result = in_both(user_input, vowels)
print(mixed_result)
