'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
today_population = 380123456
seconds_per_year = 365 * 24 * 60 * 60
annual_births = seconds_per_year / 6
annual_deaths = seconds_per_year / 12
annual_immigration = seconds_per_year / 40
annual_pop_growth = annual_births + annual_deaths + annual_immigration
pop_projection = (3 * annual_pop_growth) + today_population
print ('Population Projection for 2021:', pop_projection)
