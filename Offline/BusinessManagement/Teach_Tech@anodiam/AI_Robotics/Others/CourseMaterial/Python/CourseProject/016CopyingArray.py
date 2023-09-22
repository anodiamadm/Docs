from numpy import *

a1 = array([1, 2, 3, 4, 5, 6])           # VECTORIZED OPERATION
a2 = array([7, 8, 9, 10, 11, 12])
a3 = a1 + a2
print("Sum of two arrays:", a3)

a4 = a1 + 2                              # ADDING A VALUE WITH ALL ELEMENTS
print(a4)

print(sum(a1))                           # SUM OF ALL ELEMENTS
print(min(a1))                           # ELEMENT WITH THE MINIMUM VALUE
print(concatenate([a1,a2]))              # CONCATENATING TWO ARRAYS

a5 = array([7, 8, 9, 6])
a6 = a5                                  # ALIASING
print(a6)
print(id(a5))
print(id(a6))

a6 = a5.view()                           # SHALLOW COPY
print(id(a6))


a6 = a5.copy()                           # DEEP COPY
print(id(a6))
a5[1] = 10
print(a5)
print(a6)

