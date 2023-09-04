from numpy import *

MyArr = array([[1, 2, 3], [4, 5, 6]])  # MULTIDIMENSIONAL ARRAYS
print("My multidimensional array:", MyArr)

MyArr = array([4, 78, 97, 56, 43.0])  # FINDING ARRAY TYPE
print("My Array Type:", MyArr.dtype)

MyArr = array([4, 78, 97, 56, 43.9864567], int)  # SPECIFYING ARRAY TYPE
print("My Array Type:", MyArr.dtype)
print(MyArr)

MNArr = linspace(23, 69)       # ARRAY CREATION WITHOUT RANGE linspace()
print("My New Array:", MNArr)
MNArr = linspace(23, 69, 3)    # ARRAY CREATION WITH RANGE SPECIFIED linspace()
print("My New Array:", MNArr)

MNArr = arange(23, 69)         # ARRAY CREATION WITHOUT RANGE arange()
print("My New Array:", MNArr)
MNArr = arange(23, 69, 3)      # ARRAY CREATION WITH RANGE arange()
print("My New Array:", MNArr)

MNArr = logspace(23, 69)       # ARRAY CREATION WITHOUT RANGE logspace()
print("My New Array:", MNArr)
MNArr = logspace(23, 69, 3)    # ARRAY CREATION WITH RANGE logspace()
print("My New Array:", MNArr)
print('%2f' %MNArr[2])         # PRINTING THE VALUE AT INDEX 2 IN NORMAL NUMBERS

MNArr = zeros(8)               # ARRAY CREATION WITH zeros()
print(MNArr)

MNArr = ones(8)                # ARRAY CREATION WITH ones()
print(MNArr)
MNArr = ones(8, int)           # FOR PRINTING IN INTEGER
print(MNArr)
