'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
miles_to_drive = float(input('How many miles do you plan on putting on the old rumparoo?'))
miles_per_gallon = float(input('What kind of gas mileage do you get in that old rust bucket?'))
price_per_gallon = float(input('What does petrol run these days? Probably expensive!'))
cost_of_trip = (miles_to_drive / miles_per_gallon * price_per_gallon)
print (cost_of_trip)
