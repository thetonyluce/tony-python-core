## Classes and OOP

- What is a class?

A programmer-defined type. (aka blueprints for creating objects)

- How do you define a new class called `MyFirstClass`?

class MyFirstClass:

- How do you create an object of the class `MyFirstClass`?

Object = class(arguments)

- What is instantiation?

Assigning a class to a variable to create an object.

- What are attributes?

characteristics of a class of objects that are defined in the class.

- What does it mean when an object is embedded?

It's when an object is used to define attributes in a Class

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?

copy.copy - A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only one level deep. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

copy - deepcopy A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.

- What is the difference between a pure function and a modifier?

Pure functions do not product side effects (they )

- What is object-oriented programming?


## Methods (page 161)

- What is a method?

A function defined in a class.

- How is a method different than a function?

 method is similar to a function, but is internal to part of a class.

- What is invocation?

Calling a function.

- What is the `__init__` method and what is it used for?

__init__ is a special method in Python classes, it is the constructor method for a class.

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year.

class Car:

def __init__(self, make,  model, year):
            self.make = make
            self.model = model
            self.year = year
            print("A student object is created.")

- How do `__init__` methods handle variable arguments?

Makes class have malleable attributes.

- What is the `__str__` method used for?

__str__ is the built-in function in python, used for string representation of object._]

- How do you use a `__str__` method?



- What is operator overloading?



- What is an example of operator overloading?


## TYPE-BASED DISPATCH?

- What is polymorphism?

- Why is polymorphism beneficial?
