
class Student:                                       # OUTER CLASS

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.pc = self.PC()                          # DEFINING OBJECT OF INNER INSIDE OUTER CLASS

    def info(self):
        print(self.name, self.rollno)
        self.pc.info()


    class PC:                                        # INNER CLASS

        def __init__(self):
            self.brand = "HP"
            self.ram = 8

        def info(self):
            print(self.brand, self.ram)


s1 = Student("Rupa", 24)
s2 = Student("Monika", 25)

s1.info()
s2.info()

pc1 = Student.PC()                                     # DEFINING OBJECT OF INNER CLASS OUTSIDE
