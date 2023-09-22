
class Person:
    pass                   # KEYWORD FOR EMPTY CLASS

Per1 = Person()
print(id(Per1))            # HEAP MEMORY ALLOCATED BY CONSTRUCTOR


class Person:

    def __init__(self):                 # DEFAULT/ NON-PARAMETERIZED CONSTRUCTOR
        self.name = "Rupa"
        self.age = 16

per1 = Person()
per2 = Person()

per1.name = "Monika"

print(per1.name, per2.name)

# COMPARING OBJECTS

class Person:

    def __init__(self):
        self.name = "Rupa"
        self.age = 16

    def compare(self, other):                  # DEFINING A METHOD TO COMPARE
        if self.age == other.age:
            return "same"
        else:
            return "not same"

per1 = Person()
per2 = Person()

per2.age = 18                                  # CHANGING PER2'S AGE

print(per1.compare(per2))
