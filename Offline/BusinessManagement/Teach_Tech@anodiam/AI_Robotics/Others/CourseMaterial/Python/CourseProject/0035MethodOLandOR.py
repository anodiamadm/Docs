# METHOD OVERLOADING CONCEPT (NO EXISTENCE IN PYTHON)

class Student:
    def __init__(self):
        pass

    def sum(self, a= None, b= None, c= None):                # OVERLOADED BY CERTAIN MEANS

        s = 0

        if  a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a

        return s


Rupa = Student()

print(Rupa.sum(56,89,45))

# METHOD OVERRIDING

class A:

    def info(self):
        print("Anodiam")

class B(A):
    pass

Obj = B()
Obj.info()

# ANOTHER EXAMPLE OF OVERRIDING

class A:

    def info(self):
        print("Anodiam")

class B(A):
    def info(self):
        print("Ball")

Obj = B()
Obj.info()
