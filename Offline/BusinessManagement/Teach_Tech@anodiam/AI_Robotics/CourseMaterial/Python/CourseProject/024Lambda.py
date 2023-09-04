# ANONYMOUS FUNCTIONS LAMBDA

f = lambda x : x*x           # DEFINING A FUNCTION TO FIND SQUARE
result = f(3)
print(result)

g = lambda x,y : x-y         # DEFINING A FUNCTION FOR SUBTRACTION
result = g(8,6)
print(result)

# FILTER()

nums = [5, 6, 8, 9, 3, 13, 45, 64]

odd_nums= list(filter(lambda n : n%2!=0,nums))           # FILTERING ODD NUMBERS

print(odd_nums)

# MAP()

doubles = list(map(lambda n : n*2, odd_nums))            # DOUBLING THE ODD NUMBERS

print(doubles)

# REDUCE()

from functools import *

sum = reduce(lambda x,y: x+y, doubles)                   # SUM OF ALL NUMBERS

print(sum)
