'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''


class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, firstname, lastname, staffID):
        Person.__init__(self, firstname, lastname)
        self.staffnumber = staffID

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber


class Boss(Employee):

    def __init__(self, firstname, lastname, staffID, bosstype):
        Employee.__init__(self, firstname, lastname, staffID)
        self.bosstype = bosstype

    def GetBoss(self):
        return self.GetEmployee() + ", " +  self.bosstype

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
z = Boss("Mr", "Burns", "01", "Evil")

print(x.Name())
print(y.GetEmployee())
print(z.GetBoss())
