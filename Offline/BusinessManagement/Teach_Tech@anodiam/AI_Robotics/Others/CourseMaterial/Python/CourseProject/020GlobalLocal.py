x = 5                                       # GLOBAL VARIABLE

def random():
    x = 10                                  # LOCAL VARIABLE
    y = 7
    print("My Local Variable:", x)
    print("My Local Variable:", y)

print("My Global Variable:", x)
random()

x = 2

def random():

    print("My Local Variable:", x)         # GLOBAL USABLE INSIDE A FUNCTION

print("My Global Variable:", x)

random()

x = 2
def random():
    global x                              # ASSIGNING LOCAL AS GLOBAL

    x = 8
    print("My Local Variable :", x)

random()
print("My Global Variable :", x)

x = 2

def random():
    x = 8
    y = globals()["x"]                    # USING GLOBAL VARIABLE TO CREATE LOCAL

    print("My New Variable", y)
    print("My Local Variable :", x)

    print("My New Var Address:", id(y))   # ADDRESS SIMILAR AS GLOBAL

random()
print("My Global Variable :", x)
print("My Global Var Address:", id(x))
