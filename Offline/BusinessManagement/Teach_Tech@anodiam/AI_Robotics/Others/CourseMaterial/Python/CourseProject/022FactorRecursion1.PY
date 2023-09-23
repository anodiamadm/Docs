# FINDING FACTORIAL OF A NUMBER

def factor(n):
    a = 1

    for i in range(1, n + 1):
        a = a * i

    return a

x = 10

result = factor(x)

print(result)


# RECURSION

import sys

sys.setrecursionlimit(2000)     # SETTING RECURSION LIMIT

print(sys.getrecursionlimit())  # FINDING RECURSION LIMIT

def say():
    print("Hey")
    say()                       # USING RECURSION

say()
