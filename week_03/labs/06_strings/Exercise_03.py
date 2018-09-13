'''
Complete Exercise 8.4 (p.96) from the textbook by writing out the docstrings for the functions.

Attributes:
    s (str): Description

'''
s = 'Chris Cocksman'

'''
def any_lowercase1(s):
    """Summary: Tests for lowercase letters and returns a boolean. Also, doesn't work.

    Args:
        s (TYPE): string

    Returns:
        TYPE: Boolean (False)
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


print (any_lowercase1(s))


def any_lowercase2(s):
    """Summary: Tests for lowercase letters and returns a boolean. Doesn't work. Is terrible.

    Args:
        s (TYPE): string

    Returns:
        TYPE: Boolean (True)
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Summary: Tests for lowercase letters and returns a boolean. Doesn't work. Is terrible.

    Args:
        s (TYPE): String

    Returns:
        TYPE: Boolean


    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Summary: Tests for lowercase letters and returns a boolean. Doesn't work. Flag will always equal flag.

    Args:
        s (TYPE): String

    Returns:
        TYPE: Boolean
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
'''


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


print (any_lowercase5(s))
