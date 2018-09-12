'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''
celsius_temp = float(input('Enter Celsius temperature for conversion:'))
fahrenheit_temp = celsius_temp * 1.8 + 32.0
print (celsius_temp, 'degrees Celsius = ', fahrenheit_temp, 'degrees Fahrenheit')
