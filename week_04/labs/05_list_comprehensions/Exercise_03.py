'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
#
# new_list = [expression(i) for i in old_list]

definitely_fish = [item for item in fish_tuple if (item[-4] == 'fish')]
#new_list = [expression(i) for i in old_list if filter(i)]

print(definitely_fish)
