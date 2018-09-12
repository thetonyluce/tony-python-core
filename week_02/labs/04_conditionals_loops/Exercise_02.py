'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''


Weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


user_number = input("Give me a number and I'll tell you a day:")

if user_number > 7:
    print ("Other")

else:
    if user_number >= 0:
        print (Weekdays, [user_input - 1])
