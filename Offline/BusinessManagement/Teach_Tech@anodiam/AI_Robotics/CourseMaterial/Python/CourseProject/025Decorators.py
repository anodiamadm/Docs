# EXAMPLE OF DECORATORS IN PYTHON

def sub(x,y):
    print(x - y)

def smart_sub(f):

    def inside(x,y):           # inside FUNCTION CREATED INSIDE smart_sub FUNCTION
        if x < y:
            x,y = y,x
        return f(x,y)

    return inside              # RETURNING inside FUNCTION TO smart_sub FUNCTION

sub= smart_sub(sub)            # PASSING sub FUNCTION AS ARGUMENT TO smart_sub AND AN OBJECT CREATED

sub(5,65)
