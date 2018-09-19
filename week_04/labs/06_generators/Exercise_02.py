'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
nums = range(1, 1000000)

gen = (x for x in nums if x % 11111 == 0)

for index, value in enumerate(gen):
    new_value = value//1111
    print(new_value)

#we get the previous values, divided by 1111?
