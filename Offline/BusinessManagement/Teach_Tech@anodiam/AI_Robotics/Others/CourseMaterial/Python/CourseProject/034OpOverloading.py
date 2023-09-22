class Student:
    def __init__(self, Eng, Math):
        self.Eng = Eng
        self.Math = Math


    def __add__(self, other):                      # OVERLOADING __add__ OPERATOR TO ADD TWO STUDENT OBJECTS
        ENG = self.Eng + other.Eng
        MATH = self.Math + other.Math
        Result = Student(ENG, MATH)

        return Result


    def __gt__(self, other):                       # OVERLOADING __gt__ TO COMPARE TWO STUDENT OBJECTS
        RupaRes = self.Eng + self.Math
        MonikaRes = other.Eng + other.Math

        if RupaRes > MonikaRes:
            return True
        else:
            return False


Rupa = Student(69, 70)
Monika = Student(78, 90)

Both = Rupa + Monika                               # ADDING TWO OBJECTS

print(Both.Eng)                                    # TOTAL ENGLISH MARKS

if Rupa > Monika:
    print("Rupa wins")
else:
    print("Monika wins")
