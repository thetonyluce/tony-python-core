'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def Name(self):
        return self.firstname + " " + self.lastname

class Kiddo(Person):

    def __init__(self, firstname, lastname, age):
        Person.__init__(self, firstname, lastname)
        self.age = age

    def GetKiddo(self):
        return self.Name() + ", " + self.age

    # def say_age:
    #     the_simpsons = {
    #     Homer : "You tried and you failed miserably. The lesson is - never try.",
    #     Marge : "Honey you should listen to your heart - not the voices in your head.",
    #     Bart : "If you don't watch the violence, you'll never get desensitized."


class Employee(Person):

    def __init__(self, firstname, lastname, staffID):
        Person.__init__(self, firstname, lastname)
        self.staffnumber = staffID

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

class Friend(Person):
    homer_friends = set[Barney Gumble, Moe Syslak, Apu]
    marge_friends = set[Edna, Patty, Luann]
    bart_friends = set[Milhouse, Nelson, Martin]
    lisa_friends = set[Allison, Ralph, Bleeding Gums Murphy]
    friends = {Homer : [homer_friends], Marge : marge_friends, Bart : bart_friends, Lisa : lisa_friends }

    def __init__(self, firstname, lastname, Friend):
        Person.__init__(self, firstname, lastname)
        self.Friend = Friend

    def GetFriend(self):
        if self.friend in homer_friends:
        return self.friend() + "is a friend of Homer!""

        elif self.friend in marge_friends:
        return self.friend() + "is a friend of Marge!"

        elif self.friend in bart_friends:
        return self.friend() + "is a friend of Bart!"

        elif self.friend in lisa_friends:
        return self.friend() + "is a friend of Bart!"

        else:
        return "Not sure who this is."


class Boss(Employee):

    def __init__(self, firstname, lastname, staffID, bosstype):
        Employee.__init__(self, firstname, lastname, staffID)
        self.bosstype = bosstype

    def GetBoss(self):
        return self.GetEmployee() + ", " +  self.bosstype






p = Person("Marge", "Simpson")
e = Employee("Homer", "Simpson", "1007")
b = Boss("Mr", "Burns", "01", "Evil")
k = Kiddo("Lisa", "Simpson", "11")
f = Friend("Marge S")

print(p.Name())
print(e.GetEmployee())
print(b.GetBoss())
print(k.GetKiddo())
print(k.GetFriend())
