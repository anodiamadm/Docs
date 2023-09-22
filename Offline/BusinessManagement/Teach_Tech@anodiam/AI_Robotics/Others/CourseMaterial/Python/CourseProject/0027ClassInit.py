
class Person:                       # DEFINING CLASS

    def identity(self):             # DEFINING METHOD
        print(5.4, 16)


Rupa = Person()                     # MAKING OBJECT FROM CLASS
Monika = Person()

Person.identity(Rupa)               # CALLING THE METHOD USING CLASS BY PASSING OBJECT AS ARGUMENT
Person.identity(Monika)

Rupa.identity()                     # CALLING THE METHOD USING THE OBJECT ITSELF
Monika.identity()

# __init__ METHOD

class Person:

    occupation = "student"                       # CLASS ATTRIBUTE

    def __init__(self, height, age):             # PARAMETERIZED CONSTRUCTORS
        self.height = height
        self.age = age                           # INSTANCE ATTRIBUTES

    def identity(self):
        print("Identity is: ", self.height, self.age)


Rupa = Person(5.4, 16)
Monika = Person(5.2, 15)

Rupa.identity()
Monika.identity()

print(Rupa.occupation)               # PRINTING CLASS ATTRIBUTE
