def add(a, *b):                     # VARIABLE LENGTH ARGUMENT
    c = a
    for i in b:
        c = c + i
    print(c)

add(17, 29, 387547, 40)

def add(*b):                        # EFFICIENT
    c = 0
    for i in b:
        c = c + i
    print(c)

add(17, 29, 387547, 40)


def girl(name, **data):             # KEYWORDED VARIABLE LENGTH ARGUMENT

    print(name)
    print(data)

girl("Rupa", age = 16, city = "Kolkata", phone = 293843)


def girl(name, **data):             # USING FOR LOOP

    print(name)

    for i,j in data.items():

        print(i, j)

girl("Rupa", age = 16, city = "Kolkata", phone = 293843)
