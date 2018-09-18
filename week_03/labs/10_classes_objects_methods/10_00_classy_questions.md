## Classes and OOP

- What is a class?

A programmer-defined type. (aka blueprints for creating objects)

- How do you define a new class called `MyFirstClass`?

class MyFirstClass():

Have to be capital.

- How do you create an object of the class `MyFirstClass`?

Object = class(arguments)

my_first_instance = MyFirstClass()

- What is instantiation?

Assigning a class to a variable to create an object.

- What are attributes?

Characteristics of a class of objects that are defined in the class.

- What does it mean when an object is embedded?

It's when an object is used to define attributes in a Class.

- What is the difference between `copy.copy` and `copy.deepcopy`?

What do they each do?

copy.copy - A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only one level deep. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

copy.deepcopy A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.

- What is the difference between a pure function and a modifier?

  Pure functions do not product side effects (they don't change attributes in a class)

  A modifier function makes a change to class or object attributes.

- What is object-oriented programming?

  ## Methods (page 161)

- What is a method?

  A function defined in a class.

- How is a method different than a function?

  Method is similar to a function, but is internal to part of a class. It has access to a self instance of a class.

- What is invocation?

  Calling a function.

  class MyClass:
    pass

  x. = MyClass()
  x.method()

- What is the `__init__` method and what is it used for?

  __init__ is a special method in Python classes, it is the constructor method for a class.

  How to instantiate and create an object.

- Give an example `__init__` method for a `Car` class with attributes: 'make`, `model` and `year'.

  class Car():

    def __init__(self, make, model, year):
                self.make = make
                self.model = model
                self.year = year
                print("A student object is created.")

- How do `__init__` methods handle variable arguments?

    Makes class have malleable attributes.

- What is the `__str__` method used for?

    __str__ is the built-in function in python, used for string representation of object.

- How do you use a `__str__` method?

    The init method (short for “initialization”) is a special method that gets invoked when an object is instantiated. Its full name is __init__ (two underscore characters, followed by init, and then two more underscores). An init method for the Time class might look like this:

    # inside class Time:

        def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.minute = minute
            self.second = second

- What is operator overloading?

  Changing the behavior of an operator so that it works with programmer-defined types is called operator overloading.

- What is an example of operator overloading?

  class Order():
    def __init__(self, car, customer):
      self.cart = list(cart)
      self.customer = customer

    def __len__(self): #len is used to directly obtain the length of the cart
      return len(self.cart)


- What is polymorphism?

    Sometimes an object comes in many types or forms. For example on a web page there are many different buttons - big ones, little ones, hypertext links - but they do share the same logic: click on them to go somewhere else.  This idea is called Polymorphism.

    Example:

        class Bear(object):
          def sound(self):
            print "Groarrr"

        class Dog(object):
          def sound(self):
            print "Woof woof!"

        def makeSound(animalType):
          animalType.sound()


        bearObj = Bear()
        dogObj = Dog()

        makeSound(bearObj)
        makeSound(dogObj)

- Why is polymorphism beneficial?

  It enables simpler abstraction.


