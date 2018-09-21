'''
Write a decorator function that wraps text passed to it in <p> tags.

'''

def paragraphed(f):
    def wrapped():
        return '<p>' + f() + '</p>'
    return wrapped

@paragraphed
def original_text():
    original_text = "This is my paragraph. There are many like it but this one is mine."
    return original_text

print original_text()
