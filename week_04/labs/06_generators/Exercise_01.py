'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

gen = (x for x in nums if x % 11111 == 0)

for index, value in enumerate(gen):
    print(value)

print(gen)
