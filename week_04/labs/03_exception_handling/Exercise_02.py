'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import os

file = 'week_04/labs/03_exception_handling/integers.txt'
try:
    file_data = open(file, 'r')
    file_data = int(file_data.readline()
except IOError:
    print(f"{file} does not exist in this universe. Try another.")
except ValueError:
    print('The first line appears to be not integer-ated.')
else:
    print(file_data + 1)
    file.close


# if os.path.exists(file):
#     with open(file, 'r') as file:
#         try:
#             file_data = file.readline()
#         except IOError:
#             print('An error occured trying to read the file.')
#         except:
#             print('Path not recognized! Please try again.')
#
#         while True:
#             try:
#                 file_data = int()
#                 break
#             except ValueError:
#                 print "ValueError: Oops! That was no valid number. Try again..."
#
# print(file_data)
