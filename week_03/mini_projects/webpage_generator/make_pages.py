'''A script to convert any .txt file into a simple HTML make_pages
'''

import os

# Read in the file
with open('/Users/anthonyluce/CodingNomads/Labs/python_core/week_03/mini_projects/webpage_generator/raw/barcelona.txt', 'r') as file:
    header = file.readline()
    body = file.readlines()

with open('/Users/anthonyluce/CodingNomads/Labs/python_core/week_03/mini_projects/webpage_generator/raw/barcelona.html', 'w') as f:
    my_header = f"<H1>{header}</h1>"
    my_body = f"<p>{body}</p>"
    f.write(my_header + my_body)

print(header)
print(body)
