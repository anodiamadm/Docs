def greet():                              # DEFINING A FUNCTION
    print("Hello Class")
    print("Good Morning")

greet()                                   # CALLING NEW FUNCTION

def add(x, y):                            # PASSING ARGUMENTS IN A NEW FUNCTION
    z = x + y
    print(z)

add(3, 9)                                 # 3 & 9 ARE ACTUAL ARGUMENTS

def add(x, y):                            # X & Y ARE FORMAL ARGUMENTS
    z = x + y
    return z                              # RETURNING THE VALUE

result = add(3, 9)                        # ASSIGNING TO RESULT
print(result)

def add_sub(x, y):
    z = x + y
    a = x - y
    return z, a                           # RETURNING TWO VALUES

result1, result2 = add_sub(3, 9)
print(result1, result2)

def girl(name, age):
    print(name)
    print(age)

girl('Rupa', 16)

def girl(name, age):                       # POSITION ARGUMENT
    print(name)
    print(age)

girl(age = 18, name = 'Mina')              # KEYWORD ARGUMENTS

def girl(name, age = 18):                  # DEFAULT ARGUMENT
    print(name)
    print(age)

girl('Rupa')
