'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

userInput = 0
while True:
  try:
     userInput = int(input("Enter any integer: "))
  except ValueError:
     print("Not an integer! Mom drop you as a kid?")
     continue
  else:
     print("There ya go.")
     break
