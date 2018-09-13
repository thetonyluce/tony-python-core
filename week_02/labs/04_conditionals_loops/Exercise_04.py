'''
Print out every prime number between 1 and 100.

'''

for x in range(1, 100):

    for y in range(2, x):
        if x % y == 0:
            break
    else:
        print (x)
