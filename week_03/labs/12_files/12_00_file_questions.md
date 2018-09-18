# Files

Read through chapter ["Case Study: Word Play"](http://greenteapress.com/thinkpython2/html/thinkpython2010.html) as well as chapter ["Files"](http://greenteapress.com/thinkpython2/html/thinkpython2015.html) from
Allen B. Downey's Think Python 2e book.

- How do you open a file in read mode and print the first line?

    f = open("demofile.txt", "r")
    print(f.read())

- How can you use a for loop to iterate through the words of a file?

    f = open("demofile.txt", "r")
        for x in f:
          print(x)

- What does it mean when a program is persistent?

    In computer science, persistence refers to the characteristic of state that outlives the process that created it.

    From the book:

    Persistent Programs
        - Run for a long time (or all the time);
        - Keep at least some of their data in permanent storage
        - If shut down and restarted they pick up where they left off

- How do you open a file in write mode?

    open('filename.ext', 'w')


- Practice using f-strings as a replacement for the .format() method

    Also called “formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the __format__ protocol.


- What is the difference between a relative path and an absolute path?

    A relative path is a local path and to be access the script must be sitting in the same directorgy.
    An absolute path allows the file to be accessed from any directory

- What are some IOExceptions that you might encounter? How are they generated?

    It's what happens when you try to read a file that doesn't exist.

- What is a try statement used for?

    To get a valid input from the user.

    e.g.

    while True:
        try:
            x = int(input("Please enter a number:"))
            break

- What is an except statement used for?

    It delineates what to do when a user (or something else) causes an error.

    e.g.

    while True:
        try:
            x = int(input("Please enter a number:"))

    except ValueError:
        print ("Oops. That was not a number. Here's your sign.")

- Can you have a try without an except? Can you have an except without a try?

    You can not have try without an except. I believe you can have except without a try.

- What is the variable `__name__` used for?

  To determine whether or not a module is running on the main scope.

