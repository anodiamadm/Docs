class Student:

    school = "Anodiam"                              # CLASS ATTRIBUTE

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2                                # INSTANCE ATTRIBUTE

    def average(self):                              # INSTANCE METHOD
        return(self.m1 + self.m2)/2

    def get_m1(self):                               # ACCESSOR
        return self.m1

    def set_m2(self, val):                          # MUTATOR
        self.m1 = val

    @classmethod
    def info(cls):                                  # CLASS METHOD
        print(cls.school)

    @staticmethod
    def fun():                                      # STATIC METHOD
        return "Static Method"


Rupa = Student(70, 90)
Monika = Student(60, 80)

print(Rupa.average())
print(Monika.average())

Student.info()

print(Student.fun())
