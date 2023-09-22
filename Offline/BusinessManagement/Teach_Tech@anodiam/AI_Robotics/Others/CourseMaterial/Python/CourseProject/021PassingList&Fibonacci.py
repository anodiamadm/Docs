def count(lst):                                       # PASSING LIST TO A FUNCTION
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [43, 54, 65, 78, 3, 6, 10]

even, odd = count(lst)

print('even : {} and odd : {}'.format(even, odd))     # USE OF .FORMAT()



# PRINTING FIBONACCI SERIES

def fib(n):
    a = 0
    b = 1

    if n <= 0:                                        # IN CASE fib(n) IS NEGATIVE
        print('invalid input')
    else:

        if n == 1:
            print(a)

        else:
            print(a)
            print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(-3)
