'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

The provided code to start is in file Point1.py in this folder.

'''
import sys
import os
import math

class Point(object):
    """Represent point in 2-D space"""

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

def find_center(rectangle):
    p = Point()
    p.x = rectangle.corner.x + rectangle.width/2.0
    p.y = rectangle.corner.y + rectangle.height/2.0
    return p


def distance_between_points(p,q):
    y_diff = p.y - q.y
    x_diff = p.x = q.x
    y_sqr = math.pow(y_diff,2)
    x_sqr = math.pow(x_diff,2)
    x_y_sum = y_sqr + x_sqr
    return math.sqrt(x_y_sum)


def print_point(p):
    print '(%g, %g)' % (p.x, p.y)

def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy
    return rectangle

def main():
    # Create first Point object
    first = Point()
    first.x = 5
    first.y = 6
    # Create second Point object
    second = Point()
    second.x = 10
    second.y = 15

    print distance_between_points(first, second)

    # Create rectangle object
    my_rect = Rectangle()

    # Add a point as an attribute
    my_rect.corner = Point()
    my_rect.width = 10.0
    my_rect.height = 20.0

    # Create the Point's values
    my_rect.corner.x = 15
    my_rect.corner.y = 10
    print_point(my_rect.corner)

    # Move the rectangle around
    moved_rect = move_rectangle(my_rect, 5, 8)
    print_point(moved_rect.corner)


if __name__ == '__main__':
    main()
