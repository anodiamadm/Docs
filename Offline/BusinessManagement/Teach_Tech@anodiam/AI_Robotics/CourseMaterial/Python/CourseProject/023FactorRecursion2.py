import sys

sys.setrecursionlimit(10000)

print(sys.getrecursionlimit())

i = 0

def say():
    global i
    i += 1
    print("Hey", i)
    say()

say()


# FACTORIAL USING RECURSION

def factor(n):

    if n == 0:
        return 1

    return n * factor(n-1)

result = factor(5)

print(result)
