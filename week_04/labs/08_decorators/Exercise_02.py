'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''

def paragraphed(called_function):
    def wrapped():
        return '<p>' + called_function() + '</p>'
    return wrapped

@paragraphed
def original_text():
    print("Before")
    user_text = "Go ahead and write something:"
    print("After")
    return user_text

print (original_text())
