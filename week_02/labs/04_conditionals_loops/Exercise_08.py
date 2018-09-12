'''
Demonstrate the use of the "break" statement to exit a loop.

'''
while True:
    line = raw.input('> ')
    if line == 'done':
        break
    print line
